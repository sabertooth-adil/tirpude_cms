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
r = lambda: random.randint(0, 255)


from attendance.models import StudentAttendance
from authentication.models import UserInfo, AcademicInfo
from master_forms.models import Subject, UserOperation, Course, Semester, Section

@csrf_exempt
def GetSubjects(request):
    course = request.POST.get("course")
    semesters = request.POST.get("semesters")
    if course and semesters:
        subject_list = list(
            Subject.objects.filter(fk_course_id=course, fk_semesters_id=semesters).values_list('id', 'subjects'))
    elif course:
        subject_list = list(Subject.objects.filter(fk_course_id=course).values_list('id', 'subjects'))
    elif semesters:
        subject_list = list(Subject.objects.filter(fk_semesters_id=semesters).values_list('id', 'subjects'))
    else:
        pass
    return HttpResponse(json.dumps(subject_list))

def daterange(date1, date2):
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(n)

def Attendance(request):
    session = request.session.get('user_id')
    list = []
    dict = {}
    alltotallectures = 0
    presenttotallectures = 0
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(30)]
    if session:
        user_info_obj = UserInfo.objects.get(id=session)
        if user_info_obj.fk_user_type.user_type == "Student":
            academic_info_obj = AcademicInfo.objects.get(fk_user_info_id=session)
            subjects_obj = Subject.objects.filter(fk_course=academic_info_obj.fk_course,
                                                  fk_semesters=academic_info_obj.fk_semesters)
            for i in subjects_obj:
                dict['presentinsubject'] = StudentAttendance.objects.filter(fk_student_user_info_id=session,
                                                                            fk_subjects_id=i.id,
                                                                            attendance_status="P").count()
                presenttotallectures = presenttotallectures + StudentAttendance.objects.filter(
                    fk_student_user_info_id=session, fk_subjects_id=i.id, attendance_status="P").count()
                studentattendance_obj = StudentAttendance.objects.filter(fk_subjects_id=i.id)
                dict['totallecturessubject'] = studentattendance_obj.values('date').distinct().count()
                alltotallectures = alltotallectures + studentattendance_obj.values('date').distinct().count()
                dict['subjectname'] = i.subjects
                dict['subject_id'] = i.id
                dict['student_id'] = session
                dict['compulsory_attendance'] = int(i.compulsory_attendance)
                if studentattendance_obj.values('date').distinct().count() > 0:
                    dict['percentage'] = round(int(
                        StudentAttendance.objects.filter(fk_student_user_info_id=session, fk_subjects_id=i.id,
                                                         attendance_status="P").count()) * 100 / int(
                        studentattendance_obj.values('date').distinct().count()), 2)
                else:
                    dict['percentage'] = 0
                list.append(dict)
                dict = {}
            try:
                totalpercentage = round((presenttotallectures * 100 / alltotallectures), 2)
            except:
                totalpercentage = 0.0
            return render(request, "student_attendance.html",
                          {"subjects_obj": subjects_obj, "list": list, "totalpercentage": totalpercentage,
                           "academic_info_obj": academic_info_obj, "user_info_obj": user_info_obj, "to_date": date_list[0],
                           "from_date": date_list[-1]})
        else:
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            course_obj = Course.objects.all()
            semesters_obj = Semester.objects.all()
            section_obj = Section.objects.all()
            return render(request, "attendance.html",
                          {"user_operation_obj": user_operation_obj, "course_obj": course_obj,
                           "semesters_obj": semesters_obj, "section_obj": section_obj, "user_info_obj": user_info_obj,
                           "to_date": date_list[0], "from_date": date_list[-1]})
    else:
        return redirect("/")


@csrf_exempt
def FilterAttendance(request):
    session = request.session.get('user_id')
    user_info_obj = UserInfo.objects.get(id=session)
    user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
    list = []
    dict = {}
    subjectlist = []
    subjectdict = {}
    subjectattendancelist = []
    presentstudentlist = []
    datelist = []
    AllSubjectList = {}
    ChartSubjectList = []
    ChartSubjectDict = {}
    course = request.POST.get("course")
    semesters = request.POST.get("semesters")
    sections = request.POST.get("sections")
    subject = request.POST.get("subject")
    academic_info_obj = AcademicInfo.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                                   fk_sections_id=sections)
    chartfromdate = request.POST.get("chartfromdate")
    charttodate = request.POST.get("charttodate")
    print ("chartfromdate", chartfromdate)
    print ("charttodate", charttodate)
    print ("course", course)
    print ("semesters", semesters)
    print ("sections", sections)
    base = datetime.datetime.today()
    if chartfromdate and charttodate:
        chartfromdate = datetime.datetime.strptime(chartfromdate, '%d-%m-%Y')
        charttodate = datetime.datetime.strptime(charttodate, '%d-%m-%Y')
        date_list = [d for d in daterange(chartfromdate, charttodate)]
        startdate_range = str(date_list[-1].strftime('%Y-%m-%d'))
        enddate_range = str(date_list[0].strftime('%Y-%m-%d'))
    else:
        date_list = [base - datetime.timedelta(days=x) for x in range(30)]
        startdate_range = str(date_list[0].strftime('%Y-%m-%d'))
        enddate_range = str(date_list[-1].strftime('%Y-%m-%d'))
    print (date_list)
    print ("academic_info_obj", academic_info_obj)
    subjects_obj = Subject.objects.filter(fk_course_id=course, fk_semesters_id=semesters)
    for s in subjects_obj:
        datelist = []
        for i in reversed(date_list):
            datelist.append(str(i.date().strftime("%d-%m-%Y")))
            ChartSubjectDict['label'] = str(s.subjects)
            ChartSubjectDict['fill'] = "false"
            ChartSubjectDict['borderColor'] = ('#%02X%02X%02X' % (r(), r(), r()))
            ChartSubjectDict['lineTension'] = 0.4
            studentattendance_obj = StudentAttendance.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                                                     fk_sections_id=sections, fk_subjects_id=s.id,
                                                                     date=i)
            distinctdate_obj = studentattendance_obj.values('date').distinct()
            if distinctdate_obj:
                subjectattendancelist.append(
                    StudentAttendance.objects.filter(date=i, fk_subjects_id=s.id, attendance_status="P").count())
                print (subjectattendancelist)
            else:
                subjectattendancelist.append(0)
            ChartSubjectDict['data'] = subjectattendancelist
        subjectattendancelist = []
        ChartSubjectList.append(ChartSubjectDict)
        ChartSubjectDict = {}
    AllSubjectList = {"labels": datelist, "datasets": ChartSubjectList}

    a = 0
    attcount = 0
    for k in range(len(AllSubjectList['labels'])):
        for i in range(len(AllSubjectList['datasets'])):
            if AllSubjectList['datasets'][i]['data'][k] > 0:
                attcount = attcount + 1
                a = a + AllSubjectList['datasets'][i]['data'][k]
        try:
            presentstudentlist.append(round((a / (academic_info_obj.count() * attcount)) * 100, 2))
        except:
            presentstudentlist.append(0.0)
        a = 0
        attcount = 0

    print ("startdate_range", startdate_range)
    print ("enddate_range", enddate_range)
    print ("enddate_range", type(enddate_range))
    ChartPercentageData = {"labels": datelist, "datasets": [
        {"label": "Percentage", "data": presentstudentlist, "fill": "false", "borderColor": "rgb(0, 200, 0, 1)",
         "lineTension": 0.4}]}
    studentattendance_obj = StudentAttendance.objects.filter(date__range=[str(enddate_range), str(startdate_range)])
    print ("studentattendance_obj", studentattendance_obj)
    if subject == "All":
        studentattendance_obj = StudentAttendance.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                                                 fk_sections_id=sections,
                                                                 date__range=[str(enddate_range),
                                                                              str(startdate_range)]).order_by('-date')
        distinctdate_obj = studentattendance_obj.values('date').distinct()
        for i in distinctdate_obj:
            dict['date'] = i['date']
            distinctsubject_obj = StudentAttendance.objects.filter(date=i['date']).values('fk_subjects',
                                                                                          'fk_subjects__subjects').distinct()
            for j in distinctsubject_obj:
                subjectdict['subject_id'] = j['fk_subjects']
                subjectdict['subject_name'] = j['fk_subjects__subjects']
                subjectdict['subjectattendanc_count'] = StudentAttendance.objects.filter(date=i['date'],
                                                                                         fk_subjects_id=j[
                                                                                             'fk_subjects'],
                                                                                         attendance_status="P").count()
                subjectlist.append(subjectdict)
                subjectdict = {}
            dict['subjectattendanc_count'] = subjectlist
            subjectlist = []
            list.append(dict)
            dict = {}
    else:
        studentattendance_obj = StudentAttendance.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                                                 fk_sections_id=sections, fk_subjects_id=subject,
                                                                 date__range=[str(enddate_range),
                                                                              str(startdate_range)]).order_by('-date')
        distinctdate_obj = studentattendance_obj.values('date', 'fk_subjects', 'fk_subjects__subjects').distinct()
        for i in distinctdate_obj:
            dict['date'] = i['date']
            distinctsubject_obj = StudentAttendance.objects.filter(date=i['date'], fk_subjects_id=subject).values(
                'fk_subjects', 'fk_subjects__subjects').distinct()
            for j in distinctsubject_obj:
                subjectdict['subject_id'] = j['fk_subjects']
                subjectdict['subject_name'] = j['fk_subjects__subjects']
                subjectdict['subjectattendanc_count'] = str(
                    StudentAttendance.objects.filter(date=i['date'], fk_subjects_id=subject,
                                                     attendance_status="P").count())
                subjectlist.append(subjectdict)
                subjectdict = {}
            dict['subjectattendanc_count'] = subjectlist
            subjectlist = []
            list.append(dict)
            dict = {}
    render_string = render_to_string("attendance_filter.html", {"user_operation_obj": user_operation_obj, "list": list,
                                                                "distinctdate_obj": distinctdate_obj,
                                                                "academic_info_obj": academic_info_obj,
                                                                "subjects_obj": subjects_obj,
                                                                "AllSubjectList": json.dumps(AllSubjectList),
                                                                "ChartPercentageData": json.dumps(ChartPercentageData),
                                                                "totalstudent": academic_info_obj.count(),
                                                                "to_date": date_list[0], "from_date": date_list[-1]})
    return HttpResponse(render_string)

@csrf_exempt
def AddAttendanceDetail(request):
    session = request.session.get('user_id')
    course = request.POST.get("course")
    semesters = request.POST.get("semesters")
    sections = request.POST.get("sections")
    print ("session", session)
    print ("course", course)
    print ("semesters", semesters)
    print ("sections", sections)
    academic_info_obj = AcademicInfo.objects.filter(fk_course_id=course, fk_semesters_id=semesters,
                                                   fk_sections_id=sections)
    if academic_info_obj:
        render_string = render_to_string("add_attendance_div.html", {"academic_info_obj": academic_info_obj})
    else:
        render_string = "error"
    return HttpResponse(render_string)