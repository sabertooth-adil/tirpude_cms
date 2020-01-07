from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import datetime
from datetime import date
from .models import *
import traceback

from authentication.models import UserInfo, AcademicInfo
from master_forms.models import Semester, Section, Course, Subject, UserOperation


def error_save(error):
    time = str(datetime.datetime.now())
    with open("error_log.txt", "a") as my_file:
        my_file.write(time + "\n")
        my_file.write(error + "\n\n")
    print(error)
    return error


def notes(request):
    """
    Notes Page View Function
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        if session:
            section_obj = Section.objects.all()
            semesters_obj = Semester.objects.all()
            course_obj = Course.objects.all()
            subject_obj = Subject.objects.all()
            user_info_obj = UserInfo.objects.get(id=session)
            base = datetime.datetime.today()
            date_list = [base - datetime.timedelta(days=x) for x in range(30)]
            if user_info_obj.fk_user_type.user_type == "Faculty":
                user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
                notes_obj = AcademicNote.objects.filter(date_post__range=[date_list[-1], date_list[0]]).order_by("-id")
                return render(request, "faculty_notes.html",
                              {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                               "sections_obj": section_obj, "semester_obj": semesters_obj, "course_obj": course_obj,
                               "subject_obj": subject_obj, "notes_obj": notes_obj, "from_date": date_list[-1],
                               "to_date": date_list[0]})
            else:
                sections_obj = AcademicInfo.objects.get(fk_user_info_id=session)
                notes_obj = AcademicNote.objects.filter(fk_sections=sections_obj.fk_sections,
                                                        fk_course=sections_obj.fk_course,
                                                        fk_semesters=sections_obj.fk_semesters).order_by("-id")
                all_notes_obj = AcademicNote.objects.filter(fk_course=sections_obj.fk_course,
                                                            fk_semesters=sections_obj.fk_semesters,
                                                            fk_sections__isnull=True)
                return render(request, "academic_notes.html",
                              {"user_info_obj": user_info_obj, "notes_obj": notes_obj, "all_notes_obj": all_notes_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def save_notes(request):
    """
    Saving Academic Notes
    :param request:
    :return:
    """
    try:
        today_date = date.today()
        title = request.POST.get("title")
        session = request.session.get('user_id')
        info = request.POST.get("notes_info")
        file = request.FILES.get("file")
        subject = request.POST.get("subject")
        section = request.POST.get("section")
        semester = request.POST.get("semester")
        course = request.POST.get("course")
        print("title", title)
        print("session", session)
        print("info", info)
        print("file", file)
        print("file", file)
        print("subject", subject)
        print("section", section)
        print("semester", semester)
        print("course", course)
        # user_info_obj = UserInfo.objects.get(id=session)
        notes_obj = AcademicNote(fk_user_info_id=session,
                                 notes_title=title,
                                 notes_detail=info,
                                 notes_file=file,
                                 date_post=today_date,
                                 fk_subjects_id=subject,
                                 fk_sections_id=section,
                                 fk_semesters_id=semester,
                                 fk_course_id=course)
        notes_obj.save()
        return redirect('/notes/')
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def edit_notes(request):
    """
    edit notes function
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        notes_id = request.POST.get("id")
        notes_obj = AcademicNote.objects.get(id=notes_id)
        dict_data['id'] = notes_obj.id
        dict_data['notes_title'] = notes_obj.notes_title
        dict_data['notes_detail'] = notes_obj.notes_detail
        dict_data['notes_file_url'] = str(notes_obj.notes_file.url)
        dict_data['notes_file'] = str(notes_obj.notes_file.url)[13:]
        dict_data['date_post'] = notes_obj.date_post
        dict_data['fk_subjects'] = notes_obj.fk_subjects.id
        if notes_obj.fk_sections:
            dict_data['fk_sections'] = notes_obj.fk_sections.id
        else:
            dict_data['fk_sections'] = ""
            dict_data['fk_semesters'] = notes_obj.fk_semesters.id
            dict_data['fk_course'] = notes_obj.fk_course.id
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def update_notes(request):
    """
    Update notes
    :param request:
    :return:
    """
    try:
        today_date = date.today()
        academic_notes_id = request.POST.get("academic_notes_id")
        title = request.POST.get("edit_title")
        session = request.session.get('user_id')
        info = request.POST.get("edit_notes_info")
        file = request.FILES.get("edit_file")
        subject = request.POST.get("edit_subject")
        section = request.POST.get("edit_section")
        semester = request.POST.get("edit_semester")
        course = request.POST.get("edit_course")
        notes_obj = AcademicNote.objects.get(id=academic_notes_id)
        notes_obj.fk_user_info_id = session
        notes_obj.notes_title = title
        notes_obj.notes_detail = info
        if file:
            notes_obj.notes_file = file
        notes_obj.date_post = today_date
        notes_obj.fk_subjects_id = subject
        notes_obj.fk_sections_id = section
        notes_obj.fk_semesters_id = semester
        notes_obj.fk_course_id = course
        notes_obj.save()
        return redirect('/notes/')
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def delete_notes(request):
    """
    Delete Notes
    :param request:
    :return:
    """
    try:
        notes_id = request.POST.get("id")
        print(id)
        notes_obj = AcademicNote.objects.get(id=notes_id)
        notes_obj.delete()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')
