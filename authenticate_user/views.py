from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import random
from django.conf import settings
from django.core.mail import EmailMessage
import base64
import datetime
import traceback
from django.template.loader import render_to_string

from authentication.models import UserInfo, AcademicInfo
from authentication.views import error_save
from master_forms.models import UserOperation, UserType, UserRole
from attendance.views import date_range


def authenticate_user(request):
    """
     Call Authenticate User Page
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            user_info_detail_obj = UserInfo.objects.all().order_by('-id')
            academic_info_obj = AcademicInfo.objects.all()
            base = datetime.datetime.today()
            date_list = [base - datetime.timedelta(days=x) for x in range(30)]
            print(date_list[0])
            user_obj = UserInfo.objects.filter(registration_date__range=[date_list[0], date_list[-1]])
            user_type_obj = UserType.objects.all()
            user_role_obj = UserRole.objects.all()
            return render(request, "authenticate_user.html",
                          {"user_operation_obj": user_operation_obj, "user_role_obj": user_role_obj,
                           "user_info_detail_obj": user_info_detail_obj, "user_info_obj": user_info_obj,
                           "academic_info_obj": academic_info_obj, "user_obj": user_obj, "user_type_obj": user_type_obj,
                           "to_date": date_list[0], "from_date": date_list[-1]})
        else:
            return redirect("/")
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def activate_deactivate_user(request):
    """
    Activate or Deactivate User
    :param request:
    :return:
    """
    try:
        id = request.POST.get("id")
        change_status = request.POST.get("change_status")
        print(id)
        print(change_status)
        user_info_obj = UserInfo.objects.get(id=id)
        print("user_info_obj", user_info_obj)
        user_info_obj.status = change_status
        user_info_obj.save()
        return HttpResponse("success")
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_authenticate_user(request):
    """
    Filter Authenticate User by user_type, status, to_date, from_date
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            user_role_obj = UserRole.objects.all()
            user_type = request.POST.get("user_type")
            status = request.POST.get("status")
            to_date = request.POST.get("to_date")
            from_date = request.POST.get("from_date")
            base = datetime.datetime.today()
            if to_date and from_date:
                from_date = datetime.datetime.strptime(from_date, '%d-%m-%Y')
                to_date = datetime.datetime.strptime(to_date, '%d-%m-%Y')
                date_list = [d for d in date_range(from_date, to_date)]
                start_date_range = str(date_list[-1].strftime('%Y-%m-%d'))
                end_date_range = str(date_list[0].strftime('%Y-%m-%d'))
            else:
                date_list = [base - datetime.timedelta(days=x) for x in range(30)]
                start_date_range = str(date_list[0].strftime('%Y-%m-%d'))
                end_date_range = str(date_list[-1].strftime('%Y-%m-%d'))
            print(date_list)
            user_obj = UserInfo.objects.filter(registration_date__range=[start_date_range, end_date_range])

            print("user_type", user_type)
            print("status", status)
            print("to_date", to_date)
            print("from_date", from_date)

            if user_type and status and from_date and to_date:
                user_info_detail_obj = UserInfo.objects.filter(fk_user_type__id=user_type, status=status,
                                                               registration_date__range=[from_date, to_date]).order_by(
                    '-id')
            elif user_type and status and to_date:
                user_info_detail_obj = UserInfo.objects.filter(fk_user_type__id=user_type, status=status,
                                                               registration_date=to_date).order_by('-id')
            elif user_type and status and from_date:
                user_info_detail_obj = UserInfo.objects.filter(fk_user_type__id=user_type, status=status,
                                                               registration_date=from_date).order_by('-id')
            elif user_type and to_date and from_date:
                user_info_detail_obj = UserInfo.objects.filter(fk_user_type__id=user_type,
                                                               registration_date__range=[from_date, to_date]).order_by(
                    '-id')
            elif status and to_date and from_date:
                user_info_detail_obj = UserInfo.objects.filter(status=status,
                                                               registration_date__range=[from_date, to_date]).order_by(
                    '-id')
            elif status and to_date and from_date:
                user_info_detail_obj = UserInfo.objects.filter(status=status,
                                                               registration_date__range=[from_date, to_date]).order_by(
                    '-id')
            elif status and to_date:
                user_info_detail_obj = UserInfo.objects.filter(status=status, registration_date=to_date).order_by('-id')
            elif status and from_date:
                user_info_detail_obj = UserInfo.objects.filter(status=status, registration_date=from_date).order_by('-id')
            elif from_date and to_date:
                user_info_detail_obj = UserInfo.objects.filter(registration_date__range=[from_date, to_date]).order_by(
                    '-id')
            elif user_type:
                print("user_type", user_type)
                user_info_detail_obj = UserInfo.objects.filter(fk_user_type_id=user_type).order_by('-id')
            elif status:
                user_info_detail_obj = UserInfo.objects.filter(status=status).order_by('-id')
            elif to_date:
                user_info_detail_obj = UserInfo.objects.filter(registration_date=to_date).order_by('-id')
            elif from_date:
                user_info_detail_obj = UserInfo.objects.filter(registration_date=from_date).order_by('-id')
            else:
                print("dcxvzxmbmn")
                user_info_detail_obj = UserInfo.objects.all().order_by('-id')
            academic_info_obj = AcademicInfo.objects.all()
            print(academic_info_obj)
            print(user_info_detail_obj)
            render_string = render_to_string("authenticate_user_filter.html",
                                             {"user_role_obj": user_role_obj, "user_operation_obj": user_operation_obj,
                                              "academic_info_obj": academic_info_obj,
                                              "user_info_detail_obj": user_info_detail_obj, "user_obj": user_obj})
            return HttpResponse(render_string)
        else:
            return redirect("/")
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')

@csrf_exempt
def delete_register_request(request):
    """
    Delete Register User
    :param request:
    :return:
    """
    try:
        id = request.POST.get("id")
        print("id",id)
        user_info_detail_obj = UserInfo.objects.get(id=id)
        print(user_info_detail_obj)
        user_info_detail_obj.delete()
        return HttpResponse("success")
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def assign_user_role(request):
    """
    Assign Role to User only registed as Faculty
    :param request:
    :return:
    """
    try:
        id = request.POST.get("id")
        print(id)
        user_role = request.POST.get("user_role")
        print(user_role)
        userinfo_info = UserInfo.objects.get(id=id)
        userinfo_info.fk_user_role_id = user_role
        userinfo_info.save()
        return HttpResponse("success")
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')
