from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import datetime
import traceback
from django.template.loader import render_to_string
from authentication.models import UserInfo, AcademicInfo
from master_forms.models import Course
from leave_application.models import LeaveApplication, LeaveReason


def handler404(request, exception):
    return render(request, "404.html")


def handler400(request, exception):
    return render(request, "400.html")


def error_handler_500(request):
    return render(request, "500.html")


def error_save(error):
    time = str(datetime.datetime.now())
    with open("error_log.txt", "a") as myfile:
        myfile.write(time + "\n")
        myfile.write(error + "\n\n")
    print(error)
    return error


# leave application function for students and faculty
@csrf_exempt
def leave_application(request):
    """
       Directs user to leave application page
    """
    try:
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            print("user_info_obj", user_info_obj)
            reason_obj = LeaveReason.objects.all()
            course_obj = Course.objects.all()
            faculty_obj = UserInfo.objects.filter(fk_user_type__user_type="Faculty")
            if user_info_obj.fk_user_type.user_type == "Student":
                user_info_obj = UserInfo.objects.get(id=session)
                leave_application_obj = LeaveApplication.objects.filter(fk_user_info_id=session)
                return render(request, "leave_application.html", {"user_info_obj": user_info_obj,
                                                                  "reason_obj": reason_obj,
                                                                  "leave_application_obj": leave_application_obj,
                                                                  "faculty_obj": faculty_obj,
                                                                  "course_obj": course_obj})
            else:
                leave_application_obj = LeaveApplication.objects.all()
                user_info_obj = UserInfo.objects.get(id=session)
                academic_info_obj = AcademicInfo.objects.all()
                course_obj = Course.objects.all()
                return render(request, "faculty_leave_application.html", {"user_info_obj": user_info_obj,
                                                                          "leave_application_obj": leave_application_obj,
                                                                          "academic_info_obj": academic_info_obj,
                                                                          "course_obj": course_obj,
                                                                          "faculty_obj": faculty_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


# save leave application
@csrf_exempt
def leave_application_submit(request):
    """
    saves student application
    """
    try:
        session = request.session.get("user_id")
        start = datetime.datetime.strptime(str(request.POST.get("start")), '%d-%m-%Y').strftime('%Y-%m-%d')
        end = datetime.datetime.strptime(str(request.POST.get("end")), '%d-%m-%Y').strftime('%Y-%m-%d')
        reason = request.POST.get("reason")
        faculty = request.POST.get("faculty")
        status = "Pending"
        date_today = datetime.date.today()
        reason_detail = request.POST.get("reason_detail")
        file = request.FILES.get("file")
        academic_info_obj = AcademicInfo.objects.get(fk_user_info_id=session)
        semester = academic_info_obj.fk_semesters.id
        sections = academic_info_obj.fk_sections.id
        course = academic_info_obj.fk_course.id
        print(semester)
        print(sections)
        print(course)
        leave_application_obj = LeaveApplication(fk_leave_reason_id=reason, fk_user_info_id=session,
                                                 fk_faculty_user_id=faculty, fk_course_id=course,
                                                 fk_semesters_id=semester, fk_sections_id=sections,
                                                 start_date=start, end_date=end, date_post=date_today,
                                                 status=status, reason=reason_detail, file=file)
        leave_application_obj.save()
        return redirect('/leave-application/')
    except :
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


# approves or disapproves leave applications
@csrf_exempt
def approve_disapprove_application(request):
    """
       changes leave application status
    """
    try:
        id = request.POST.get("id")
        action_status = request.POST.get("action_status")
        print(action_status)
        leave_application_obj = LeaveApplication.objects.get(id=id)
        if action_status == "Approved":
            leave_application_obj.action_status = "Disapproved"
        else:
            leave_application_obj.action_status = "Approved"
        leave_application_obj.save()
        print(id)
        return HttpResponse("success")
    except :
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


# gives detailed information about leave application
@csrf_exempt
def view_leave_application_detail(request):
    """
    shows student's leave application details to faculty
    """
    try:
        dict = {}
        id = request.POST.get("id")
        leave_application_obj = LeaveApplication.objects.get(id=id)
        leave_application_obj.status = "Read"
        leave_application_obj.save()
        academic_info_obj = AcademicInfo.objects.get(fk_user_info=leave_application_obj.fk_user_info)
        user_info_obj = UserInfo.objects.get(id=leave_application_obj.fk_user_info.id)
        dict['student_name'] = user_info_obj.first_name+" "+user_info_obj.last_name
        dict['semester'] = academic_info_obj.fk_semesters.semester
        dict['sections'] = academic_info_obj.fk_sections.sections
        dict['course'] = academic_info_obj.fk_course.course
        dict['leave_reason'] = leave_application_obj.fk_leave_reason.reason_to_leave
        dict['reason'] = leave_application_obj.reason
        dict['start_date'] = leave_application_obj.start_date.strftime('%d-%m-%Y')
        dict['end_date'] = leave_application_obj.end_date.strftime('%d-%m-%Y')
        dict['date_post'] = leave_application_obj.date_post.strftime('%d-%m-%Y')
        return JsonResponse(dict)
    except :
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


# shows leave application details to student
@csrf_exempt
def get_leave_application_detail(request):
    """
    shows detail about leave application to student
    """
    try:
        leave_application_list_id = request.POST.get("leave_application_list_id")
        leave_application_obj = LeaveApplication.objects.get(id=leave_application_list_id)
        return JsonResponse({"detail": leave_application_obj.reason, "status": leave_application_obj.status})
    except :
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


# filters leave application according to specific criteria
@csrf_exempt
def filter_leave_applications(request):
    """
    Returns leave applications according to selected criteria
    """
    try:
        start_date_filter = request.POST.get("start_date_filter")
        if start_date_filter:
            start_date_filter = datetime.datetime.strptime(str(request.POST.get("start_date_filter")), '%d-%m-%Y').strftime(
                '%Y-%m-%d')
        end_date_filter = request.POST.get("end_date_filter")
        if end_date_filter:
            end_date_filter = datetime.datetime.strptime(str(request.POST.get("end_date_filter")), '%d-%m-%Y').strftime(
                '%Y-%m-%d')
        status_filter = request.POST.get("status_filter")
        course_filter = request.POST.get("course_filter")
        faculty_filter = request.POST.get("faculty_filter")
        academic_info_obj = AcademicInfo.objects.all()
        course_obj = Course.objects.all()
        faculty_obj = UserInfo.objects.filter(fk_user_type__user_type ="Faculty")

        if request.POST.get("course_filter") and request.POST.get("faculty_filter") and request.POST.get(
                "start_date_filter") and request.POST.get("end_date_filter") and request.POST.get("status_filter"):
            leave_application_obj = LeaveApplication.objects.filter(fk_course_id=course_filter,
                                                                    fk_faculty_user_id=faculty_filter,
                                                                    date_post__range=[start_date_filter, end_date_filter],
                                                                    action_status=status_filter)

        elif request.POST.get("course_filter") and request.POST.get("faculty_filter") and request.POST.get("status_filter"):
            leave_application_obj = LeaveApplication.objects.filter(fk_course_id=course_filter,
                                                                    fk_faculty_user_id=faculty_filter,
                                                                    action_status=status_filter)

        elif request.POST.get("course_filter") and request.POST.get("faculty_filter"):
            leave_application_obj = LeaveApplication.objects.filter(fk_course_id=course_filter,
                                                                    fk_faculty_user_id=faculty_filter)

        elif request.POST.get("course_filter") and request.POST.get("start_date_filter"):
            leave_application_obj = LeaveApplication.objects.filter(fk_course_id=course_filter, date_post=start_date_filter)

        elif request.POST.get("course_filter") and request.POST.get("end_date_filter"):
            leave_application_obj = LeaveApplication.objects.filter(fk_course_id=course_filter, date_post=end_date_filter)

        elif request.POST.get("course_filter") and request.POST.get("status_filter"):
            leave_application_obj = LeaveApplication.objects.filter(fk_course_id=course_filter, action_status=status_filter)

        elif request.POST.get("course_filter") and request.POST.get("status_filter"):
            leave_application_obj = LeaveApplication.objects.filter(fk_course_id=course_filter, action_status=status_filter)

        elif request.POST.get("faculty_filter") and request.POST.get("start_date_filter"):
            leave_application_obj = LeaveApplication.objects.filter(fk_faculty_user_id=faculty_filter,
                                                                    date_post=start_date_filter)

        elif request.POST.get("faculty_filter") and request.POST.get("end_date_filter"):
            leave_application_obj = LeaveApplication.objects.filter(fk_faculty_user_id=faculty_filter,
                                                                    date_post=end_date_filter)

        elif request.POST.get("faculty_filter") and request.POST.get("status_filter"):
            leave_application_obj = LeaveApplication.objects.filter(fk_faculty_user_id=faculty_filter,
                                                                    action_status=status_filter)

        elif request.POST.get("start_date_filter") and request.POST.get("end_date_filter"):
            leave_application_obj = LeaveApplication.objects.filter(date_post__range=[start_date_filter, end_date_filter])

        elif request.POST.get("start_date_filter") and request.POST.get("status_filter"):
            leave_application_obj = LeaveApplication.objects.filter(date_post=start_date_filter,
                                                                    action_status=status_filter)

        elif request.POST.get("end_date_filter") and request.POST.get("status_filter"):
            leave_application_obj = LeaveApplication.objects.filter(date_post=end_date_filter, action_status=status_filter)

        elif request.POST.get("start_date_filter"):
            leave_application_obj = LeaveApplication.objects.filter(date_post=start_date_filter)

        elif request.POST.get("end_date_filter"):
            leave_application_obj = LeaveApplication.objects.filter(date_post=end_date_filter)

        elif request.POST.get("course_filter"):
            leave_application_obj = LeaveApplication.objects.filter(fk_course_id=course_filter)

        elif request.POST.get("faculty_filter"):
            leave_application_obj = LeaveApplication.objects.filter(fk_faculty_user_id=faculty_filter)

        elif request.POST.get("status_filter"):
            leave_application_obj = LeaveApplication.objects.filter(action_status=status_filter)

        else:
            leave_application_obj = LeaveApplication.objects.all()
        render_string = render_to_string("filter_leave_application.html", {"leave_application_obj": leave_application_obj,
                                                                           "academic_info_obj": academic_info_obj,
                                                                           "course_obj": course_obj,
                                                                           "faculty_obj": faculty_obj})
        return HttpResponse(render_string)
    except :
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


# deletes leave application
@csrf_exempt
def delete_leave_application(request):
    """
    enables student to delete leave application
    """
    try:
        id = request.POST.get("id")
        leave_application_obj = LeaveApplication.objects.get(id=id)
        leave_application_obj.delete()
        return HttpResponse("success")
    except :
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')
