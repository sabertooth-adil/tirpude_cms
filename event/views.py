from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.utils import timezone
from .models import *
import traceback
import datetime

from authentication.models import UserInfo, AcademicInfo, AddressDetail
from master_forms.models import Semester, Section, Course, UserOperation


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
        return redirect("error_handler_500")


@csrf_exempt
def students_event(request):
    """
    Event page view function for student and faculty
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        activity_obj = EventActivity.objects.all()
        event_obj = StudentEvent.objects.all()
        time_now = timezone.now()
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            course_obj = Course.objects.all()
            section_obj = Section.objects.all()
            semesters_obj = Semester.objects.all()
            StudentEvent.objects.filter(event_title__isnull=True).delete()

            if user_info_obj.fk_user_type.user_type == "Faculty":
                user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
                my_list_data = []
                dict_data = {}
                for i in event_obj:
                    dict_data["id"] = i.id
                    dict_data["total"] = EventActivity.objects.filter(fk_student_events=i.id).count()
                    my_list_data.append(dict_data)
                    dict_data = {}
                return render(request, "students_event.html", {"course_obj": course_obj, "activity_obj": activity_obj,
                                                               "event_obj": event_obj, "my_list_data": my_list_data,
                                                               "section_obj": section_obj,
                                                               "semesters_obj": semesters_obj,
                                                               "user_info_obj": user_info_obj,
                                                               "sections_obj": section_obj,
                                                               "user_operation_obj": user_operation_obj})
            else:
                return render(request, "Events.html",
                              {"event_obj": event_obj, "activity_obj": activity_obj, "time_now": time_now})

        else:
            return render(request, "Events.html",
                          {"event_obj": event_obj, "activity_obj": activity_obj, "time_now": time_now})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def events(request):
    """
    Event page view function
    :param request:
    :return:
    """
    try:
        event_obj = StudentEvent.objects.all()
        activity_obj = EventActivity.objects.all()

        time_now = timezone.now()

        return render(request, "Events.html", {"event_obj": event_obj, "activity_obj": activity_obj,
                                               "time_now": time_now})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_event(request):
    """
    Add event
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        students_event_obj = StudentEvent(fk_user_info_id=session)
        students_event_obj.save()
        return JsonResponse({"event_id": students_event_obj.id})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_event(request):
    """
    Edit event function
    :param request:
    :return:
    """
    try:
        section_obj = Section.objects.all()
        semesters_obj = Semester.objects.all()
        session = request.session.get("user_id")
        event_id = request.POST.get("event_id")
        event_registration_obj = EventRegistration.objects.filter(fk_student_events_id=event_id)
        if not event_id:
            students_event_obj = StudentEvent(fk_user_info_id=session)
            students_event_obj.save()
            event_obj = StudentEvent.objects.get(id=students_event_obj.id)
        else:
            event_obj = StudentEvent.objects.get(id=event_id)
        activity_obj = EventActivity.objects.filter(fk_student_events_id=event_obj.id)
        event_member_obj = EventMember.objects.filter(fk_student_events=event_obj.id)

        course_obj = Course.objects.all()
        render_string = render_to_string("edit_events.html", {"event_obj": event_obj,
                                                              "event_member_obj": event_member_obj,
                                                              "activity_obj": activity_obj,
                                                              "course_obj": course_obj,
                                                              "section_obj": section_obj,
                                                              "semesters_obj": semesters_obj,
                                                              "event_registration_obj": event_registration_obj})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def cancel_event(request):
    """
    cancel event function
    :param request:
    :return:
    """
    try:
        event_id = request.POST.get("event_id")
        StudentEvent.objects.filter(id=event_id).delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def save_event(request):
    """
    save event function
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        title = request.POST.get("title")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        event_details = request.POST.get("event_details")
        event_type = request.POST.get("event_type")
        event_id = request.POST.get("id")
        event_form = request.POST.get("event_form")
        students_event_obj = StudentEvent.objects.get(id=event_id)
        students_event_obj.fk_user_info_id = session
        students_event_obj.event_title = title
        students_event_obj.start_date = start_date
        students_event_obj.end_date = end_date
        students_event_obj.event_details = event_details
        students_event_obj.event_type = event_type
        students_event_obj.event_form = event_form
        students_event_obj.save()
        return HttpResponse("Success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_event(request):
    """
    delete event function
    :param request:
    :return:
    """
    try:
        event_id = request.POST.get("event_id")
        StudentEvent.objects.get(id=event_id).delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def save_activity(request):
    """
    save activity function
    :param request:
    :return:
    """
    try:
        event_id = request.POST.get("id")
        activity_name = request.POST.get("activity_name")
        schedule_date = request.POST.get("activity_start_date")
        start_time = request.POST.get("activity_from")
        end_time = request.POST.get("activity_to")
        activity_detail = request.POST.get("activity_detail")
        activity_type = request.POST.get("activity_type")
        activity_venue = request.POST.get("activity_venue")
        activity_obj = EventActivity(activity_name=activity_name,
                                     schedule_date=schedule_date,
                                     start_time=start_time,
                                     end_time=end_time,
                                     activity_details=activity_detail,
                                     activity_type=activity_type,
                                     activity_venue=activity_venue,
                                     fk_student_events_id=event_id, )
        activity_obj.save()
        activity_obj = EventActivity.objects.filter(fk_student_events_id=event_id)
        render_string = render_to_string("activity_list.html", {"activity_obj": activity_obj})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_activity(request):
    """
    delete activity function
    :param request:
    :return:
    """
    try:
        activity_id = request.POST.get("activity_id")
        EventActivity.objects.get(id=activity_id).delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_activity(request):
    """
    update activity details function
    :param request:
    :return:
    """
    try:
        activity_id = request.POST.get("activity_id")
        activity_name = request.POST.get("activity_name")
        schedule_date = request.POST.get("activity_date")
        start_time = request.POST.get("activity_from")
        end_time = request.POST.get("activity_to")
        activity_type = request.POST.get("activity_type")
        activity_venue = request.POST.get("activity_venue")
        activity_detail = request.POST.get("activity_detail")
        EventActivity.objects.filter(id=activity_id).update(activity_name=activity_name,
                                                            schedule_date=schedule_date,
                                                            start_time=start_time,
                                                            end_time=end_time,
                                                            activity_details=activity_detail,
                                                            activity_type=activity_type,
                                                            activity_venue=activity_venue)
        event_id = EventActivity.objects.get(id=activity_id).fk_student_events.id
        activity_obj = EventActivity.objects.filter(fk_student_events_id=event_id)
        render_string = render_to_string("activity_list.html", {"activity_obj": activity_obj})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def filter_member(request):
    """
    filter members for adding in event
    :param request:
    :return:
    """
    try:
        event_id = request.POST.get("event_id")
        member_key = request.POST.get("member_key")
        sections = request.POST.get("sections")
        course = request.POST.get("course")
        semester = request.POST.get("semester")

        event_member_id_list = []
        for i in EventMember.objects.filter(fk_student_events_id=event_id):
            event_member_id_list.append(i.fk_user_info_id)
        if member_key == "Student":
            academicinfo_obj = AcademicInfo.objects.filter(fk_sections_id=sections,
                                                           fk_course_id=course,
                                                           fk_semesters_id=semester)
            render_string = render_to_string("filter_event_member.html", {"academicinfo_obj": academicinfo_obj,
                                                                          "event_member_id_list": event_member_id_list})

        else:
            faculty_obj = UserInfo.objects.filter(fk_user_type__user_type=member_key)
            render_string = render_to_string("filter_event_member.html", {"faculty_obj": faculty_obj,
                                                                          "event_member_id_list": event_member_id_list})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_event_member(request):
    """
    Adding filter members to the event
    :param request:
    :return:
    """
    try:
        member_list = request.POST.get("member_list")
        event_id = request.POST.get("event_id")
        member_key = request.POST.get("member_key")

        if member_key == "Student":
            for i in member_list.split(","):
                if not EventMember.objects.filter(fk_user_info_id=i, fk_student_events_id=event_id).exists():
                    academic_obj = AcademicInfo.objects.get(fk_user_info=i)
                    event_member_obj = EventMember(fk_student_events_id=event_id,
                                                   fk_user_info_id=i,
                                                   fk_course_id=academic_obj.fk_course.id,
                                                   fk_semesters_id=academic_obj.fk_semesters.id,
                                                   fk_sections_id=academic_obj.fk_sections.id)
                    event_member_obj.save()
        else:
            for i in member_list.split(","):
                if not EventMember.objects.filter(fk_user_info_id=i, fk_student_events_id=event_id).exists():
                    event_member_obj = EventMember(fk_student_events_id=event_id,
                                                   fk_user_info_id=i)
                    event_member_obj.save()

        event_member_obj = EventMember.objects.filter(fk_student_events=event_id)
        render_string = render_to_string("event_Members.html", {"event_member_obj": event_member_obj})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_event_member(request):
    """
    Delete added event members
    :param request:
    :return:
    """
    try:
        event_id = request.POST.get("id")
        EventMember.objects.get(id=event_id).delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def manage_activity_member(request):
    """
    Allot event's member to the event's activity
    :param request:
    :return:
    """
    try:
        activity_id = request.POST.get("activity_id")
        event_id = EventActivity.objects.get(id=activity_id).fk_student_events_id
        event_member_obj = EventMember.objects.filter(fk_student_events=event_id)
        activity_member_obj = ActivityMember.objects.filter(fk_activity_id=activity_id)
        render_string = render_to_string("manage_activity_member.html", {"event_member_obj": event_member_obj,
                                                                         "activity_id": activity_id,
                                                                         "activity_member_obj": activity_member_obj})
        return JsonResponse(
            {"render_string": render_string, "activity_name": EventActivity.objects.get(id=activity_id).activity_name})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def save_activity_member(request):
    """
    save alloyted event"s activity member
    :param request:
    :return:
    """
    try:
        event_member_id = request.POST.get("event_member_id")
        member_role = request.POST.get("member_role")
        member_task = request.POST.get("member_task")
        activity_id = request.POST.get("activity_id")
        event_id = EventActivity.objects.get(id=activity_id).fk_student_events_id
        event_member_obj = EventMember.objects.filter(fk_student_events=event_id)

        activity_member_obj = ActivityMember(fk_event_member_id=event_member_id,
                                             fk_activity_id=activity_id,
                                             roles=member_role,
                                             task=member_task)
        activity_member_obj.save()

        activity_member_obj = ActivityMember.objects.filter(fk_activity_id=activity_id)
        render_string = render_to_string("manage_activity_member.html", {"event_member_obj": event_member_obj,
                                                                         "activity_member_obj": activity_member_obj,
                                                                         "activity_id": activity_id})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_activity_member(request):
    """
    Update alloted event's activity member
    :param request:
    :return:
    """
    try:
        event_member_id = request.POST.get("event_member_id")
        member_role = request.POST.get("member_role")
        member_task = request.POST.get("member_task")
        activity_member_id = request.POST.get("activity_member_id")

        activity_id = ActivityMember.objects.get(id=activity_member_id).fk_activity_id
        event_id = EventActivity.objects.get(id=activity_id).fk_student_events_id

        activity_member_obj = ActivityMember.objects.get(id=activity_member_id)
        activity_member_obj.fk_event_member_id = event_member_id
        activity_member_obj.roles = member_role
        activity_member_obj.task = member_task
        activity_member_obj.save()

        event_member_obj = EventMember.objects.filter(fk_student_events=event_id)

        activity_member_obj = ActivityMember.objects.filter(fk_activity_id=activity_id)
        render_string = render_to_string("manage_activity_member.html", {"event_member_obj": event_member_obj,
                                                                         "activity_member_obj": activity_member_obj,
                                                                         "activity_id": activity_id})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_activity_member(request):
    """
    Delete allotted event"s activity member
    :param request:
    :return:
    """
    try:
        activity_member_id = request.POST.get("activity_member_id")
        ActivityMember.objects.get(id=activity_member_id).delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def manage_activity_guest(request):
    """
    Add guest to the activity
    :param request:
    :return:
    """
    try:
        activity_id = request.POST.get("activity_id")

        activity_guest_obj = ActivityGuest.objects.filter(fk_activity_id=activity_id)
        render_string = render_to_string("manage_activity_guest.html", {"activity_id": activity_id,
                                                                        "activity_guest_obj": activity_guest_obj})
        return JsonResponse(
            {"render_string": render_string, "activity_name": EventActivity.objects.get(id=activity_id).activity_name})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def save_activity_guest(request):
    """
    Save added activity guest
    :param request:
    :return:
    """
    try:
        activity_id = request.POST.get("activity_id")
        name = request.POST.get("name")
        college = request.POST.get("college")
        purpose = request.POST.get("purpose")
        email = request.POST.get("email")
        contact_no = request.POST.get("contact_no")

        activity_guest_obj = ActivityGuest(fk_activity_id=activity_id,
                                           name=name,
                                           college=college,
                                           purpose=purpose,
                                           email=email,
                                           contact_no=contact_no)
        activity_guest_obj.save()
        activity_guest_obj = ActivityGuest.objects.filter(fk_activity_id=activity_id)

        render_string = render_to_string("manage_activity_guest.html", {"activity_guest_obj": activity_guest_obj,
                                                                        "activity_id": activity_id})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_activity_guest(request):
    """
    Update added activity guest
    :param request:
    :return:
    """
    try:
        activity_guest_id = request.POST.get("activity_guest_id")
        name = request.POST.get("name")
        college = request.POST.get("college")
        purpose = request.POST.get("purpose")
        email = request.POST.get("email")
        contact_no = request.POST.get("contact_no")

        activity_id = ActivityGuest.objects.get(id=activity_guest_id).fk_activity_id

        activity_guest_obj = ActivityGuest.objects.get(id=activity_guest_id)
        activity_guest_obj.name = name
        activity_guest_obj.college = college
        activity_guest_obj.purpose = purpose
        activity_guest_obj.email = email
        activity_guest_obj.contact_no = contact_no

        activity_guest_obj.save()

        activity_guest_obj = ActivityGuest.objects.filter(fk_activity_id=activity_id)
        render_string = render_to_string("manage_activity_guest.html", {"activity_guest_obj": activity_guest_obj,
                                                                        "activity_id": activity_id})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_activity_guest(request):
    """
    Delete added activity guest
    :param request:
    :return:
    """
    try:
        activity_guest_id = request.POST.get("activity_guest_id")
        ActivityGuest.objects.get(id=activity_guest_id).delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def manage_finance_modal(request):
    """
    Open modal to manage the budget of activity and
    events
    :param request:
    :return:
    """
    try:
        event_id = request.POST.get("event_id")

        activity_obj = EventActivity.objects.filter(fk_student_events=event_id)
        activity_item_obj = ActivityItem.objects.all()

        my_list_data = []
        dict_data = {}
        e_total = 0
        for activity in activity_obj:
            total = 0
            dict_data["id"] = activity.id
            for item in ActivityItem.objects.filter(fk_activity=activity.id):
                total += item.item_quantity * item.item_cost
                e_total += item.item_quantity * item.item_cost
            dict_data["total"] = total
            my_list_data.append(dict_data)
            dict_data = {}

        total_dict = {
            "event_total_item_cost": e_total,
            "total_propose_budget": EventActivity.objects.filter(fk_student_events=event_id).aggregate(Sum("propose"))[
                "propose__sum"],
            "total_allotted_budget":
                EventActivity.objects.filter(fk_student_events=event_id).aggregate(Sum("allotted"))[
                    "allotted__sum"],
            "total_actual_budget": EventActivity.objects.filter(fk_student_events=event_id).aggregate(Sum("actual"))[
                "actual__sum"]
        }

        render_string = render_to_string("manage_activity_budget.html", {"activity_obj": activity_obj,
                                                                         "activity_item_obj": activity_item_obj,
                                                                         "my_list_data": my_list_data,
                                                                         "total_dict": total_dict})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def save_item(request):
    """
    Save item related to the activity with
    name, quantity and cost
    :param request:
    :return:
    """
    try:
        activity_id = request.POST.get("activity_id")
        item_name = request.POST.get("item_name")
        item_cost = request.POST.get("item_cost")
        item_quantity = request.POST.get("item_quantity")

        activity_item_obj = ActivityItem(fk_activity_id=activity_id,
                                         item=item_name,
                                         item_cost=item_cost,
                                         item_quantity=item_quantity)
        activity_item_obj.save()

        activity_item_obj = ActivityItem.objects.filter(fk_activity_id=activity_id)
        render_string = render_to_string("activity_item_list.html", {"activity_item_obj": activity_item_obj})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_activity_item(request):
    """
    Update item related to the activity
    :param request:
    :return:
    """
    try:
        item_id = request.POST.get("item_id")
        item_name = request.POST.get("item_name")
        item_cost = request.POST.get("item_cost")
        item_quantity = request.POST.get("item_quantity")

        activity_item_obj = ActivityItem.objects.get(id=item_id)
        activity_item_obj.item = item_name
        activity_item_obj.item_cost = item_cost
        activity_item_obj.item_quantity = item_quantity
        activity_item_obj.save()

        activity_id = ActivityItem.objects.get(id=item_id).fk_activity_id
        activity_item_obj = ActivityItem.objects.filter(fk_activity_id=activity_id)
        render_string = render_to_string("activity_item_list.html", {"activity_item_obj": activity_item_obj})
        return JsonResponse({"render_string": render_string, "activity_id": activity_id})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_activity_item(request):
    """
    Delete item related to the activity
    :param request:
    :return:
    """
    try:
        item_id = request.POST.get("item_id")
        ActivityItem.objects.get(id=item_id).delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def save_activity_budget(request):
    """
    Saving the activity allotted, proposed and actual
    budget
    :param request:
    :return:
    """
    try:
        activity_id = request.POST.get("activity_id")
        proposed = request.POST.get("proposed")
        allotted = request.POST.get("allotted")
        actual = request.POST.get("actual")

        activity_obj = EventActivity.objects.get(id=activity_id)
        activity_obj.propose = proposed
        activity_obj.allotted = allotted
        activity_obj.actual = actual
        activity_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def event_registration_form(request):
    """
    Event registration form for registering the
    event participant
    :param request:
    :return:
    """
    try:
        event_id = request.POST.get("event_id")

        event_registration_obj = EventRegistration(fk_student_events_id=event_id)
        event_registration_obj.save()

        event_obj = StudentEvent.objects.get(id=event_id)
        activity_obj = EventActivity.objects.filter(fk_student_events_id=event_id)

        render_string = render_to_string("event_registration_form.html", {"event_obj": event_obj,
                                                                          "activity_obj": activity_obj,
                                                                          "event_registration_id":
                                                                              event_registration_obj.id})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_grp_member(request):
    """
    Add group members to the event
    :param request:
    :return:
    """
    try:
        activity_id = request.POST.get("activity_id")
        grp_member_list = request.POST.get("grp_member_list")
        event_registration_id = request.POST.get("event_registration_id")
        for i in grp_member_list.split(","):
            activity_group_member_obj = ActivityGroupMember(fk_events_registrations_id=event_registration_id,
                                                            fk_activity_id=activity_id,
                                                            grp_member_name=i)
            activity_group_member_obj.save()

        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def remove_grp_member(request):
    """
    Remove added group member
    :param request:
    :return:
    """
    try:
        activity_id = request.POST.get("activity_id")
        event_registration_id = request.POST.get("event_registration_id")
        ActivityGroupMember.objects.filter(fk_events_registrations_id=event_registration_id,
                                           fk_activity_id=activity_id).delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def save_event_registration(request):
    """
    Save event participant details
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        event_registration_id = request.POST.get("event_registration_id")
        event_id = request.POST.get("event_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        college = request.POST.get("college")
        course_year = request.POST.get("course_year")
        email = request.POST.get("email")
        contact_no = request.POST.get("contact_no")
        address = request.POST.get("address")
        city = request.POST.get("city")
        gender = request.POST.get("gender")
        activity_selected_list = request.POST.get("activity_selected_list")

        if EventRegistration.objects.filter(fk_student_events_id=event_id, email=email).exists():
            EventRegistration.objects.get(fk_student_events_id=event_id, email=email).delete()

        event_registration_obj = EventRegistration.objects.get(id=event_registration_id)

        try:
            event_registration_obj.fk_user_info_id = UserInfo.objects.get(id=session).id
        except Exception:
            pass
        event_registration_obj.first_name = first_name
        event_registration_obj.last_name = last_name
        event_registration_obj.college = college
        event_registration_obj.email = email
        event_registration_obj.contact_no = contact_no
        event_registration_obj.course_year = course_year
        event_registration_obj.address = address
        event_registration_obj.gender = gender
        event_registration_obj.gender = gender
        event_registration_obj.city = city
        event_registration_obj.save()

        for i in activity_selected_list.split(","):
            activity_group_member_obj = ActivityGroupMember(fk_events_registrations_id=event_registration_id,
                                                            fk_activity_id=i,
                                                            grp_member_name=first_name + " " + last_name)
            activity_group_member_obj.save()

        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def event_registration_login(request):
    """
    Event registration login for tirpude students
    :param request:
    :return:
    """
    try:
        id_username = request.POST.get("id_username")
        id_password = request.POST.get("id_password")
        if UserInfo.objects.filter(email=id_username, password=id_password).exists():
            if UserInfo.objects.filter(email=id_username, password=id_password, status="Active").exists():
                obj_userinfo = UserInfo.objects.get(email=id_username, password=id_password)
                request.session["user_id"] = obj_userinfo.id

                year = 1
                academic_obj = AcademicInfo.objects.get(fk_user_info_id=obj_userinfo.id)
                if academic_obj.fk_semesters == 1 or academic_obj.fk_semesters == 2:
                    year = 1
                if academic_obj.fk_semesters == 3 or academic_obj.fk_semesters == 4:
                    year = 2
                if academic_obj.fk_semesters == 5 or academic_obj.fk_semesters == 6:
                    year = 3

                address_obj = AddressDetail.objects.get(fk_user_info_id=obj_userinfo.id)

                dict_data = {
                    "first_name": obj_userinfo.first_name,
                    "last_name": obj_userinfo.last_name,
                    "email": obj_userinfo.email,
                    "year": year,
                    "gender": obj_userinfo.fk_gender.gender,
                    "phone_no": obj_userinfo.phone_no,
                    "address": address_obj.address,
                    "city": address_obj.fk_city.city
                }

                list_data = [dict_data]
                return JsonResponse({"success": "success", "list": list_data})
            else:
                return JsonResponse({"success": "unauthorized user"})
        else:
            return JsonResponse({"success": "error"})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def activity_participant_modal(request):
    """
    Open modal to view activity participants
    :param request:
    :return:
    """
    try:
        activity_id = request.POST.get("activity_id")
        event_id = EventActivity.objects.get(id=activity_id).fk_student_events_id

        "count ", EventRegistration.objects.filter(first_name__isnull=True).delete()

        event_registration_obj = EventRegistration.objects.filter(fk_student_events=event_id)
        activity_grpmember_obj = ActivityGroupMember.objects.filter(fk_activity_id=activity_id)

        event_registration_ids_list = []

        for i in ActivityGroupMember.objects.filter(fk_activity_id=activity_id).distinct():
            event_registration_ids_list.append(i.fk_events_registrations_id)

        render_string = render_to_string("activity_pariticipant_modal.html",
                                         {"event_registration_obj": event_registration_obj,
                                          "activity_grpmember_obj": activity_grpmember_obj,
                                          "event_registration_ids_list": event_registration_ids_list,
                                          "event_id": event_id})
        return JsonResponse(
            {"render_string": render_string, "activity_name": EventActivity.objects.get(id=activity_id).activity_name})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")
