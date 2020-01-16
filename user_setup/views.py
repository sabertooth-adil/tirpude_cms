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

from authentication.models import UserInfo
from master_forms.models import UserOperation, Module, Screen, UserRole


def screens_modules(request):
    session = request.session.get('user_id')
    if session:
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        modules_obj = Module.objects.all()
        screen_obj = Screen.objects.all()
        return render(request, "screens_modules.html",
                      {"user_operation_obj": user_operation_obj, "modules_obj": modules_obj, "screen_obj": screen_obj,
                       "user_info_obj": user_info_obj})
    else:
        return redirect("/")


@csrf_exempt
def add_module_name(request):
    module_name = request.POST.get("module_name")
    module_url = request.POST.get("module_url")
    modules_obj = Module(module_name=module_name, module_url=module_url)
    modules_obj.save()
    user_role_obj = UserRole.objects.all()
    for i in user_role_obj:
        user_operation_obj = UserOperation(status='module', fk_module=modules_obj, fk_user_role_id=i.id,
                                           special_data='Y')
        user_operation_obj.save()
    return HttpResponse("success")


@csrf_exempt
def edit_module_name(request):
    id = request.POST.get("id")
    modules_obj = Module.objects.get(id=id)
    return JsonResponse(
        {"id": modules_obj.id, "module_name": modules_obj.module_name, "module_url": modules_obj.module_url})


@csrf_exempt
def update_module_name(request):
    module_id = request.POST.get("module_id")
    module_name = request.POST.get("module_name")
    module_url = request.POST.get("module_url")
    modules_obj = Module.objects.get(id=module_id)
    modules_obj.module_name = module_name
    modules_obj.module_url = module_url
    modules_obj.save()
    return HttpResponse("success")


@csrf_exempt
def delete_module(request):
    id = request.POST.get("id")
    modules_obj = Module.objects.get(id=id)
    modules_obj.delete()
    return HttpResponse("success")


@csrf_exempt
def add_screen_name(request):
    screen_module_name = request.POST.get("screen_module_name")
    screen_name = request.POST.get("screen_name")
    screen_url = request.POST.get("screen_url")
    screen_obj = Screen(fk_module_id=screen_module_name, screen_name=screen_name, screen_url=screen_url)
    screen_obj.save()
    user_role_obj = UserRole.objects.all()
    for i in user_role_obj:
        if UserOperation.objects.filter(status='module', fk_module_id=screen_obj.fk_module.id, fk_screen__isnull=True,
                                        fk_user_role_id=i.id).exists():
            user_operation_obj = UserOperation.objects.get(status='module', fk_module_id=screen_obj.fk_module.id,
                                                           fk_screen__isnull=True, fk_user_role_id=i.id)
            user_operation_obj.status = 'master_module'
            user_operation_obj.save()
        if screen_obj.fk_module:
            user_operation_obj = UserOperation(status='screen', fk_module_id=screen_obj.fk_module.id,
                                               fk_screen_id=screen_obj.id, fk_user_role_id=i.id, special_data='Y')
        else:
            user_operation_obj = UserOperation(status='module', fk_screen_id=screen_obj.id, fk_user_role_id=i.id,
                                               special_data='Y')
        user_operation_obj.save()
    return HttpResponse("success")


@csrf_exempt
def edit_screen_name(request):
    id = request.POST.get("id")
    screen_obj = Screen.objects.get(id=id)
    return JsonResponse(
        {"id": screen_obj.id, "module_name": screen_obj.fk_module.id, "screen_name": screen_obj.screen_name,
         "screen_url": screen_obj.screen_url})


@csrf_exempt
def update_screen_name(request):
    screen_id = request.POST.get("screen_id")
    screen_module_name = request.POST.get("screen_module_name")
    screen_name = request.POST.get("screen_name")
    screen_url = request.POST.get("screen_url")
    screen_obj = Screen.objects.get(id=screen_id)
    screen_obj.fk_module_id = screen_module_name
    screen_obj.screen_name = screen_name
    screen_obj.screen_url = screen_url
    screen_obj.save()
    user_operation_obj = UserOperation.objects.filter(fk_screen_id=screen_id)
    print(user_operation_obj)
    for i in user_operation_obj:
        print("id", i.id)
        i.fk_module_id = screen_module_name
        i.save()
    return HttpResponse("success")


@csrf_exempt
def delete_screen(request):
    id = request.POST.get("id")
    modules_obj = Screen.objects.get(id=id)
    modules_obj.delete()
    return HttpResponse("success")


def manage_user(request):
    session = request.session.get('user_id')
    if session:
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        modules_list = []
        user_operation_obj = UserOperation.objects.all()
        user_role_obj = UserRole.objects.all()
        modules_obj = Module.objects.all()
        screen_obj = Screen.objects.all()
        for i in screen_obj:
            if i.fk_module:
                modules_list.append(i.fk_module.id)
            else:
                pass
        modules_list = (list(set(modules_list)))
        return render(request, "manage_user.html",
                      {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                       "user_operation_obj": user_operation_obj, "user_role_obj": user_role_obj,
                       "modules_obj": modules_obj,
                       "screen_obj": screen_obj, "modules_list": modules_list})
    else:
        return redirect("/")


@csrf_exempt
def add_user_role(request):
    modules_list = []
    user_role = request.POST.get("user_role")
    user_role_obj = UserRole(user_role=user_role)
    user_role_obj.save()
    modules_obj = Module.objects.all()
    for i in modules_obj:
        user_operation_obj = UserOperation(fk_user_role_id=user_role_obj.id, fk_module_id=i.id, status='master_module')
        user_operation_obj.save()
        if Screen.objects.filter(fk_module_id=i.id).exists():
            screen_obj = Screen.objects.filter(fk_module_id=i.id)
            for j in screen_obj:
                print("screen_obj", j.id)
                user_operation_obj = UserOperation(fk_user_role_id=user_role_obj.id, fk_module_id=i.id,
                                                   fk_screen_id=j.id,
                                                   status='screen')
                user_operation_obj.save()
        else:
            user_operation_obj.status = 'module'
            user_operation_obj.save()

    user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_role_obj.id)
    screen_obj = Screen.objects.all()
    for i in screen_obj:
        if i.fk_module:
            modules_list.append(i.fk_module.id)
        else:
            pass
    modules_list = (list(set(modules_list)))
    print(modules_list)
    render_string = render_to_string("manage_user_rights_rander.html",
                                     {"user_operation_obj": user_operation_obj, "user_role_obj": user_role_obj,
                                      "modules_obj": modules_obj, "screen_obj": screen_obj,
                                      "modules_list": modules_list})
    return HttpResponse(render_string)


@csrf_exempt
def update_userright(request):
    user_role_obj_id = request.POST.get("user_role_obj_id")
    user_operation = json.loads(request.POST.get('user_operation'))
    print("user_role_obj_id", user_role_obj_id)
    for i in range(len(user_operation)):
        print("str(user_operation[str(i)]['Special'])", type(str(user_operation[str(i)]['Special'])))
        user_operation_obj = UserOperation.objects.get(id=str(user_operation[str(i)]['id']))
        if str(user_operation[str(i)]['Special']) == 'True':
            user_operation_obj.special_data = "Y"
            user_operation_obj.save()
        else:
            user_operation_obj.special_data = "N"
            user_operation_obj.save()
        if str(user_operation[str(i)]['View']) == 'True':
            user_operation_obj.view_data = "Y"
            user_operation_obj.save()
        else:
            user_operation_obj.view_data = "N"
            user_operation_obj.save()
        if str(user_operation[str(i)]['Edit']) == 'True':
            user_operation_obj.edit_data = "Y"
            user_operation_obj.save()
        else:
            user_operation_obj.edit_data = "N"
            user_operation_obj.save()
        if str(user_operation[str(i)]['Save']) == 'True':
            user_operation_obj.save_data = "Y"
            user_operation_obj.save()
        else:
            user_operation_obj.save_data = "N"
            user_operation_obj.save()
        if str(user_operation[str(i)]['Delete']) == 'True':
            user_operation_obj.delete_data = "Y"
            user_operation_obj.save()
        else:
            user_operation_obj.delete_data = "N"
            user_operation_obj.save()
    return HttpResponse("success")


def edit_manage_user(request, id):
    session = request.session.get('user_id')
    if session:
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        modules_list = []
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=id)
        user_role_obj = UserRole.objects.get(id=id)
        modules_obj = Module.objects.all()
        screen_obj = Screen.objects.all()
        for i in screen_obj:
            if i.fk_module:
                modules_list.append(i.fk_module.id)
            else:
                pass
        modules_list = (list(set(modules_list)))
        print(modules_list)
        return render(request, "edit_manage_user.html",
                      {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                       "user_operation_obj": user_operation_obj, "user_role_obj": user_role_obj,
                       "modules_obj": modules_obj,
                       "screen_obj": screen_obj, "modules_list": modules_list})
    else:
        return redirect("/")


@csrf_exempt
def update_user_role_name(request):
    user_role = request.POST.get("user_role")
    user_role_obj_id = request.POST.get("user_role_obj_id")
    user_role_obj = UserRole.objects.get(id=user_role_obj_id)
    user_role_obj.user_role = user_role
    user_role_obj.save()
    return HttpResponse("success")


@csrf_exempt
def delete_manage_role(request):
    id = request.POST.get("id")
    user_role_obj = UserRole.objects.get(id=id)
    user_role_obj.delete()
    return HttpResponse("success")


@csrf_exempt
def assign_user_role(request):
    id = request.POST.get("id")
    print(id)
    user_role = request.POST.get("user_role")
    print(user_role)
    userinfo_info = UserInfo.objects.get(id=id)
    userinfo_info.fk_user_role_id = user_role
    userinfo_info.save()
    return HttpResponse("success")
