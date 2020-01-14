from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import traceback


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
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def notice(request):
    """
    Page for Notice
    :param request:
    :return:
    """
    try:
        course_obj = Course.objects.all()
        semester_obj = Semester.objects.all()
        section_obj = Section.objects.all()
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            if user_info_obj.fk_user_type.user_type == "Student":
                show_notice = Notice.objects.filter(Q(audience="Student") | Q(audience="All")).order_by("-id")
                return render(request, "student_notice.html",
                              {"user_info_obj": user_info_obj, "show_notice": show_notice})
            else:
                user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
                my_notice = Notice.objects.filter(Q(audience="Faculty") | Q(audience="All")).order_by("-id")
                show_notice = Notice.objects.all().order_by("-id")
                return render(request, "faculty_notice.html",
                              {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                               "show_notice": show_notice, "my_notice": my_notice, "course_obj": course_obj,
                               "semester_obj": semester_obj, "section_obj": section_obj})
        else:
            return redirect("/")
    except Exception:

        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def save_notice(request):
    """
    Saving new notice details
    :param request:
    :return:
    """
    try:
        editor_data = request.POST.get("editor_data")
        title = request.POST.get("title_name")
        audience = request.POST.get("audience")
        course = request.POST.get("course")
        semester = request.POST.get("semester")
        section = request.POST.get("section")
        if audience == "Faculty":
            notice_object = Notice(notice_body=editor_data, notice_title=title, audience="Faculty")
        elif audience == "All":
            notice_object = Notice(notice_body=editor_data, notice_title=title, audience="All")
        else:
            if course == "All":
                notice_object = Notice(notice_body=editor_data, notice_title=title, audience="Student")
            else:
                if semester == "All":
                    notice_object = Notice(notice_body=editor_data, notice_title=title, fk_course_id=course,
                                           audience="Student")
                else:
                    if section == "All":
                        notice_object = Notice(notice_body=editor_data, notice_title=title, fk_course_id=course,
                                               fk_semester_id=semester, audience="Student")
                    else:
                        notice_object = Notice(notice_body=editor_data, notice_title=title, fk_course_id=course,
                                               fk_semester_id=semester, fk_section_id=section, audience="Student")

        notice_object.save()
        return redirect("/notice/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def get_single_notice_detail(request):
    """
    Append notice body details in page
    :param request:
    :return:
    """
    try:
        notice_id = request.POST.get("id")
        notice_object = Notice.objects.get(id=notice_id)
        return JsonResponse({"notice_body": notice_object.notice_body})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_single_notice_detail(request):
    """
    Deleting notice details from table
    :param request:
    :return:
    """
    try:
        notice_id = request.POST.get("id")
        notice_object = Notice.objects.get(id=notice_id)
        notice_object.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def filter_notice(request):
    """
    Filter for notice table
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            course = request.POST.get("filter_course")
            sem = request.POST.get("filter_semesters")
            section = request.POST.get("filter_sections")
            audience = request.POST.get("filter_audience")
            start_date = request.POST.get("filter_from_date")
            end_date = request.POST.get("filter_to_date")
            if start_date:
                start_date = datetime.datetime.strptime(str(request.POST.get("filter_from_date")), "%d-%m-%Y").strftime(
                    "%Y-%m-%d")
            if end_date:
                end_date = datetime.datetime.strptime(str(request.POST.get("filter_to_date")), "%d-%m-%Y").strftime(
                    "%Y-%m-%d")
            filter_str = "Notice.objects"
            if sem:
                filter_str += ".filter(fk_semester_id=sem)"
            if course:
                filter_str += ".filter(fk_course_id=course)"
            if audience:
                filter_str += ".filter(audience=audience)"
            if start_date:
                filter_str += ".filter(date__gte=start_date)"
            if end_date:
                filter_str += ".filter(date__lte=end_date)"
            if section:
                filter_str += ".filter(fk_section_id=section)"
            show_notice = eval(filter_str)
            render_string = render_to_string("filter_notice.html",
                                             {"user_operation_obj": user_operation_obj, "show_notice": show_notice})
            return HttpResponse(render_string)
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")
