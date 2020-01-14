from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import date
from .models import *
import traceback
import datetime

from authentication.models import UserInfo, AcademicInfo
from master_forms.models import Semester, Section, Course, Subject, UserOperation


def error_save(error):
    """
    Redirecting to error page
    :param error:
    :return:
    """
    try:
        time = str(datetime.datetime.now())
        with open("error_log.txt", "a") as my_file:
            my_file.write(time + "\n")
            my_file.write(error + "\n\n")
        return error
    except:
        return redirect('error_handler_500')

    ####################################################################################################################
    # Notes #
    ####################################################################################################################


def notes(request):
    """
    Notes page view function for student and faculty
    depends on user profile
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
                               "section_obj": section_obj, "semester_obj": semesters_obj, "course_obj": course_obj,
                               "subject_obj": subject_obj, "notes_obj": notes_obj, "from_date": date_list[-1],
                               "to_date": date_list[0]})
            else:
                section_obj = AcademicInfo.objects.get(fk_user_info_id=session)
                notes_obj = AcademicNote.objects.filter(fk_sections=section_obj.fk_sections,
                                                        fk_course=section_obj.fk_course,
                                                        fk_semesters=section_obj.fk_semesters).order_by("-id")
                all_notes_obj = AcademicNote.objects.filter(fk_course=section_obj.fk_course,
                                                            fk_semesters=section_obj.fk_semesters,
                                                            fk_sections__isnull=True)
                return render(request, "academic_notes.html",
                              {"user_info_obj": user_info_obj, "notes_obj": notes_obj, "all_notes_obj": all_notes_obj})
        else:
            return redirect("/")
    except Exception:
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
    except Exception:
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
    except Exception:
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
    except Exception:
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
        notes_obj = AcademicNote.objects.get(id=notes_id)
        notes_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_notes(request):
    session = request.session.get('user_id')
    if session:
        if request.method == "POST":
            user_info_obj = UserInfo.objects.get(id=session)
            user_operations_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            print("in if post")
            course = request.POST.get("filter_course")
            sem = request.POST.get("filter_semesters")
            section = request.POST.get("filter_sections")
            subject = request.POST.get("filter_subject")
            start_date = request.POST.get("filter_from_date")
            end_date = request.POST.get("filter_to_date")

        print("subject ", subject)

        if start_date:
            start_date = datetime.datetime.strptime(str(request.POST.get("filter_from_date")), '%d/%m/%Y').strftime(
                '%Y-%m-%d')
        if end_date:
            end_date = datetime.datetime.strptime(str(request.POST.get("filter_to_date")), '%d/%m/%Y').strftime(
                '%Y-%m-%d')

        filter_str = "AcademicNote.objects"
        if sem:
            filter_str += ".filter(fk_semesters_id=sem)"
        if course:
            filter_str += ".filter(fk_course_id=course)"
        if subject:
            filter_str += ".filter(fk_subjects_id=subject)"
        if section:
            filter_str += ".filter(fk_sections_id=section)"
        if start_date:
            filter_str += ".filter(date_post__gte=start_date)"
        if end_date:
            filter_str += ".filter(date_post__lte=end_date)"
        if filter_str == "AcademicNote.objects":
            filter_str += ".all()"

        print(filter_str)

        notes_obj = eval(filter_str)

        render_string = render_to_string("faculty_filternotes.html",
                                         {"user_operations_obj": user_operations_obj, "notes_obj": notes_obj})
        return HttpResponse(render_string)
    else:
        return redirect("/")


def syllabus(request):
    """
    Syllabus page view
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        user_info_obj = UserInfo.objects.get(id=session)
        course_obj = Course.objects.all()
        semesters_obj = Semester.objects.all()
        subject_obj = Subject.objects.all()
        if user_info_obj.fk_user_type.user_type == "Faculty":
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            syllabus_obj = AcademicSyllabus.objects.all()
            return render(request, "faculty_syllabus.html", {"user_operation_obj": user_operation_obj,
                                                             "user_info_obj": user_info_obj,
                                                             "syllabus_obj": syllabus_obj,
                                                             "course_obj": course_obj, "semester_obj": semesters_obj,
                                                             "subject_obj": subject_obj})
        else:
            semester_obj = AcademicInfo.objects.get(fk_user_info_id=session)
            syllabus_obj = AcademicSyllabus.objects.filter(fk_course=semester_obj.fk_course,
                                                           fk_semesters=semester_obj.fk_semesters)
            return render(request, "academic_syllabus.html", {"user_info_obj": user_info_obj,
                                                              "syllabus_obj": syllabus_obj})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')

    ####################################################################################################################
    # Syllabus #
    ####################################################################################################################


@csrf_exempt
def add_syllabus(request):
    """
    Add syllabus
    :param request:
    :return:
    """
    try:
        date_today = date.today()
        title = request.POST.get("title")
        session = request.session.get('user_id')
        info = request.POST.get("syllabus_info")
        file = request.FILES.get("file")
        subject = request.POST.get("subject")
        semester = request.POST.get("semester")
        course = request.POST.get("course")
        # Getting syllabus objects
        user_info_obj = UserInfo.objects.get(id=session)
        if user_info_obj.fk_user_type.user_type == "Faculty":
            # Saving assignment details to database
            if request.method == 'POST':
                syllabus_obj = AcademicSyllabus(fk_user_info_id=session,
                                                syllabus_title=title,
                                                syllabus_detail=info,
                                                syllabus_file=file,
                                                date_post=date_today,
                                                fk_subjects_id=subject,
                                                fk_semesters_id=semester,
                                                fk_course_id=course)
                syllabus_obj.save()
        return redirect("/syllabus")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def delete_syllabus(request):
    """
    Delete syllabus
    :param request:
    :return:
    """
    try:
        syllabus_id = request.POST.get("id")
        syllabus_obj = AcademicSyllabus.objects.get(id=syllabus_id)
        syllabus_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def edit_syllabus(request):
    """
    edit syllabus
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        syllabus_id = request.POST.get("id")
        syllabus_obj = AcademicSyllabus.objects.get(id=syllabus_id)
        dict_data['id'] = syllabus_obj.id
        dict_data['syllabus_title'] = syllabus_obj.syllabus_title
        dict_data['syllabus_detail'] = syllabus_obj.syllabus_detail
        dict_data['syllabus_file'] = str(syllabus_obj.syllabus_file.url)[16:]
        dict_data['syllabus_file_name'] = str(syllabus_obj.syllabus_file.url)
        dict_data['fk_semesters'] = syllabus_obj.fk_semesters.id
        dict_data['fk_course'] = syllabus_obj.fk_course.id
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def update_syllabus(request):
    """
    update syllabus
    :param request:
    :return:
    """
    try:
        date_today = date.today()
        syllabus_id = request.POST.get("syllabus_id")
        title = request.POST.get("edit_title")
        session = request.session.get('user_id')
        info = request.POST.get("edit_syllabus_info")
        file = request.FILES.get("edit_file")
        subject = request.POST.get("edit_subject")
        semester = request.POST.get("edit_semester")
        course = request.POST.get("edit_course")
        syllabus_obj = AcademicSyllabus.objects.get(id=syllabus_id)
        syllabus_obj.fk_user_info_id = session
        syllabus_obj.syllabus_title = title
        syllabus_obj.syllabus_detail = info
        syllabus_obj.date_post = date_today
        if file:
            syllabus_obj.syllabus_file = file
        syllabus_obj.fk_subjects_id = subject
        syllabus_obj.fk_semesters_id = semester
        syllabus_obj.fk_course_id = course
        syllabus_obj.save()
        return redirect("/syllabus")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')

    ####################################################################################################################
    # Assignments #
    ####################################################################################################################


@csrf_exempt
def assignment(request):
    """
    Assignment page view
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        section_obj = Section.objects.all()
        semesters_obj = Semester.objects.all()
        course_obj = Course.objects.all()
        subject_obj = Subject.objects.all()
        user_info_obj = UserInfo.objects.get(id=session)
        time_now = timezone.now().date() - timezone.timedelta(days=1)  # Getting Current Time
        from_date = timezone.now().date() - timezone.timedelta(days=30)
        to_date = timezone.now().date()
        if user_info_obj.fk_user_type.user_type == "Faculty":
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            assignment_obj = Assignment.objects.filter(date_post__gte=from_date, date_post__lte=to_date)
            submitted_assignments_obj = SubmittedAssignment.objects.all()
            academic_info_obj = AcademicInfo.objects.all()
            return render(request, "faculty_assignment.html",
                          {"user_operation_obj": user_operation_obj, "section_obj": section_obj,
                           "semester_obj": semesters_obj,
                           "course_obj": course_obj, "subject_obj": subject_obj,
                           "assignment_obj": assignment_obj,
                           "submitted_assignments_obj": submitted_assignments_obj,
                           "academic_info_obj": academic_info_obj, "user_info_obj": user_info_obj,
                           "time_now": time_now, "from_date": from_date, "to_date": to_date})
        else:
            assignment_obj = SubmittedAssignment.objects.filter(fk_user_info_id=session)
            return render(request, "assignment.html",
                          {"assignment_obj": assignment_obj, "user_info_obj": user_info_obj, "time_now": time_now})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def save_assignment(request):
    """
    save and update assignment
    :param request:
    :return:
    """
    try:
        date_today = date.today()
        title = request.POST.get("title")
        session = request.session.get('user_id')
        info = request.POST.get("info")
        file = request.FILES.get("file")
        date_final = request.POST.get("date_final")
        subject = request.POST.get("subject")
        section = request.POST.get("section")
        semester = request.POST.get("semester")
        course = request.POST.get("course")
        user_info_obj = UserInfo.objects.get(id=session)
        student_list = request.POST.get("student_list")
        key = request.POST.get("key")
        assignment_id = request.POST.get("assignment_id")

        if user_info_obj.fk_user_type.user_type == "Faculty":
            date_final = datetime.datetime.strptime(str(date_final), '%d/%m/%Y')
            if request.method == 'POST':
                if key == "Submit":
                    assignment_obj = Assignment(fk_user_info_id=session,
                                                assignment_title=title,
                                                assignment_info=info,
                                                assignment_file=file,
                                                date_post=date_today,
                                                date_final=date_final,
                                                fk_subjects_id=subject,
                                                fk_sections_id=section,
                                                fk_semesters_id=semester,
                                                fk_course_id=course)
                    assignment_obj.save()

                    if student_list:
                        for i in student_list.split(','):
                            submitted_assignment = SubmittedAssignment(fk_user_info_id=i,
                                                                       fk_assignment_title_id=assignment_obj.id)
                            submitted_assignment.save()
                    else:
                        if section:
                            academic_info_obj = AcademicInfo.objects.filter(fk_sections_id=section,
                                                                            fk_course_id=course,
                                                                            fk_semesters_id=semester)
                        else:
                            academic_info_obj = AcademicInfo.objects.filter(fk_course_id=course,
                                                                            fk_semesters_id=semester)

                        for i in academic_info_obj:
                            submitted_assignment = SubmittedAssignment(fk_user_info_id=i.fk_user_info_id,
                                                                       fk_assignment_title_id=assignment_obj.id)
                            submitted_assignment.save()

                else:
                    assignment_obj = Assignment.objects.get(id=assignment_id)
                    if section:
                        if assignment_obj.assignment_title == title and assignment_obj.fk_subjects.id == int(
                                subject) and assignment_obj.fk_sections.id == int(
                            section) and assignment_obj.fk_semesters.id == int(
                            semester) and assignment_obj.fk_course.id == int(
                            course) and not file:
                            pass
                        else:
                            assignment_obj.fk_user_info_id = session
                            assignment_obj.assignment_title = title
                            assignment_obj.assignment_info = info
                            if file:
                                assignment_obj.assignment_file = file
                            assignment_obj.date_post = date_today
                            assignment_obj.date_final = date_final
                            assignment_obj.fk_subjects_id = subject
                            assignment_obj.fk_sections_id = section
                            assignment_obj.fk_semesters_id = semester
                            assignment_obj.fk_course_id = course
                            assignment_obj.save()

                            SubmittedAssignment.objects.filter(fk_assignment_title_id=assignment_obj.id).delete()
                    else:
                        if assignment_obj.assignment_title == title and assignment_obj.fk_subjects.id == int(
                                subject) and assignment_obj.fk_semesters.id == int(
                            semester) and assignment_obj.fk_course.id == int(
                            course) and not file:
                            pass
                        else:
                            assignment_obj.fk_user_info_id = session
                            assignment_obj.assignment_title = title
                            assignment_obj.assignment_info = info
                            if file:
                                assignment_obj.assignment_file = file
                            assignment_obj.date_post = date_today
                            assignment_obj.date_final = date_final
                            assignment_obj.fk_subjects_id = subject
                            assignment_obj.fk_semesters_id = semester
                            assignment_obj.fk_course_id = course
                            assignment_obj.save()

                            SubmittedAssignment.objects.filter(fk_assignment_title_id=assignment_obj.id).delete()

                    SubmittedAssignment.objects.filter(fk_assignment_title_id=assignment_obj.id,
                                                       submission_date__isnull=True).delete()
                    if student_list:
                        for i in student_list.split(','):
                            if SubmittedAssignment.objects.filter(fk_user_info_id=i,
                                                                  fk_assignment_title_id=assignment_obj.id).exists():
                                pass
                            else:
                                submitted_assignment = SubmittedAssignment(fk_user_info_id=i,
                                                                           fk_assignment_title_id=assignment_obj.id)
                                submitted_assignment.save()
                    else:
                        if section:
                            academic_info_obj = AcademicInfo.objects.filter(fk_sections_id=section,
                                                                            fk_course_id=course,
                                                                            fk_semesters_id=semester)
                        else:
                            academic_info_obj = AcademicInfo.objects.filter(fk_course_id=course,
                                                                            fk_semesters_id=semester)

                        for i in academic_info_obj:
                            if SubmittedAssignment.objects.filter(fk_user_info_id=i.fk_user_info_id,
                                                                  fk_assignment_title_id=assignment_obj.id).exists():
                                pass
                            else:
                                submitted_assignment = SubmittedAssignment(fk_user_info_id=i.fk_user_info_id,
                                                                           fk_assignment_title_id=assignment_obj.id)
                                submitted_assignment.save()
        else:
            if request.method == 'POST':
                assignment_id = request.POST.get("assignment_title")
                submission_date = date_today
                submitted_file = request.FILES.get("file")
                submitted_assignment = SubmittedAssignment.objects.get(fk_user_info_id=session,
                                                                       fk_assignment_title_id=assignment_id)
                submitted_assignment.submission_date = submission_date
                submitted_assignment.submitted_file = submitted_file
                submitted_assignment.save()
        return redirect('assignment')
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def delete_assignment(request):
    """
    Delete Assignment
    :param request:
    :return:
    """
    try:
        assignment_id = request.POST.get("id")
        assignments_obj = Assignment.objects.get(id=assignment_id)
        assignments_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def edit_assignment(request):
    """
    Get details of assignment for editing
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        assignment_id = request.POST.get("id")
        assignments_obj = Assignment.objects.get(id=assignment_id)
        dict_data['id'] = assignments_obj.id
        dict_data['assignment_title'] = assignments_obj.assignment_title
        dict_data['assignment_info'] = assignments_obj.assignment_info
        dict_data['assignment_file_url'] = str(assignments_obj.assignment_file.url)
        dict_data['assignment_file'] = str(assignments_obj.assignment_file.url)[19:]
        dict_data['date_final'] = datetime.datetime.strptime(str(assignments_obj.date_final),
                                                             '%Y-%m-%d').strftime('%d/%m/%Y')
        dict_data['fk_subjects'] = assignments_obj.fk_subjects.id
        if assignments_obj.fk_sections:
            dict_data['fk_sections'] = assignments_obj.fk_sections.id
        else:
            dict_data['fk_sections'] = ""
        dict_data['fk_semesters'] = assignments_obj.fk_semesters.id
        dict_data['fk_course'] = assignments_obj.fk_course.id
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def assignment_get_student_list(request):
    """
    Filtering out student by section,sem and course
    for sending the assignment
    :param request:
    :return:
    """
    try:
        sections = request.POST.get("sections")
        course = request.POST.get("course")
        semester = request.POST.get("semester")
        academic_info_obj = AcademicInfo.objects.filter(fk_sections_id=sections,
                                                        fk_course_id=course,
                                                        fk_semesters_id=semester)
        render_string = render_to_string("assignmentstudents.html", {"academic_info_obj": academic_info_obj})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_assignments(request):
    session = request.session.get('user_id')
    if session:
        user_info_obj = UserInfo.objects.get(id=session)
        user_operations_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        course = request.POST.get("filter_course")
        sem = request.POST.get("filter_semesters")
        section = request.POST.get("filter_sections")
        subject = request.POST.get("filter_subject")
        start_date = request.POST.get("filter_from_date")
        end_date = request.POST.get("filter_to_date")
        time_now = timezone.now().date() - timezone.timedelta(days=1)  # Getting Current Time

        if start_date:
            start_date = datetime.datetime.strptime(str(request.POST.get("filter_from_date")),
                                                    '%d/%m/%Y').strftime('%Y-%m-%d')
        if end_date:
            end_date = datetime.datetime.strptime(str(request.POST.get("filter_to_date")),
                                                  '%d/%m/%Y').strftime('%Y-%m-%d')

        filter_str = "Assignment.objects"
        if sem:
            filter_str += ".filter(fk_semesters_id=sem)"
        if course:
            filter_str += ".filter(fk_course_id=course)"
        if subject:
            filter_str += ".filter(fk_subjects_id=subject)"
        if section:
            filter_str += ".filter(fk_sections_id=section)"
        if start_date:
            filter_str += ".filter(date_post__gte=start_date)"
        if end_date:
            filter_str += ".filter(date_post__lte=end_date)"
        if filter_str == "Assignment.objects":
            filter_str += ".all()"
        print(filter_str)

        assignment_obj = eval(filter_str)
        print(filter_str)

        render_string = render_to_string("faculty_filterassignment.html",
                                         {"user_operations_obj": user_operations_obj, "assignment_obj": assignment_obj,
                                          "time_now": time_now})
        return HttpResponse(render_string)
    else:
        return redirect("/")


@csrf_exempt
def edit_student_list(request):
    """
    Edit or delete the selected student for assignment
    :param request:
    :return:
    """
    try:
        assignment_id = request.POST.get("id")
        student_list = SubmittedAssignment.objects.filter(fk_assignment_title_id=assignment_id)
        academic_info_obj = AcademicInfo.objects.all()
        render_string = render_to_string("edit_assignmentstudents.html", {"student_list": student_list,
                                                                          "academic_info_obj": academic_info_obj})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')
