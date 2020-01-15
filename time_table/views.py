from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login, authenticate
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse, JsonResponse
from django.db.models import Avg, Max, Min, Sum
from django.shortcuts import render, redirect
from datetime import date
import datetime
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import F, Q
import random
from datetime import timedelta, date
from django.conf import settings
from django.core.mail import EmailMessage
import base64
import os
import os.path
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import traceback

from authentication.models import UserInfo, AcademicInfo
from authentication.views import error_save
from master_forms.models import Course, Semester, Section, Day, Time, UserOperation, Subject, Lecture
from time_table.models import TimeTableMaster, TimeTableDetail


def time_table(request):
    """
    Time Table Page
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        session = request.session.get('user_id')
        if session:
            course_obj = Course.objects.all()
            semester_obj = Semester.objects.all()
            section_obj = Section.objects.all()
            days_obj = Day.objects.all()
            time_obj = Time.objects.all()
            user_info_obj = UserInfo.objects.get(id=session)
            time_table_detail_obj = TimeTableMaster.objects.all()
            if user_info_obj.fk_user_type.user_type == "Student":
                academic_info_obj = AcademicInfo.objects.get(fk_user_info=user_info_obj)
                print("academic_info_obj", academic_info_obj)
                if TimeTableMaster.objects.filter(fk_course=academic_info_obj.fk_course,
                                                  fk_semesters=academic_info_obj.fk_semesters,
                                                  fk_sections=academic_info_obj.fk_sections).exists():
                    time_table_master_obj = TimeTableMaster.objects.get(fk_course=academic_info_obj.fk_course,
                                                                        fk_semesters=academic_info_obj.fk_semesters,
                                                                        fk_sections=academic_info_obj.fk_sections)
                    if TimeTableDetail.objects.filter(fk_timetable_master=time_table_master_obj).exists():
                        time_table_detail_monday_obj = TimeTableDetail.objects.filter(
                            fk_timetable_master=time_table_master_obj, fk_day_id=1).order_by('fk_time_start')
                        time_table_detail_tuesday_obj = TimeTableDetail.objects.filter(
                            fk_timetable_master=time_table_master_obj, fk_day_id=2).order_by('fk_time_start')
                        time_table_detail_wednesday_obj = TimeTableDetail.objects.filter(
                            fk_timetable_master=time_table_master_obj, fk_day_id=3).order_by('fk_time_start')
                        time_table_detail_thursday_obj = TimeTableDetail.objects.filter(
                            fk_timetable_master=time_table_master_obj, fk_day_id=4).order_by('fk_time_start')
                        time_table_detail_friday_obj = TimeTableDetail.objects.filter(
                            fk_timetable_master=time_table_master_obj, fk_day_id=5).order_by('fk_time_start')
                        time_table_detail_saturday_obj = TimeTableDetail.objects.filter(
                            fk_timetable_master=time_table_master_obj, fk_day_id=6).order_by('fk_time_start')

                        start_time = \
                            TimeTableDetail.objects.filter(fk_timetable_master=time_table_master_obj).order_by(
                                'fk_time_start')[
                                0].fk_time_start.id
                        end_time = \
                            TimeTableDetail.objects.filter(fk_timetable_master=time_table_master_obj).order_by(
                                '-fk_time_end')[
                                0].fk_time_end.id
                        time_range_obj = Time.objects.filter(id__range=(start_time, end_time))
                        print(start_time, end_time)
                        index = 0
                        for i in time_range_obj:
                            index = index + 1
                            if time_range_obj.count() == index:
                                pass
                            else:
                                dict_data['next_time'] = time_range_obj[index].time
                                dict_data['time'] = i.time
                                dict_data['id'] = i.id
                                list_data.append(dict_data)
                            dict_data = {}
                        print(list_data)
                        return render(request, "student_time_table.html", {"user_info_obj": user_info_obj,
                                                                           "time_table_detail_monday_obj": time_table_detail_monday_obj,
                                                                           "time_table_detail_tuesday_obj": time_table_detail_tuesday_obj,
                                                                           "time_table_detail_wednesday_obj": time_table_detail_wednesday_obj,
                                                                           "time_table_detail_thursday_obj": time_table_detail_thursday_obj,
                                                                           "time_table_detail_friday_obj": time_table_detail_friday_obj,
                                                                           "time_table_detail_saturday_obj": time_table_detail_saturday_obj,
                                                                           "time_table_master_obj": time_table_master_obj,
                                                                           "time_range_obj": time_range_obj,
                                                                           "list_data": list_data})
                    else:
                        return render(request, "student_time_table.html",
                                      {"user_info_obj": user_info_obj, "time_table_detail_monday_obj": "",
                                       "time_table_detail_tuesday_obj": "",
                                       "time_table_detail_wednesday_obj": "",
                                       "time_table_detail_thursday_obj": "",
                                       "time_table_detail_friday_obj": "",
                                       "time_table_detail_saturday_obj": "",
                                       "time_table_master_obj": time_table_master_obj, "time_range_obj": "",
                                       "list_data": ""})
                else:
                    return render(request, "student_time_table.html",
                                  {"user_info_obj": user_info_obj, "time_table_detail_monday_obj": "",
                                   "time_table_detail_tuesday_obj": "",
                                   "time_table_detail_wednesday_obj": "",
                                   "time_table_detail_thursday_obj": "",
                                   "time_table_detail_friday_obj": "",
                                   "time_table_detail_saturday_obj": "",
                                   "time_table_master_obj": "", "time_range_obj": "", "list_data": ""})
            else:
                user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
                return render(request, "time_table.html",
                              {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                               "course_obj": course_obj, "semester_obj": semester_obj, "section_obj": section_obj,
                               "days_obj": days_obj, "time_obj": time_obj,"time_table_detail_obj": time_table_detail_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_time_table(request):
    """
    Time Table Filter
    :param request:
    :return:
    """
    try:
        course = request.POST.get("course")
        semesters = request.POST.get("semesters")
        sections = request.POST.get("sections")
        lecture_obj = Lecture.objects.all()
        days_obj = Day.objects.all()
        time_obj = Time.objects.all()
        user_info_faculty_obj = UserInfo.objects.filter(fk_user_type__user_type="Faculty")
        if TimeTableMaster.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                          fk_sections_id=sections).exists():
            timetable_obj = TimeTableMaster.objects.get(fk_course_id=course, fk_semesters_id=semesters,
                                                        fk_sections_id=sections)
            time_table_detail_obj = TimeTableDetail.objects.filter(fk_timetable_master=timetable_obj, fk_day_id=1)
        else:
            timetable_obj = ""
            time_table_detail_obj = ""
        subjects_obj = Subject.objects.filter(fk_course_id=course, fk_semesters_id=semesters)
        render_string = render_to_string("create_timetable_div.html",
                                         {"time_table_detail_obj": time_table_detail_obj, "subjects_obj": subjects_obj,
                                          "lecture_obj": lecture_obj, "days_obj": days_obj, "time_obj": time_obj,
                                          "user_info_faculty_obj": user_info_faculty_obj,
                                          "timetable_obj": timetable_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def save_update_date_note_timetable(request):
    """
    save, update date note timetable
    :param request:
    :return:
    """
    try:
        course = request.POST.get("course")
        semesters = request.POST.get("semesters")
        sections = request.POST.get("sections")
        if TimeTableMaster.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                          fk_sections_id=sections).exists():
            timetable_obj = TimeTableMaster.objects.get(fk_course_id=course, fk_semesters_id=semesters,
                                                        fk_sections_id=sections)
            timetable_obj.from_date = datetime.datetime.strptime(str(request.POST.get("start_date")),
                                                                 '%d-%m-%Y').strftime(
                '%Y-%m-%d')
            timetable_obj.to_date = datetime.datetime.strptime(str(request.POST.get("end_date")), '%d-%m-%Y').strftime(
                '%Y-%m-%d')
            timetable_obj.note = request.POST.get("note")
            timetable_obj.save()
        else:
            timetable_obj = TimeTableMaster(fk_course_id=course, fk_semesters_id=semesters, fk_sections_id=sections)
            timetable_obj.save()
            timetable_obj.from_date = datetime.datetime.strptime(str(request.POST.get("start_date")),
                                                                 '%d-%m-%Y').strftime(
                '%Y-%m-%d')
            timetable_obj.to_date = datetime.datetime.strptime(str(request.POST.get("end_date")), '%d-%m-%Y').strftime(
                '%Y-%m-%d')
            timetable_obj.note = request.POST.get("note")
            timetable_obj.save()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def edit_time_table(request, id):
    """
    edit time table
    :param request:
    :param id:
    :return:
    """
    try:
        time_table_detail_obj = TimeTableDetail.objects.filter(fk_timetable_master_id=id, fk_day_id=1)
        time_table_master_obj = TimeTableMaster.objects.get(id=id)
        lecture_obj = Lecture.objects.all()
        days_obj = Day.objects.all()
        time_obj = Time.objects.all()
        session = request.session.get('user_id')
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        user_info_faculty_obj = UserInfo.objects.filter(fk_user_type__user_type="Faculty")
        subjects_obj = Subject.objects.filter(fk_course_id=time_table_master_obj.fk_course.id,
                                              fk_semesters_id=time_table_master_obj.fk_semesters.id)
        return render(request, "edit_time_table.html",
                      {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                       "time_table_detail_obj": time_table_detail_obj, "time_table_master_obj": time_table_master_obj,
                       "lecture_obj": lecture_obj, "days_obj": days_obj, "time_obj": time_obj,
                       "subjects_obj": subjects_obj,
                       "user_info_faculty_obj": user_info_faculty_obj})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def add_time_table(request):
    """
    add time table
    :param request:
    :return:
    """
    try:
        course = request.POST.get("course")
        semesters = request.POST.get("semesters")
        sections = request.POST.get("sections")
        lecture = request.POST.get("lecture")
        subject = request.POST.get("subject")
        day = request.POST.get("day")
        faculty = request.POST.getlist("faculty[]")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        lecture_break = request.POST.get("lecture_break")
        print("faculty", len(faculty))
        if TimeTableMaster.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                          fk_sections_id=sections).exists():
            timetable_obj = TimeTableMaster.objects.get(fk_course_id=course, fk_semesters_id=semesters,
                                                        fk_sections_id=sections)
            if lecture_break == "Lecture" and TimeTableDetail.objects.filter(fk_timetable_master=timetable_obj,
                                                                             fk_day_id=day,
                                                                             fk_lecture_id=lecture).exists():
                send_msg = {"msg": "Lecture No Already Exists", "status": "0"}
            elif TimeTableDetail.objects.filter(
                    Q(fk_timetable_master=timetable_obj, fk_day_id=day, fk_time_start_id=start_time) | Q(
                        fk_timetable_master=timetable_obj, fk_day_id=day, fk_time_end_id=end_time)).exists():
                send_msg = {"msg": "Time Already Used", "status": "0"}
            else:
                if lecture_break == "Break":
                    time_table_detail_obj = TimeTableDetail(fk_timetable_master=timetable_obj, fk_day_id=day,
                                                            fk_time_start_id=start_time, fk_time_end_id=end_time,
                                                            lecture_break=lecture_break)
                    time_table_detail_obj.save()
                    send_msg = {"msg": "success", "status": "1"}
                else:
                    if len(faculty) == 1:
                        if TimeTableDetail.objects.filter(
                                Q(Q(fk_faculty_user_info1_id=faculty[0]) | Q(fk_faculty_user_info2_id=faculty[0]),
                                  fk_day_id=day, fk_time_start__id=start_time) | Q(
                                    Q(fk_faculty_user_info1_id=faculty[0]) | Q(fk_faculty_user_info2_id=faculty[0]),
                                    fk_day_id=day, fk_time_end_id=end_time) | Q(
                                    Q(fk_faculty_user_info1_id=faculty[0]) | Q(fk_faculty_user_info2_id=faculty[0]),
                                    fk_day_id=day, fk_time_start__id__gte=start_time,
                                    fk_time_end_id__lte=end_time)).exists():
                            send_msg = {"msg": "Faculty is Busy", "status": "0"}
                        else:
                            time_table_detail_obj = TimeTableDetail(fk_timetable_master=timetable_obj, fk_day_id=day,
                                                                    fk_lecture_id=lecture, fk_subjects_id=subject,
                                                                    fk_time_start_id=start_time,
                                                                    fk_time_end_id=end_time,
                                                                    lecture_break=lecture_break,
                                                                    fk_faculty_user_info1_id=faculty[0])
                            time_table_detail_obj.save()
                            send_msg = {"msg": "success", "status": "1"}
                    if len(faculty) == 2:
                        if TimeTableDetail.objects.filter(Q(
                                Q(fk_faculty_user_info1_id=faculty[0]) | Q(fk_faculty_user_info1_id=faculty[1]) | Q(
                                    fk_faculty_user_info2_id=faculty[0]) | Q(fk_faculty_user_info2_id=faculty[1]),
                                fk_day_id=day, fk_time_start_id=start_time) | Q(
                            Q(fk_faculty_user_info1_id=faculty[0]) | Q(fk_faculty_user_info1_id=faculty[1]) | Q(
                                fk_faculty_user_info2_id=faculty[0]) | Q(fk_faculty_user_info2_id=faculty[1]),
                            fk_day_id=day, fk_time_end_id=end_time) | Q(
                            Q(fk_faculty_user_info1_id=faculty[0]) | Q(fk_faculty_user_info1_id=faculty[1]) | Q(
                                fk_faculty_user_info2_id=faculty[0]) | Q(fk_faculty_user_info2_id=faculty[1]),
                            fk_day_id=day, fk_time_start__id__gte=start_time, fk_time_end_id__lte=end_time)).exists():
                            send_msg = {"msg": "Faculty is Busy", "status": "0"}
                        else:
                            time_table_detail_obj = TimeTableDetail(fk_timetable_master=timetable_obj, fk_day_id=day,
                                                                    fk_lecture_id=lecture, fk_subjects_id=subject,
                                                                    fk_time_start_id=start_time,
                                                                    fk_time_end_id=end_time,
                                                                    lecture_break=lecture_break,
                                                                    fk_faculty_user_info1_id=faculty[0],
                                                                    fk_faculty_user_info2_id=faculty[1])
                            time_table_detail_obj.save()
                            send_msg = {"msg": "success", "status": "1"}

        print(send_msg)
        return JsonResponse(send_msg)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def change_time_table_day(request):
    """
    change time table day
    :param request:
    :return:
    """
    try:
        course = request.POST.get("course")
        semesters = request.POST.get("semesters")
        sections = request.POST.get("sections")
        day = request.POST.get("day")
        print(day)
        if TimeTableMaster.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                          fk_sections_id=sections).exists():
            timetable_obj = TimeTableMaster.objects.get(fk_course_id=course, fk_semesters_id=semesters,
                                                        fk_sections_id=sections)
            time_table_detail_obj = TimeTableDetail.objects.filter(fk_timetable_master=timetable_obj,
                                                                   fk_day_id=day).order_by('fk_time_start')
        else:
            time_table_detail_obj = ""
        render_string = render_to_string("day_timetable_div.html", {"time_table_detail_obj": time_table_detail_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def edit_day_time_table(request):
    """
    edit day time table
    :param request:
    :return:
    """
    try:
        list_data = []
        faculty_list = []
        dict_data = {}
        id = request.POST.get("id")
        time_table_detail_obj = TimeTableDetail.objects.get(id=id)
        dict_data['id'] = time_table_detail_obj.id
        dict_data['fk_timetable_master'] = time_table_detail_obj.fk_timetable_master.id
        if time_table_detail_obj.fk_subjects:
            dict_data['fk_subjects'] = time_table_detail_obj.fk_subjects.id
        else:
            dict_data['fk_subjects'] = ""
        dict_data['fk_day'] = time_table_detail_obj.fk_day.id
        if time_table_detail_obj.fk_lecture:
            dict_data['fk_lecture'] = time_table_detail_obj.fk_lecture.id
        else:
            dict_data['fk_lecture'] = ""
        dict_data['fk_time_start'] = time_table_detail_obj.fk_time_start.id
        dict_data['fk_time_end'] = time_table_detail_obj.fk_time_end.id
        dict_data['lecture_break'] = time_table_detail_obj.lecture_break
        if time_table_detail_obj.fk_faculty_user_info1:
            faculty_list.append(time_table_detail_obj.fk_faculty_user_info1.id)
        if time_table_detail_obj.fk_faculty_user_info2:
            faculty_list.append(time_table_detail_obj.fk_faculty_user_info2.id)
        dict_data['faculty_list'] = faculty_list
        list_data.append(dict_data)
        print(list_data)
        return JsonResponse({"list_data": list_data})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def update_time_table(request):
    """
    update time table
    :param request:
    :return:
    """
    try:
        time_table_detail_id = request.POST.get("time_table_detail_id")
        time_table_master_id = request.POST.get("time_table_master_id")
        lecture = request.POST.get("lecture")
        subject = request.POST.get("subject")
        day = request.POST.get("day")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        lecture_break = request.POST.get("lecture_break")
        faculty = request.POST.getlist("faculty[]")
        time_table_detail_obj = TimeTableDetail.objects.get(id=time_table_detail_id)
        print("time_table_detail_id", time_table_detail_id)
        print("time_table_master_id", time_table_master_id)
        print("lecture", lecture)
        print("subject", subject)
        print("day", day)
        print("start_time", start_time)
        print("end_time", end_time)
        print("lecture_break", lecture_break)
        # print ("faculty",faculty)
        if lecture_break == "Lecture" and TimeTableDetail.objects.filter(fk_timetable_master_id=time_table_master_id,
                                                                         fk_day_id=day, fk_lecture_id=lecture).exclude(
            id=time_table_detail_id).exists():
            send_msg = {"msg": "Lecture No Already Exists", "status": "0"}
        elif TimeTableDetail.objects.filter(
                Q(fk_timetable_master_id=time_table_master_id, fk_day_id=day, fk_time_start_id=start_time) | Q(
                    fk_timetable_master=time_table_master_id, fk_day_id=day, fk_time_end_id=end_time)).exclude(
            id=time_table_detail_id).exists():
            send_msg = {"msg": "Time Already Used", "status": "0"}
        else:
            if lecture_break == "Break":
                time_table_detail_obj.fk_lecture_id = ""
                time_table_detail_obj.fk_subjects_id = ""
                time_table_detail_obj.fk_faculty_user_info1_id = ""
                time_table_detail_obj.fk_faculty_user_info2_id = ""
            else:
                time_table_detail_obj.fk_lecture_id = lecture
                time_table_detail_obj.fk_subjects_id = subject
                if len(faculty) == 1:
                    print("faculty length 1")
                    if TimeTableDetail.objects.filter(
                            Q(Q(fk_faculty_user_info1_id=faculty[0]) | Q(fk_faculty_user_info2_id=faculty[0]),
                              fk_day_id=day, fk_time_start__id=start_time) | Q(
                                Q(fk_faculty_user_info1_id=faculty[0]) | Q(fk_faculty_user_info2_id=faculty[0]),
                                fk_day_id=day, fk_time_end_id=end_time) | Q(
                                Q(fk_faculty_user_info1_id=faculty[0]) | Q(fk_faculty_user_info2_id=faculty[0]),
                                fk_day_id=day, fk_time_start__id__gte=start_time,
                                fk_time_end_id__lte=end_time)).exclude(
                        id=time_table_detail_id).exists():
                        send_msg = {"msg": "Faculty is Busy", "status": "0"}
                    else:
                        time_table_detail_obj.fk_faculty_user_info1_id = faculty[0]
                        time_table_detail_obj.fk_faculty_user_info2_id = ""
                        time_table_detail_obj.fk_day_id = day
                        time_table_detail_obj.fk_time_start_id = start_time
                        time_table_detail_obj.fk_time_end_id = end_time
                        time_table_detail_obj.lecture_break = lecture_break
                        time_table_detail_obj.save()
                        send_msg = {"msg": "success", "status": "1"}
                if len(faculty) == 2:
                    print("faculty length 2")
                    if TimeTableDetail.objects.filter(Q(
                            Q(fk_faculty_user_info1_id=faculty[0]) | Q(fk_faculty_user_info1_id=faculty[1]) | Q(
                                fk_faculty_user_info2_id=faculty[0]) | Q(fk_faculty_user_info2_id=faculty[1]),
                            fk_day_id=day, fk_time_start_id=start_time) | Q(
                        Q(fk_faculty_user_info1_id=faculty[0]) | Q(fk_faculty_user_info1_id=faculty[1]) | Q(
                            fk_faculty_user_info2_id=faculty[0]) | Q(fk_faculty_user_info2_id=faculty[1]),
                        fk_day_id=day, fk_time_end_id=end_time) | Q(
                        Q(fk_faculty_user_info1_id=faculty[0]) | Q(fk_faculty_user_info1_id=faculty[1]) | Q(
                            fk_faculty_user_info2_id=faculty[0]) | Q(fk_faculty_user_info2_id=faculty[1]),
                        fk_day_id=day, fk_time_start__id__gte=start_time, fk_time_end_id__lte=end_time)).exclude(
                        id=time_table_detail_id).exists():
                        send_msg = {"msg": "Faculty is Busy", "status": "0"}
                    else:
                        time_table_detail_obj.fk_faculty_user_info1_id = faculty[0]
                        time_table_detail_obj.fk_faculty_user_info2_id = faculty[1]
                        time_table_detail_obj.fk_day_id = day
                        time_table_detail_obj.fk_time_start_id = start_time
                        time_table_detail_obj.fk_time_end_id = end_time
                        time_table_detail_obj.lecture_break = lecture_break
                        time_table_detail_obj.save()
                        send_msg = {"msg": "success", "status": "1"}
        return JsonResponse(send_msg)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def delete_time_table_row(request):
    """
    delete time table row
    :param request:
    :return:
    """
    try:
        id = request.POST.get("id")
        time_table_detail_obj = TimeTableDetail.objects.get(id=id)
        time_table_detail_obj.delete()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def faculty_workload(request):
    """
    faculty workload page
    :param request:
    :return:
    """
    try:
        dict_data = {}
        list_data = []
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            time_table_detail_monday_obj = TimeTableDetail.objects.filter(
                Q(fk_faculty_user_info1_id=session, fk_day_id=1) | Q(fk_faculty_user_info2_id=session,
                                                                     fk_day_id=1)).order_by('fk_time_start')
            time_table_detail_tuesday_obj = TimeTableDetail.objects.filter(
                Q(fk_faculty_user_info1_id=session, fk_day_id=2) | Q(fk_faculty_user_info2_id=session,
                                                                     fk_day_id=2)).order_by('fk_time_start')
            time_table_detail_wednesday_obj = TimeTableDetail.objects.filter(
                Q(fk_faculty_user_info1_id=session, fk_day_id=3) | Q(fk_faculty_user_info2_id=session,
                                                                     fk_day_id=3)).order_by('fk_time_start')
            time_table_detail_thursday_obj = TimeTableDetail.objects.filter(
                Q(fk_faculty_user_info1_id=session, fk_day_id=4) | Q(fk_faculty_user_info2_id=session,
                                                                     fk_day_id=4)).order_by('fk_time_start')
            time_table_detail_friday_obj = TimeTableDetail.objects.filter(
                Q(fk_faculty_user_info1_id=session, fk_day_id=5) | Q(fk_faculty_user_info2_id=session,
                                                                     fk_day_id=5)).order_by('fk_time_start')
            time_table_detail_saturday_obj = TimeTableDetail.objects.filter(
                Q(fk_faculty_user_info1_id=session, fk_day_id=6) | Q(fk_faculty_user_info2_id=session,
                                                                     fk_day_id=6)).order_by('fk_time_start')
            if TimeTableDetail.objects.filter(
                    Q(fk_faculty_user_info1_id=session) | Q(fk_faculty_user_info2_id=session)).exists():
                start_time = TimeTableDetail.objects.filter(
                    Q(fk_faculty_user_info1_id=session) | Q(fk_faculty_user_info2_id=session)).order_by(
                    'fk_time_start')[
                    0].fk_time_start.id
                end_time = TimeTableDetail.objects.filter(
                    Q(fk_faculty_user_info1_id=session) | Q(fk_faculty_user_info2_id=session)).order_by('-fk_time_end')[
                    0].fk_time_end.id
            else:
                start_time = 1
                end_time = 1
            time_range_obj = Time.objects.filter(id__range=(start_time, end_time))
            print(start_time, end_time)
            index = 0
            for i in time_range_obj:
                index = index + 1
                if time_range_obj.count() == index:
                    pass
                else:
                    dict_data['next_time'] = time_range_obj[index].time
                    dict_data['time'] = i.time
                    dict_data['id'] = i.id
                    list_data.append(dict_data)
                dict_data = {}
            print(list_data)
            print(time_table_detail_monday_obj)
            return render(request, "faculty_workload.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "time_table_detail_monday_obj": time_table_detail_monday_obj, "list_data": list_data,
                           "time_table_detail_tuesday_obj": time_table_detail_tuesday_obj,
                           "time_table_detail_wednesday_obj": time_table_detail_wednesday_obj,
                           "time_table_detail_thursday_obj": time_table_detail_thursday_obj,
                           "time_table_detail_friday_obj": time_table_detail_friday_obj,
                           "time_table_detail_saturday_obj": time_table_detail_saturday_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def all_time_table(request):
    """
    all time table Page
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        master_list = []
        master_dict = {}
        time_table_master_obj = TimeTableMaster.objects.all()
        time_table_detail_obj = TimeTableDetail.objects.all()
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            for i in time_table_master_obj:
                master_dict['master_id'] = i.id
                if TimeTableDetail.objects.filter(fk_timetable_master_id=i.id).exists():
                    start_time = TimeTableDetail.objects.filter(fk_timetable_master_id=i.id).order_by('fk_time_start')[
                        0].fk_time_start.id
                    end_time = TimeTableDetail.objects.filter(fk_timetable_master_id=i.id).order_by('-fk_time_end')[
                        0].fk_time_end.id
                else:
                    start_time = 1
                    end_time = 1
                print(start_time, end_time)
                time_range_obj = Time.objects.filter(id__range=(start_time, end_time))
                index = 0
                for i in time_range_obj:
                    index = index + 1
                    if time_range_obj.count() == index:
                        pass
                    else:
                        dict_data['next_time'] = time_range_obj[index].time
                        dict_data['time'] = i.time
                        dict_data['id'] = i.id
                        list_data.append(dict_data)
                    dict_data = {}
                master_dict['start_end_time'] = list_data
                list_data = []
                master_list.append(master_dict)
                master_dict = {}
            print("master_list", master_list)
            return render(request, "all_time_table.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "time_table_master_obj": time_table_master_obj,
                           "time_table_detail_obj": time_table_detail_obj,
                           "master_list": master_list})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def all_faculty_workload(request):
    """
    all faculty workload Page
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        master_list = []
        master_dict = {}
        time_table_detail_obj = TimeTableDetail.objects.all()
        user_info_faculty_obj = UserInfo.objects.filter(fk_user_type__user_type="Faculty")
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            for i in user_info_faculty_obj:
                if TimeTableDetail.objects.filter(
                        Q(fk_faculty_user_info1=i.id) | Q(fk_faculty_user_info2=i.id)).exists():
                    master_dict['master_id'] = i.id
                    start_time = \
                        TimeTableDetail.objects.filter(
                            Q(fk_faculty_user_info1=i.id) | Q(fk_faculty_user_info2=i.id)).order_by(
                            'fk_time_start')[0].fk_time_start.id
                    end_time = \
                        TimeTableDetail.objects.filter(
                            Q(fk_faculty_user_info1=i.id) | Q(fk_faculty_user_info2=i.id)).order_by(
                            '-fk_time_end')[0].fk_time_end.id
                    print(start_time, end_time)
                    time_range_obj = Time.objects.filter(id__range=(start_time, end_time))
                    index = 0
                    for i in time_range_obj:
                        index = index + 1
                        if time_range_obj.count() == index:
                            pass
                        else:
                            dict_data['next_time'] = time_range_obj[index].time
                            dict_data['time'] = i.time
                            dict_data['id'] = i.id
                            list_data.append(dict_data)
                        dict_data = {}
                    master_dict['start_end_time'] = list_data
                    list_data = []
                    master_list.append(master_dict)
                    master_dict = {}
            print("master_list", master_list)
            return render(request, "all_faculty_workload.html",
                          {"user_operation_obj": user_operation_obj, "time_table_detail_obj": time_table_detail_obj,
                           "user_info_faculty_obj": user_info_faculty_obj, "master_list": master_list,
                           "user_info_obj": user_info_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')

@csrf_exempt
def delete_time_table(request):
    """
    delete time table Master
    :param request:
    :return:
    """
    try:
        id = request.POST.get("id")
        time_table_master_obj = TimeTableMaster.objects.get(id=id)
        time_table_master_obj.delete()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')
