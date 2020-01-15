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

from authentication.views import error_save

r = lambda: random.randint(0, 255)

from attendance.models import StudentAttendance
from authentication.models import UserInfo, AcademicInfo
from master_forms.models import Subject, UserOperation, Course, Semester, Section


@csrf_exempt
def GetSubjects(request):
    """
        Get Subject list by course,semesters
    :param request:
    :return:
    """
    try:
        course = request.POST.get("course")
        semesters = request.POST.get("semesters")
        if course and semesters:
            subject_list = list(
                Subject.objects.filter(fk_course_id=course, fk_semesters_id=semesters).values_list("id", "subjects"))
        elif course:
            subject_list = list(Subject.objects.filter(fk_course_id=course).values_list("id", "subjects"))
        elif semesters:
            subject_list = list(Subject.objects.filter(fk_semesters_id=semesters).values_list("id", "subjects"))
        else:
            pass
        return HttpResponse(json.dumps(subject_list))
    except:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def date_range(date1, date2):
    """
        Generate list if date fron start and end date
    :param date1:
    :param date2:
    :return:
    """
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(n)


def attendance(request):
    """
        Attendance Page of Student login and Faculty login
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        list_data = []
        dict_data = {}
        all_total_lecture = 0
        present_total_lecture = 0
        base = datetime.datetime.today()
        date_list = [base - datetime.timedelta(days=x) for x in range(30)]
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            if user_info_obj.fk_user_type.user_type == "Student":
                academic_info_obj = AcademicInfo.objects.get(fk_user_info_id=session)
                subjects_obj = Subject.objects.filter(fk_course=academic_info_obj.fk_course,
                                                      fk_semesters=academic_info_obj.fk_semesters)
                for i in subjects_obj:
                    dict_data["present_in_subject"] = StudentAttendance.objects.filter(fk_student_user_info_id=session,
                                                                                       fk_subjects_id=i.id,
                                                                                       attendance_status="P").count()
                    present_total_lecture = present_total_lecture + StudentAttendance.objects.filter(
                        fk_student_user_info_id=session, fk_subjects_id=i.id, attendance_status="P").count()
                    student_attendance_obj = StudentAttendance.objects.filter(fk_subjects_id=i.id)
                    dict_data["total_lectures_subject"] = student_attendance_obj.values("date").distinct().count()
                    all_total_lecture = all_total_lecture + student_attendance_obj.values("date").distinct().count()
                    dict_data["subject_name"] = i.subjects
                    dict_data["subject_id"] = i.id
                    dict_data["student_id"] = session
                    dict_data["compulsory_attendance"] = int(i.compulsory_attendance)
                    if student_attendance_obj.values("date").distinct().count() > 0:
                        dict_data["percentage"] = round(int(
                            StudentAttendance.objects.filter(fk_student_user_info_id=session, fk_subjects_id=i.id,
                                                             attendance_status="P").count()) * 100 / int(
                            student_attendance_obj.values("date").distinct().count()), 2)
                    else:
                        dict_data["percentage"] = 0
                    list_data.append(dict_data)
                    dict_data = {}
                try:
                    total_percentage = round((present_total_lecture * 100 / all_total_lecture), 2)
                except:
                    total_percentage = 0.0
                return render(request, "student_attendance.html",
                              {"subjects_obj": subjects_obj, "list_data": list_data,
                               "total_percentage": total_percentage,
                               "academic_info_obj": academic_info_obj, "user_info_obj": user_info_obj,
                               "to_date": date_list[0], "from_date": date_list[-1]})
            else:
                user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
                course_obj = Course.objects.all()
                semester_obj = Semester.objects.all()
                section_obj = Section.objects.all()
                return render(request, "attendance.html",
                              {"user_operation_obj": user_operation_obj, "course_obj": course_obj,
                               "semester_obj": semester_obj, "section_obj": section_obj, "user_info_obj": user_info_obj,
                               "to_date": date_list[0], "from_date": date_list[-1]})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def filter_attendance(request):
    try:
        session = request.session.get("user_id")
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        list_data = []
        dict_data = {}
        subject_list = []
        subject_dict = {}
        subject_attendance_list = []
        present_student_list = []
        date_list_list = []
        all_subject_list = {}
        chart_subject_list = []
        chart_subject_dict = {}
        course = request.POST.get("course")
        semesters = request.POST.get("semesters")
        sections = request.POST.get("sections")
        subject = request.POST.get("subject")
        academic_info_obj = AcademicInfo.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                                        fk_sections_id=sections)
        chart_from_date = request.POST.get("chart_from_date")
        chart_to_date = request.POST.get("chart_to_date")
        print("chart_from_date", chart_from_date)
        print("chart_to_date", chart_to_date)
        print("course", course)
        print("semesters", semesters)
        print("sections", sections)
        base = datetime.datetime.today()
        if chart_from_date and chart_to_date:
            chart_from_date = datetime.datetime.strptime(chart_from_date, "%d-%m-%Y")
            chart_to_date = datetime.datetime.strptime(chart_to_date, "%d-%m-%Y")
            date_list = [d for d in date_range(chart_from_date, chart_to_date)]
            start_date_range = str(date_list[-1].strftime("%Y-%m-%d"))
            end_date_range = str(date_list[0].strftime("%Y-%m-%d"))
        else:
            date_list = [base - datetime.timedelta(days=x) for x in range(30)]
            start_date_range = str(date_list[0].strftime("%Y-%m-%d"))
            end_date_range = str(date_list[-1].strftime("%Y-%m-%d"))
        print(date_list)
        print("academic_info_obj", academic_info_obj)
        subjects_obj = Subject.objects.filter(fk_course_id=course, fk_semesters_id=semesters)
        for s in subjects_obj:
            date_list_list = []
            for i in reversed(date_list):
                date_list_list.append(str(i.date().strftime("%d-%m-%Y")))
                chart_subject_dict["label"] = str(s.subjects)
                chart_subject_dict["fill"] = "false"
                chart_subject_dict["borderColor"] = ("#%02X%02X%02X" % (r(), r(), r()))
                chart_subject_dict["lineTension"] = 0.4
                student_attendance_obj = StudentAttendance.objects.filter(fk_course_id=course,
                                                                          fk_semesters_id=semesters,
                                                                          fk_sections_id=sections, fk_subjects_id=s.id,
                                                                          date=i)
                distinct_date_obj = student_attendance_obj.values("date").distinct()
                if distinct_date_obj:
                    subject_attendance_list.append(
                        StudentAttendance.objects.filter(date=i, fk_subjects_id=s.id, attendance_status="P").count())
                    print(subject_attendance_list)
                else:
                    subject_attendance_list.append(0)
                chart_subject_dict["data"] = subject_attendance_list
            subject_attendance_list = []
            chart_subject_list.append(chart_subject_dict)
            chart_subject_dict = {}
        all_subject_list = {"labels": date_list_list, "datasets": chart_subject_list}

        a = 0
        attendance_count = 0
        for k in range(len(all_subject_list["labels"])):
            for i in range(len(all_subject_list["datasets"])):
                if all_subject_list["datasets"][i]["data"][k] > 0:
                    attendance_count = attendance_count + 1
                    a = a + all_subject_list["datasets"][i]["data"][k]
            try:
                present_student_list.append(round((a / (academic_info_obj.count() * attendance_count)) * 100, 2))
            except:
                present_student_list.append(0.0)
            a = 0
            attendance_count = 0

        print("start_date_range", start_date_range)
        print("end_date_range", end_date_range)
        print("end_date_range", type(end_date_range))
        chart_percentage_data = {"labels": date_list_list, "datasets": [
            {"label": "Percentage", "data": present_student_list, "fill": "false", "borderColor": "rgb(0, 200, 0, 1)",
             "lineTension": 0.4}]}
        student_attendance_obj = StudentAttendance.objects.filter(
            date__range=[str(end_date_range), str(start_date_range)])
        print("student_attendance_obj", student_attendance_obj)
        if subject == "All":
            student_attendance_obj = StudentAttendance.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                                                      fk_sections_id=sections,
                                                                      date__range=[str(end_date_range),
                                                                                   str(start_date_range)]).order_by(
                "-date")
            distinct_date_obj = student_attendance_obj.values("date").distinct()
            for i in distinct_date_obj:
                dict_data["date"] = i["date"]
                distinct_subject_obj = StudentAttendance.objects.filter(date=i["date"]).values("fk_subjects",
                                                                                               "fk_subjects__subjects").distinct()
                for j in distinct_subject_obj:
                    subject_dict["subject_id"] = j["fk_subjects"]
                    subject_dict["subject_name"] = j["fk_subjects__subjects"]
                    subject_dict["subject_attendance_count"] = StudentAttendance.objects.filter(date=i["date"],
                                                                                                fk_subjects_id=j[
                                                                                                    "fk_subjects"],
                                                                                                attendance_status="P").count()
                    subject_list.append(subject_dict)
                    subject_dict = {}
                dict_data["subject_attendance_count"] = subject_list
                subject_list = []
                list_data.append(dict_data)
                dict_data = {}
        else:
            student_attendance_obj = StudentAttendance.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                                                      fk_sections_id=sections, fk_subjects_id=subject,
                                                                      date__range=[str(end_date_range),
                                                                                   str(start_date_range)]).order_by(
                "-date")
            distinct_date_obj = student_attendance_obj.values("date", "fk_subjects", "fk_subjects__subjects").distinct()
            for i in distinct_date_obj:
                dict_data["date"] = i["date"]
                distinct_subject_obj = StudentAttendance.objects.filter(date=i["date"], fk_subjects_id=subject).values(
                    "fk_subjects", "fk_subjects__subjects").distinct()
                for j in distinct_subject_obj:
                    subject_dict["subject_id"] = j["fk_subjects"]
                    subject_dict["subject_name"] = j["fk_subjects__subjects"]
                    subject_dict["subject_attendance_count"] = str(
                        StudentAttendance.objects.filter(date=i["date"], fk_subjects_id=subject,
                                                         attendance_status="P").count())
                    subject_list.append(subject_dict)
                    subject_dict = {}
                dict_data["subject_attendance_count"] = subject_list
                subject_list = []
                list_data.append(dict_data)
                dict_data = {}
        render_string = render_to_string("attendance_filter.html",
                                         {"user_operation_obj": user_operation_obj, "list_data": list_data,
                                          "distinct_date_obj": distinct_date_obj,
                                          "academic_info_obj": academic_info_obj,
                                          "subjects_obj": subjects_obj,
                                          "all_subject_list": json.dumps(all_subject_list),
                                          "chart_percentage_data": json.dumps(chart_percentage_data),
                                          "total_student": academic_info_obj.count(),
                                          "to_date": date_list[0], "from_date": date_list[-1]})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_attendance_detail(request):
    """
    Add Attendance Page
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        course = request.POST.get("course")
        semesters = request.POST.get("semesters")
        sections = request.POST.get("sections")
        print("session", session)
        print("course", course)
        print("semesters", semesters)
        print("sections", sections)
        academic_info_obj = AcademicInfo.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                                        fk_sections_id=sections)
        if academic_info_obj:
            render_string = render_to_string("add_attendance_div.html", {"academic_info_obj": academic_info_obj})
        else:
            render_string = "error"
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def save_attendance_detail(request):
    """
    Save attendance Detail
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        course = request.POST.get("course")
        semesters = request.POST.get("semesters")
        sections = request.POST.get("sections")
        subject = request.POST.get("subject")
        attendance_date = datetime.datetime.strptime(str(request.POST.get("attendance_date")), "%d-%m-%Y").strftime(
            "%Y-%m-%d")
        absent_student_list = request.POST.getlist("absent_student_list[]")
        present_student_list = request.POST.getlist("present_student_list[]")
        if StudentAttendance.objects.filter(fk_course_id=course, fk_semesters_id=semesters, fk_sections_id=sections,
                                            fk_subjects_id=subject, date=attendance_date).exists():
            return HttpResponse("already save")
        else:
            for i in absent_student_list:
                student_attendance_obj = StudentAttendance(fk_student_user_info_id=i, fk_faculty_user_info_id=session,
                                                           fk_course_id=course, fk_semesters_id=semesters,
                                                           fk_sections_id=sections, fk_subjects_id=subject,
                                                           date=attendance_date, attendance_status="A")
                student_attendance_obj.save()
            for i in present_student_list:
                student_attendance_obj = StudentAttendance(fk_student_user_info_id=i, fk_faculty_user_info_id=session,
                                                           fk_course_id=course, fk_semesters_id=semesters,
                                                           fk_sections_id=sections, fk_subjects_id=subject,
                                                           date=attendance_date, attendance_status="P")
                student_attendance_obj.save()
            return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def filter_attendance_detail(request):
    """
        Filter Attendance Detail
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        course = request.POST.get("course")
        semesters = request.POST.get("semesters")
        sections = request.POST.get("sections")
        subject = request.POST.get("subject")
        attendance_date = request.POST.get("attendance_date")
        print("session", session)
        print("course", course)
        print("semesters", semesters)
        print("sections", sections)
        print("subject", subject)
        print("attendance_date", attendance_date)
        user_info_obj = UserInfo.objects.get(id=session)
        student_attendance_obj = StudentAttendance.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                                                  fk_sections_id=sections, fk_subjects_id=subject,
                                                                  date=attendance_date)
        student_attendance_obj_list = list(student_attendance_obj.values_list("fk_student_user_info", flat=True))
        if student_attendance_obj:
            academic_info_date_wise_obj = AcademicInfo.objects.filter(fk_user_info__in=student_attendance_obj_list)
            print(academic_info_date_wise_obj)
            render_string = render_to_string("subject_attendance.html",
                                             {"academic_info_date_wise_obj": academic_info_date_wise_obj,
                                              "student_attendance_obj": student_attendance_obj,
                                              "user_info_obj": user_info_obj})
        else:
            render_string = "error"
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def filter_attendance_detail(request):
    """
        Filter Attendance Detail
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        course = request.POST.get("course")
        semesters = request.POST.get("semesters")
        sections = request.POST.get("sections")
        subject = request.POST.get("subject")
        attendance_date = request.POST.get("attendance_date")
        print("session", session)
        print("course", course)
        print("semesters", semesters)
        print("sections", sections)
        print("subject", subject)
        print("attendance_date", attendance_date)
        user_info_obj = UserInfo.objects.get(id=session)
        student_attendance_obj = StudentAttendance.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                                                  fk_sections_id=sections, fk_subjects_id=subject,
                                                                  date=attendance_date)
        student_attendance_obj_list = list(student_attendance_obj.values_list("fk_student_user_info", flat=True))
        if student_attendance_obj:
            academic_info_date_wise_obj = AcademicInfo.objects.filter(fk_user_info__in=student_attendance_obj_list)
            print(academic_info_date_wise_obj)
            render_string = render_to_string("subject_attendance.html",
                                             {"academic_info_date_wise_obj": academic_info_date_wise_obj,
                                              "student_attendance_obj": student_attendance_obj,
                                              "user_info_obj": user_info_obj})
        else:
            render_string = "error"
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_attendance_detail(request):
    """
    Update Attendance Detail
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        course = request.POST.get("course")
        semesters = request.POST.get("semesters")
        sections = request.POST.get("sections")
        subject = request.POST.get("subject")
        attendance_date = request.POST.get("attendance_date")
        absent_student_list = request.POST.getlist("absent_student_list[]")
        present_student_list = request.POST.getlist("present_student_list[]")
        print("session", session)
        print("course", course)
        print("semesters", semesters)
        print("sections", sections)
        print("subject", subject)
        print(absent_student_list)
        print(present_student_list)
        for i in absent_student_list:
            student_attendance_obj = StudentAttendance.objects.get(fk_student_user_info_id=i, fk_course_id=course,
                                                                   fk_semesters_id=semesters, fk_sections_id=sections,
                                                                   fk_subjects_id=subject, date=attendance_date)
            student_attendance_obj.attendance_status = "A"
            student_attendance_obj.fk_faculty_user_info_id = session
            student_attendance_obj.save()
        for i in present_student_list:
            student_attendance_obj = StudentAttendance.objects.get(fk_student_user_info_id=i, fk_course_id=course,
                                                                   fk_semesters_id=semesters, fk_sections_id=sections,
                                                                   fk_subjects_id=subject, date=attendance_date)
            student_attendance_obj.attendance_status = "P"
            student_attendance_obj.fk_faculty_user_info_id = session
            student_attendance_obj.save()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def single_student_attendance_detail(request):
    """
    Single student attendance detail
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        id = request.POST.get("id")
        user_info_obj = UserInfo.objects.get(id=session)
        list_data = []
        dict_data = {}
        all_total_lecture = 0
        present_total_lecture = 0
        academic_info_obj = AcademicInfo.objects.get(fk_user_info_id=id)
        subjects_obj = Subject.objects.filter(fk_course=academic_info_obj.fk_course,
                                              fk_semesters=academic_info_obj.fk_semesters)
        for i in subjects_obj:
            dict_data["present_in_subject"] = StudentAttendance.objects.filter(fk_student_user_info_id=id,
                                                                               fk_subjects_id=i.id,
                                                                               attendance_status="P").count()
            present_total_lecture = present_total_lecture + StudentAttendance.objects.filter(fk_student_user_info_id=id,
                                                                                             fk_subjects_id=i.id,
                                                                                             attendance_status="P").count()
            student_attendance_obj = StudentAttendance.objects.filter(fk_subjects_id=i.id)
            dict_data["total_lectures_subject"] = student_attendance_obj.values("date").distinct().count()
            all_total_lecture = all_total_lecture + student_attendance_obj.values("date").distinct().count()
            dict_data["subject_name"] = i.subjects
            dict_data["subject_id"] = i.id
            dict_data["student_id"] = id
            dict_data["compulsory_attendance"] = int(i.compulsory_attendance)
            if student_attendance_obj.values("date").distinct().cou.nt() > 0:
                print(student_attendance_obj.values("date").distinct().count())
                dict_data["percentage"] = round(int(
                    StudentAttendance.objects.filter(fk_student_user_info_id=id, fk_subjects_id=i.id,
                                                     attendance_status="P").count()) * 100 / int(
                    student_attendance_obj.values("date").distinct().count()), 2)
            else:
                dict_data["percentage"] = 0
            list_data.append(dict_data)
            dict_data = {}
        if present_total_lecture == 0:
            total_percentage = 0
        else:
            total_percentage = round((present_total_lecture * 100 / all_total_lecture), 2)
        print(list_data)
        render_string = render_to_string("student_attendance_detail.html",
                                         {"subjects_obj": subjects_obj, "list_data": list_data,
                                          "total_percentage": total_percentage,
                                          "academic_info_obj": academic_info_obj, "user_info_obj": user_info_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def get_subject_attendance_detail(request):
    """
    get subject attendance detail
    :param request:
    :return:
    """
    try:
        subject_id = request.POST.get("subject_id")
        student_id = request.POST.get("student_id")
        student_attendance_obj = StudentAttendance.objects.filter(fk_student_user_info_id=student_id,
                                                                  fk_subjects_id=subject_id)
        subjects_obj = Subject.objects.get(id=subject_id)
        render_string = render_to_string("student_subject_attendance.html",
                                         {"student_attendance_obj": student_attendance_obj,
                                          "subjects_obj": subjects_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


"""
FilterChartAttendance is not in used now i i this function for filter attendance chart but after discussion we deside to
filter it on only main filter 
"""

# @csrf_exempt
# def FilterChartAttendance(request):
#     list_data = []
#     dict_data = {}
#     subject_list_data = []
#     subject_dict = {}
#     subject_attendance_list_data = []
#     present_student_list_data = []
#     date_list_data = []
#     chart_subject_list_data = []
#     chart_subject_dict = {}
#     course = request.POST.get("course")
#     semesters = request.POST.get("semesters")
#     sections = request.POST.get("sections")
#     chartsubject = request.POST.get("chartsubject")
#     chart_from_date = request.POST.get("chart_from_date")
#     chart_to_date = request.POST.get("chart_to_date")
#     subject = request.POST.get("subject")
#     chart_from_date = datetime.datetime.strptime(chart_from_date, "%d-%m-%Y")
#     chart_to_date = datetime.datetime.strptime(chart_to_date, "%d-%m-%Y")
#     print ("course", course)
#     print ("semesters", semesters)
#     print ("sections", sections)
#     print ("chartsubject", chartsubject)
#     print ("chart_from_date", chart_from_date)
#     print ("chart_to_date", chart_to_date)
#     academic_info_obj = AcademicInfo.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
#                                                    fk_sections_id=sections)
#     subjects_obj = Subject.objects.filter(fk_course_id=course, fk_semesters_id=semesters)
#     date_list_data = [d for d in date_range(chart_from_date, chart_to_date)]
#     for s in subjects_obj:
#         date_list_data = []
#         for i in date_list_data:
#             date_list_data.append(str(i.date().strftime("%m-%d")))
#             chart_subject_dict["label"] = str(s.subjects)
#             chart_subject_dict["fill"] = "false"
#             chart_subject_dict["borderColor"] = ("#%02X%02X%02X" % (r(), r(), r()))
#             chart_subject_dict["lineTension"] = 0.4
#             student_attendance_obj = StudentAttendance.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
#                                                                      fk_sections_id=sections, fk_subjects_id=s.id,
#                                                                      date=i)
#             distinct_date_obj = student_attendance_obj.values("date").distinct()
#             if distinct_date_obj:
#                 subject_attendance_list_data.append(
#                     StudentAttendance.objects.filter(date=i, fk_subjects_id=s.id, attendance_status="P").count())
#                 print (subject_attendance_list_data)
#             else:
#                 subject_attendance_list_data.append(0)
#             chart_subject_dict["data"] = subject_attendance_list_data
#         subject_attendance_list_data = []
#         chart_subject_list_data.append(chart_subject_dict)
#         chart_subject_dict = {}
#     all_subject_list_data = {"labels": date_list_data, "datasets": chart_subject_list_data}
#     print ("all_subject_list_data", all_subject_list_data)
#
#     a = 0
#     attendance_count = 0
#     for k in range(len(all_subject_list_data["labels"])):
#         for i in range(len(all_subject_list_data["datasets"])):
#             if all_subject_list_data["datasets"][i]["data"][k] > 0:
#                 attendance_count = attendance_count + 1
#                 a = a + all_subject_list_data["datasets"][i]["data"][k]
#         if a > 0:
#             present_student_list_data.append(round((a / (academic_info_obj.count() * attendance_count)) * 100, 2))
#         else:
#             present_student_list_data.append(0.0)
#         a = 0
#         attendance_count = 0
#
#     chart_percentage_data = {"labels": date_list_data, "datasets": [
#         {"label": "Percentage", "data": present_student_list_data, "fill": "false", "borderColor": "rgb(0, 200, 0, 1)",
#          "lineTension": 0.4}]}
#
#     if subject == "All":
#         student_attendance_obj = StudentAttendance.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
#                                                                  fk_sections_id=sections,
#                                                                  date__range=[chart_from_date, chart_to_date]).order_by(
#             "-date")
#         distinct_date_obj = student_attendance_obj.values("date").distinct()
#         for i in distinct_date_obj:
#             dict_data["date"] = i["date"]
#             distinct_subject_obj = StudentAttendance.objects.filter(date=i["date"]).values("fk_subjects",
#                                                                                           "fk_subjects__subjects").distinct()
#             for j in distinct_subject_obj:
#                 subject_dict["subject_id"] = j["fk_subjects"]
#                 subject_dict["subject_name"] = j["fk_subjects__subjects"]
#                 subject_dict["subject_attendance_count"] = StudentAttendance.objects.filter(date=i["date"],
#                                                                                          fk_subjects_id=j[
#                                                                                              "fk_subjects"],
#                                                                                          attendance_status="P").count()
#                 subject_list_data.append(subject_dict)
#                 subject_dict = {}
#             dict_data["subject_attendance_count"] = subject_list_data
#             subject_list_data = []
#             list_data.append(dict_data)
#             dict_data = {}
#     else:
#         student_attendance_obj = StudentAttendance.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
#                                                                  fk_sections_id=sections, fk_subjects_id=subject,
#                                                                  date__range=[chart_from_date, chart_to_date]).order_by(
#             "-date")
#         distinct_date_obj = student_attendance_obj.values("date", "fk_subjects", "fk_subjects__subjects").distinct()
#         for i in distinct_date_obj:
#             dict_data["date"] = i["date"]
#             distinct_subject_obj = StudentAttendance.objects.filter(date=i["date"], fk_subjects_id=subject).values(
#                 "fk_subjects", "fk_subjects__subjects").distinct()
#             for j in distinct_subject_obj:
#                 subject_dict["subject_id"] = j["fk_subjects"]
#                 subject_dict["subject_name"] = j["fk_subjects__subjects"]
#                 subject_dict["subject_attendance_count"] = str(
#                     StudentAttendance.objects.filter(date=i["date"], fk_subjects_id=subject,
#                                                      attendance_status="P").count())
#                 subject_list_data.append(subject_dict)
#                 subject_dict = {}
#             dict_data["subject_attendance_count"] = subject_list_data_data
#             subject_list_data_data = []
#             list_data_data.append(dict_data)
#             dict_data = {}
#     render_string = render_to_string("chart_filter.html", {"list_data_data": list_data, "distinct_date_obj": distinct_date_obj,
#                                                            "academic_info_obj": academic_info_obj,
#                                                            "subjects_obj": subjects_obj,
#                                                            "all_subject_list_data": json.dumps(all_subject_list_data),
#                                                            "chart_percentage_data": json.dumps(chart_percentage_data),
#                                                            "total_student": academic_info_obj.count(),
#                                                            "to_date": date_list_data[0], "from_date": date_list_data[-1]})
#     return HttpResponse(render_string)
