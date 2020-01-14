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
import os
import csv
import json
from django.db.models import F, Q

from authentication.models import UserInfo, AddressDetail, AcademicInfo
from authentication.views import error_save
from master_forms.models import UserOperation, CompanyType, JobType, SelectionProcessTest, Course, Semester, Section
from placement.models import Company, CompanyAppearance, CompanyAppearanceDateTime, CompanyAppearanceJobTypeDetail, \
    AppleCompanyAppearance, CompanyAppearanceTestResult


def company(request):
    """
    Company Page
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            company_obj = Company.objects.all()
            company_type_obj = CompanyType.objects.all()
            return render(request, "placement_companies.html",
                          {"user_info_obj": user_info_obj, "user_operation_obj": user_operation_obj,
                           "company_obj": company_obj, "company_type_obj": company_type_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def add_company(request):
    """
    Add Company Master
    :param request:
    :return:
    """
    try:
        company_name = request.POST.get("company_name")
        company_type = request.POST.get("company_type")
        company_location = request.POST.get("company_location")
        company_main_address = request.POST.get("company_main_address")
        company_other_detail = request.POST.get("company_other_detail")
        contact_person_one_name = request.POST.get("contact_person_one_name")
        contact_person_one_email = request.POST.get("contact_person_one_email")
        contact_person_one_mobile_no = request.POST.get("contact_person_one_mobile_no")
        contact_person_two_name = request.POST.get("contact_person_two_name")
        contact_person_two_email = request.POST.get("contact_person_two_email")
        contact_person_two_mobile_no = request.POST.get("contact_person_two_mobile_no")
        company_obj = Company(company_name=company_name, fk_company_type_id=company_type,
                              company_location=company_location,
                              company_main_address=company_main_address, company_other_detail=company_other_detail,
                              contact_person_one_name=contact_person_one_name,
                              contact_person_one_email=contact_person_one_email,
                              contact_person_one_mobile_no=contact_person_one_mobile_no,
                              contact_person_two_name=contact_person_two_name,
                              contact_person_two_email=contact_person_two_email,
                              contact_person_two_mobile_no=contact_person_two_mobile_no)
        company_obj.save()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def edit_company(request):
    """
    Edit Company Master Page
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        id = request.POST.get("id")
        company_type_obj = Company.objects.get(id=id)
        dict_data['id'] = company_type_obj.id
        dict_data['company_name'] = company_type_obj.company_name
        dict_data['fk_company_type_id'] = company_type_obj.fk_company_type.id
        dict_data['company_location'] = company_type_obj.company_location
        dict_data['company_main_address'] = company_type_obj.company_main_address
        dict_data['company_other_detail'] = company_type_obj.company_other_detail
        dict_data['contact_person_one_name'] = company_type_obj.contact_person_one_name
        dict_data['contact_person_one_email'] = company_type_obj.contact_person_one_email
        dict_data['contact_person_one_mobile_no'] = company_type_obj.contact_person_one_mobile_no
        dict_data['contact_person_two_name'] = company_type_obj.contact_person_two_name
        dict_data['contact_person_two_email'] = company_type_obj.contact_person_two_email
        dict_data['contact_person_two_mobile_no'] = company_type_obj.contact_person_two_mobile_no
        list_data.append(dict_data)
        print(list_data)
        return JsonResponse({"list_data": list_data})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def update_company(request):
    """
    Update Company Master Data
    :param request:
    :return:
    """
    try:
        id = request.POST.get("company_id")
        print("id")
        print(request.POST.get("edit_company_other_detail"))
        company_obj = Company.objects.get(id=id)
        company_obj.company_name = request.POST.get("edit_company_name")
        company_obj.fk_company_type_id = request.POST.get("edit_company_type")
        company_obj.company_location = request.POST.get("edit_company_location")
        company_obj.company_main_address = request.POST.get("edit_company_main_address")
        company_obj.company_other_detail = request.POST.get("edit_company_other_detail")
        company_obj.contact_person_one_name = request.POST.get("edit_contact_person_one_name")
        company_obj.contact_person_one_email = request.POST.get("edit_contact_person_one_email")
        company_obj.contact_person_one_mobile_no = request.POST.get("edit_contact_person_one_mobile_no")
        company_obj.contact_person_two_name = request.POST.get("edit_contact_person_two_name")
        company_obj.contact_person_two_email = request.POST.get("edit_contact_person_two_email")
        company_obj.contact_person_two_mobile_no = request.POST.get("edit_contact_person_two_mobile_no")
        company_obj.save()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def delete_company(request):
    """
    Delete Company Master
    :param request:
    :return:
    """
    try:
        id = request.POST.get("id")
        company_obj = Company.objects.get(id=id)
        company_obj.delete()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def company_appearances(request):
    """
    Company Appearances Page
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            company_obj = Company.objects.all()
            company_type_obj = CompanyType.objects.all()
            job_type_obj = JobType.objects.all()
            company_appearance_obj = CompanyAppearance.objects.all()
            list_data = []
            dict_data = {}
            for i in company_appearance_obj:
                dict_data['company_appearance_id'] = i.id
                date_list = list(
                    CompanyAppearance.objects.filter(id=i.id).values_list('fk_company_appearance_date_time_list__date',
                                                                          flat=True))
                dict_data['max_date'] = max(date_list)
                dict_data['min_date'] = min(date_list)
                list_data.append(dict_data)
                dict_data = {}
            print(list_data)
            return render(request, "placement_company_appearance.html",
                          {"list_data": list_data, "user_info_obj": user_info_obj,
                           "user_operation_obj": user_operation_obj,
                           "company_obj": company_obj, "company_type_obj": company_type_obj,
                           "job_type_obj": job_type_obj,
                           "company_appearance_obj": company_appearance_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def edit_company_appearances(request, id):
    """
    Edit Company Appearances Page
    :param request:
    :param id:
    :return:
    """
    try:
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            selection_process_test_obj = SelectionProcessTest.objects.all()
            job_type_obj = JobType.objects.all()
            company_obj = Company.objects.get(id=id)
            company_appearance_obj = CompanyAppearance.objects.filter(fk_company=company_obj)
            company_appearance_not_apply_obj = list(CompanyAppearance.objects.filter(
                fk_company_appearance_date_time_list__date__lte=datetime.datetime.now().strftime(
                    '%Y-%m-%d')).values_list(
                'id', flat=True).distinct())
            return render(request, "placement_edit_company_appearance.html",
                          {"company_appearance_not_apply_obj": company_appearance_not_apply_obj,
                           "user_info_obj": user_info_obj,
                           "user_operation_obj": user_operation_obj, "company_appearance_obj": company_appearance_obj,
                           "company_obj": company_obj, "selection_process_test_obj": selection_process_test_obj,
                           "job_type_obj": job_type_obj, "job_type_obj": job_type_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def add_company_visiting_selection_precess_date_time(request):
    """
    Add Company Visiting Selection Precess, Date, Time
    :param request:
    :return:
    """
    try:
        dict_data = {}
        list_data = []
        company_visiting_selection_process_test = request.POST.get("company_visiting_selection_process_test")
        company_visited_date = request.POST.get("company_visited_date")
        company_visited_start_time = request.POST.get("company_visited_start_time")
        company_visited_end_time = request.POST.get("company_visited_end_time")

        company_visited_date = datetime.datetime.strptime(str(company_visited_date), '%d-%m-%Y').strftime('%Y-%m-%d')
        if company_visited_start_time:
            company_visited_start_time = datetime.datetime.strptime(str(company_visited_start_time),
                                                                    '%I:%M %p').strftime(
                '%H:%M:%S')
        else:
            company_visited_start_time = None
        if company_visited_end_time:
            company_visited_end_time = datetime.datetime.strptime(str(company_visited_end_time), '%I:%M %p').strftime(
                '%H:%M:%S')
        else:
            company_visited_end_time = None
        company_appearance_date_time_obj = CompanyAppearanceDateTime(
            fk_selection_process_test_id=company_visiting_selection_process_test, date=company_visited_date,
            start_time=company_visited_start_time, end_time=company_visited_end_time)
        company_appearance_date_time_obj.save()

        dict_data['id'] = company_appearance_date_time_obj.id
        dict_data['fk_selection_process_test_id'] = company_appearance_date_time_obj.fk_selection_process_test.id
        dict_data[
            'fk_selection_process_test_name'] = company_appearance_date_time_obj.fk_selection_process_test.test_name
        dict_data['date'] = datetime.datetime.strptime(str(company_appearance_date_time_obj.date), '%Y-%m-%d').strftime(
            '%d-%m-%Y')
        if company_appearance_date_time_obj.start_time:
            dict_data['start_time'] = datetime.datetime.strptime(str(company_appearance_date_time_obj.start_time),
                                                                 '%H:%M:%S').strftime('%I:%M %p')
        else:
            dict_data['start_time'] = ""
        if company_appearance_date_time_obj.end_time:
            dict_data['end_time'] = datetime.datetime.strptime(str(company_appearance_date_time_obj.end_time),
                                                               '%H:%M:%S').strftime(
                '%I:%M %p')
        else:
            dict_data['end_time'] = ""
        list_data.append(dict_data)
        dict_data = {}
        return JsonResponse({"list_data": list_data})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def edit_company_visiting_selection_precess_date_time(request):
    """
    Edit Company Visiting Selection Precess, date, time Page
    :param request:
    :return:
    """
    try:
        dict_data = {}
        list_data = []
        id = request.POST.get('id')
        company_appearance_date_time_obj = CompanyAppearanceDateTime.objects.get(id=id)

        dict_data['id'] = company_appearance_date_time_obj.id
        dict_data['fk_selection_process_test_id'] = company_appearance_date_time_obj.fk_selection_process_test.id
        dict_data[
            'fk_selection_process_test_name'] = company_appearance_date_time_obj.fk_selection_process_test.test_name
        dict_data['date'] = datetime.datetime.strptime(str(company_appearance_date_time_obj.date), '%Y-%m-%d').strftime(
            '%d-%m-%Y')
        if company_appearance_date_time_obj.start_time:
            dict_data['start_time'] = datetime.datetime.strptime(str(company_appearance_date_time_obj.start_time),
                                                                 '%H:%M:%S').strftime('%I:%M %p')
        else:
            dict_data['start_time'] = ""
        if company_appearance_date_time_obj.end_time:
            dict_data['end_time'] = datetime.datetime.strptime(str(company_appearance_date_time_obj.end_time),
                                                               '%H:%M:%S').strftime(
                '%I:%M %p')
        else:
            dict_data['end_time'] = ""
        list_data.append(dict_data)
        dict_data = {}
        return JsonResponse({"list_data": list_data})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def update_company_visiting_selection_precess_date_time(request):
    """
    Update Company Visiting Selection Precess, date, time
    :param request:
    :return:
    """
    try:
        dict_data = {}
        list_data = []
        company_visiting_selection_process_date_time_id = request.POST.get(
            "company_visiting_selection_process_date_time_id")
        company_visiting_selection_process_test = request.POST.get("company_visiting_selection_process_test")
        company_visited_date = request.POST.get("company_visited_date")
        company_visited_start_time = request.POST.get("company_visited_start_time")
        company_visited_end_time = request.POST.get("company_visited_end_time")

        company_visited_date = datetime.datetime.strptime(str(company_visited_date), '%d-%m-%Y').strftime('%Y-%m-%d')
        if company_visited_start_time:
            company_visited_start_time = datetime.datetime.strptime(str(company_visited_start_time),
                                                                    '%I:%M %p').strftime(
                '%H:%M:%S')
        else:
            company_visited_start_time = None
        if company_visited_end_time:
            company_visited_end_time = datetime.datetime.strptime(str(company_visited_end_time), '%I:%M %p').strftime(
                '%H:%M:%S')
        else:
            company_visited_end_time = None
        company_appearance_date_time_obj = CompanyAppearanceDateTime.objects.get(
            id=company_visiting_selection_process_date_time_id)
        company_appearance_date_time_obj.fk_selection_process_test_id = company_visiting_selection_process_test
        company_appearance_date_time_obj.date = company_visited_date
        company_appearance_date_time_obj.start_time = company_visited_start_time
        company_appearance_date_time_obj.end_time = company_visited_end_time
        company_appearance_date_time_obj.save()

        dict_data['id'] = company_appearance_date_time_obj.id
        dict_data['fk_selection_process_test_id'] = company_appearance_date_time_obj.fk_selection_process_test.id
        dict_data[
            'fk_selection_process_test_name'] = company_appearance_date_time_obj.fk_selection_process_test.test_name
        dict_data['date'] = datetime.datetime.strptime(str(company_appearance_date_time_obj.date), '%Y-%m-%d').strftime(
            '%d-%m-%Y')
        if company_appearance_date_time_obj.start_time:
            dict_data['start_time'] = datetime.datetime.strptime(str(company_appearance_date_time_obj.start_time),
                                                                 '%H:%M:%S').strftime('%I:%M %p')
        else:
            dict_data['start_time'] = ""
        if company_appearance_date_time_obj.end_time:
            dict_data['end_time'] = datetime.datetime.strptime(str(company_appearance_date_time_obj.end_time),
                                                               '%H:%M:%S').strftime(
                '%I:%M %p')
        else:
            dict_data['end_time'] = ""
        list_data.append(dict_data)
        dict_data = {}
        return JsonResponse({"list_data": list_data})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def delete_company_visiting_selection_precess_date_time(request):
    """
    Delete Company Visiting Selection Precess, Date, Time
    :param request:
    :return:
    """
    try:
        id = request.POST.get('id')
        company_appearance_date_time_obj = CompanyAppearanceDateTime.objects.get(id=id)
        company_appearance_date_time_obj.delete()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def add_company_visiting_job_type_package_job_location(request):
    """
    Add Company Visiting Job Type Package Job location
    :param request:
    :return:
    """
    try:
        dict_data = {}
        list_data = []
        job_type_list = []
        job_type_dict = {}
        company_visiting_job_type = request.POST.getlist("company_visiting_job_type[]")
        company_visiting_package = request.POST.get("company_visiting_package")
        company_visiting_job_location = request.POST.get("company_visiting_job_location")

        print("company_visiting_job_type", company_visiting_job_type)
        print("company_visiting_package", company_visiting_package)
        print("company_visiting_job_location", company_visiting_job_location)

        company_appearance_job_type_detail_obj = CompanyAppearanceJobTypeDetail(package=company_visiting_package,
                                                                                job_location=company_visiting_job_location)
        company_appearance_job_type_detail_obj.save()
        for i in company_visiting_job_type:
            company_appearance_job_type_detail_obj.fk_job_type.add(JobType.objects.get(id=i))

        for i in company_appearance_job_type_detail_obj.fk_job_type.all():
            job_type_dict['job_type_id'] = i.id
            job_type_dict['job_type_name'] = i.job_type
            job_type_list.append(job_type_dict)
            job_type_dict = {}

        dict_data['id'] = company_appearance_job_type_detail_obj.id
        dict_data['fk_job_type'] = job_type_list
        dict_data['package'] = company_appearance_job_type_detail_obj.package
        dict_data['job_location'] = company_appearance_job_type_detail_obj.job_location
        list_data.append(dict_data)
        dict_data = {}

        print(list_data)
        return JsonResponse({"list_data": list_data})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def edit_company_visiting_job_type_package_job_location(request):
    """
    Edit Company Visiting Job Type Package Job Location Data
    :param request:
    :return:
    """
    try:
        dict_data = {}
        list_data = []
        job_type_list = []
        job_type_dict = {}
        id = request.POST.get("id")
        company_appearance_job_type_detail_obj = CompanyAppearanceJobTypeDetail.objects.get(id=id)
        for i in company_appearance_job_type_detail_obj.fk_job_type.all():
            job_type_list.append(i.id)

        dict_data['id'] = company_appearance_job_type_detail_obj.id
        dict_data['fk_job_type'] = job_type_list
        dict_data['package'] = company_appearance_job_type_detail_obj.package
        dict_data['job_location'] = company_appearance_job_type_detail_obj.job_location
        list_data.append(dict_data)
        dict_data = {}
        print(list_data)
        return JsonResponse({"list_data": list_data})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def update_company_visiting_job_type_package_job_location(request):
    """
    Update Company Visiting Job Type Package Job Location
    :param request:
    :return:
    """
    try:
        dict_data = {}
        list_data = []
        job_type_list = []
        job_type_dict = {}
        company_visiting_job_type_package_job_location_id = request.POST.get(
            "company_visiting_job_type_package_job_location_id")
        company_visiting_job_type = request.POST.getlist("company_visiting_job_type[]")
        company_visiting_package = request.POST.get("company_visiting_package")
        company_visiting_job_location = request.POST.get("company_visiting_job_location")

        print("company_visiting_job_type_package_job_location_id", company_visiting_job_type_package_job_location_id)
        print("company_visiting_job_type", company_visiting_job_type)
        print("company_visiting_package", company_visiting_package)
        print("company_visiting_job_location", company_visiting_job_location)

        company_appearance_job_type_detail_obj = CompanyAppearanceJobTypeDetail.objects.get(
            id=company_visiting_job_type_package_job_location_id)
        company_appearance_job_type_detail_obj.fk_job_type.clear()
        company_appearance_job_type_detail_obj.package = company_visiting_package
        company_appearance_job_type_detail_obj.job_location = company_visiting_job_location
        company_appearance_job_type_detail_obj.save()
        for i in company_visiting_job_type:
            company_appearance_job_type_detail_obj.fk_job_type.add(JobType.objects.get(id=i))

        for i in company_appearance_job_type_detail_obj.fk_job_type.all():
            job_type_dict['job_type_id'] = i.id
            job_type_dict['job_type_name'] = i.job_type
            job_type_list.append(job_type_dict)
            job_type_dict = {}

        dict_data['id'] = company_appearance_job_type_detail_obj.id
        dict_data['fk_job_type'] = job_type_list
        dict_data['package'] = company_appearance_job_type_detail_obj.package
        dict_data['job_location'] = company_appearance_job_type_detail_obj.job_location
        list_data.append(dict_data)
        dict_data = {}

        print(list_data)
        return JsonResponse({"list_data": list_data})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def delete_company_visiting_job_type_package_job_location(request):
    """
    delete company visiting job type, package, job location
    :param request:
    :return:
    """
    try:
        id = request.POST.get("id")
        company_appearance_job_type_detail_obj = CompanyAppearanceJobTypeDetail.objects.get(id=id)
        company_appearance_job_type_detail_obj.delete()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def add_company_visting_detail(request):
    """
    add company visting detail
    :param request:
    :return:
    """
    try:
        company_id = request.POST.get("company_id")
        company_visiting_interview_address = request.POST.get("company_visiting_interview_address")
        company_visiting_other_detail = request.POST.get("company_visiting_other_detail")
        company_visiting_job_type_package_job_location_list = request.POST.getlist(
            "company_visiting_job_type_package_job_location_list[]")
        company_visiting_date_time_list = request.POST.getlist("company_visiting_date_time_list[]")

        print("company_visiting_job_type_package_job_location_list",
              company_visiting_job_type_package_job_location_list)
        print("company_visiting_date_time_list", company_visiting_date_time_list)

        company_appearance_obj = CompanyAppearance(fk_company_id=company_id,
                                                   company_interview_location=company_visiting_interview_address,
                                                   company_visiting_other_detail=company_visiting_other_detail)
        company_appearance_obj.save()

        for i in company_visiting_job_type_package_job_location_list:
            company_appearance_obj.fk_company_appearance_job_type_detail_list.add(
                CompanyAppearanceJobTypeDetail.objects.get(id=i))

        for j in company_visiting_date_time_list:
            company_appearance_obj.fk_company_appearance_date_time_list.add(CompanyAppearanceDateTime.objects.get(id=j))

        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def edit_visiting_company_detail(request):
    """
    edit visiting company detail Data
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        job_type_detail_list = []
        job_type_detail_dict = {}
        job_type_list = []
        job_type_dict = {}
        selection_list = []
        selection_dict = {}

        id = request.POST.get("id")
        company_appearance_obj = CompanyAppearance.objects.get(id=id)
        dict_data['id'] = company_appearance_obj.id
        dict_data['company_interview_location'] = company_appearance_obj.company_interview_location
        dict_data['company_visiting_other_detail'] = company_appearance_obj.company_visiting_other_detail

        for i in company_appearance_obj.fk_company_appearance_job_type_detail_list.all():
            for j in i.fk_job_type.all():
                job_type_dict['job_type'] = j.job_type
                job_type_dict['job_type_id'] = j.id
                job_type_list.append(job_type_dict)
                job_type_dict = {}
            job_type_detail_dict['fk_job_type'] = job_type_list
            job_type_list = []

            job_type_detail_dict['fk_company_appearance_job_type_detail_list_id'] = i.id
            job_type_detail_dict['package'] = i.package
            job_type_detail_dict['job_location'] = i.job_location
            job_type_detail_list.append(job_type_detail_dict)
            job_type_detail_dict = {}
        dict_data['fk_company_appearance_job_type_detail_list'] = job_type_detail_list

        for i in company_appearance_obj.fk_company_appearance_date_time_list.all():
            selection_dict['fk_company_appearance_date_time_list_id'] = i.id
            selection_dict['date'] = datetime.datetime.strptime(str(i.date), '%Y-%m-%d').strftime('%d-%m-%Y')
            if i.start_time:
                selection_dict['start_time'] = datetime.datetime.strptime(str(i.start_time), '%H:%M:%S').strftime(
                    '%I:%M %p')
            else:
                selection_dict['start_time'] = ""
            if i.end_time:
                selection_dict['end_time'] = datetime.datetime.strptime(str(i.end_time), '%H:%M:%S').strftime(
                    '%I:%M %p')
            else:
                selection_dict['end_time'] = ""
            selection_dict['fk_selection_process_test'] = i.fk_selection_process_test.test_name
            selection_dict['fk_selection_process_test_id'] = i.fk_selection_process_test.id
            selection_list.append(selection_dict)
            selection_dict = {}
        dict_data['fk_company_appearance_date_time_list'] = selection_list
        list_data.append(dict_data)
        dict_data = {}
        print(list_data)
        return JsonResponse({"list_data": list_data})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def update_company_visting_detail(request):
    """
    update company visting detail
    :param request:
    :return:
    """
    try:
        company_id = request.POST.get("company_id")
        company_visiting_id = request.POST.get("company_visiting_id")
        company_visiting_interview_address = request.POST.get("company_visiting_interview_address")
        company_visiting_other_detail = request.POST.get("company_visiting_other_detail")
        company_visiting_job_type_package_job_location_list = request.POST.getlist(
            "company_visiting_job_type_package_job_location_list[]")
        company_visiting_date_time_list = request.POST.getlist("company_visiting_date_time_list[]")

        company_appearance_obj = CompanyAppearance.objects.get(id=company_visiting_id)
        company_appearance_obj.fk_company_id = company_id
        company_appearance_obj.company_interview_location = company_visiting_interview_address
        company_appearance_obj.company_visiting_other_detail = company_visiting_other_detail
        company_appearance_obj.save()
        company_appearance_obj.fk_company_appearance_job_type_detail_list.clear()
        company_appearance_obj.fk_company_appearance_date_time_list.clear()

        for i in company_visiting_job_type_package_job_location_list:
            company_appearance_obj.fk_company_appearance_job_type_detail_list.add(
                CompanyAppearanceJobTypeDetail.objects.get(id=i))

        for j in company_visiting_date_time_list:
            company_appearance_obj.fk_company_appearance_date_time_list.add(CompanyAppearanceDateTime.objects.get(id=j))
        apple_company_appearance_obj = AppleCompanyAppearance.objects.filter(
            fk_company_appearance=company_appearance_obj)
        for j in apple_company_appearance_obj:
            for i in j.fk_company_appearance.fk_company_appearance_date_time_list.all():
                if CompanyAppearanceTestResult.objects.filter(fk_appled_company_appearance_id=j.id,
                                                              fk_user_info_id=j.fk_user_info.id,
                                                              fk_selection_process_test_id=i.fk_selection_process_test.id).exists():
                    pass
                else:
                    company_appearance_test_result_obj = CompanyAppearanceTestResult(
                        fk_appled_company_appearance_id=j.id,
                        fk_user_info_id=j.fk_user_info.id,
                        fk_selection_process_test_id=i.fk_selection_process_test.id)
                    company_appearance_test_result_obj.save()

        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def student_company_appearances(request):
    """
    student company appearances
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            company_appearance_obj = CompanyAppearance.objects.all().order_by('-id')
            company_appearance_past_obj = list(CompanyAppearance.objects.filter(
                fk_company_appearance_date_time_list__date__lte=datetime.datetime.now().strftime(
                    '%Y-%m-%d')).values_list(
                'id', flat=True).distinct())
            company_appearance_upcoming_obj = list(CompanyAppearance.objects.filter(
                fk_company_appearance_date_time_list__date__gt=datetime.datetime.now().strftime(
                    '%Y-%m-%d')).values_list(
                'id', flat=True).distinct())
            apple_company_appearance_obj = list(
                AppleCompanyAppearance.objects.filter(fk_user_info=user_info_obj).values_list(
                    'fk_company_appearance__id',
                    flat=True).distinct())
            print("company_appearance_obj", company_appearance_obj)
            print("company_appearance_past_obj", company_appearance_past_obj)
            print("company_appearance_upcoming_obj", company_appearance_upcoming_obj)
            print("apple_company_appearance_obj", apple_company_appearance_obj)
            return render(request, "placement_student_company_appearance.html",
                          {"user_info_obj": user_info_obj, "company_appearance_obj": company_appearance_obj,
                           "company_appearance_past_obj": company_appearance_past_obj,
                           "company_appearance_upcoming_obj": company_appearance_upcoming_obj,
                           "apple_company_appearance_obj": apple_company_appearance_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def apply_visiting_company_modal_detail(request):
    """
    apply visiting company modal detail Data
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        session = request.session.get('user_id')
        id = request.POST.get("id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            academic_info_obj = AcademicInfo.objects.get(fk_user_info=user_info_obj)
            company_appearance_obj = CompanyAppearance.objects.get(id=id)
            company_obj = Company.objects.get(id=company_appearance_obj.fk_company.id)
            if AppleCompanyAppearance.objects.filter(fk_company_appearance=company_appearance_obj,
                                                     fk_user_info=user_info_obj).exists():
                apple_company_appearance_obj = AppleCompanyAppearance.objects.get(
                    fk_company_appearance=company_appearance_obj, fk_user_info=user_info_obj)
                dict_data['applied_status'] = "Applied"
                dict_data['appled_company_appearance_id'] = apple_company_appearance_obj.id
            else:
                dict_data['applied_status'] = "Not Applied"
                dict_data['appled_company_appearance_id'] = ""
            dict_data['id'] = company_appearance_obj.id
            dict_data['company_name'] = company_obj.company_name
            dict_data['company_main_address'] = company_obj.company_main_address
            dict_data['company_location'] = company_obj.company_location
            dict_data['fk_company_type'] = company_obj.fk_company_type.company_type
            if academic_info_obj.resume:
                dict_data['resume'] = academic_info_obj.resume.url
                dict_data['resume_name'] = str(academic_info_obj.resume.url)[14:]
            else:
                dict_data['resume'] = ""
                dict_data['resume_name'] = ""
            list_data.append(dict_data)
            dict_data = {}
            return JsonResponse({"list_data": list_data})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def apply_visiting_company(request):
    """
    apply visiting company
    :param request:
    :return:
    """
    try:
        modal_company_visiting_id = request.POST.get("modal_company_visiting_id")
        modal_student_resume = request.FILES.get("modal_student_resume")

        print("modal_company_visiting_id", modal_company_visiting_id)
        print("modal_student_resume", modal_student_resume)

        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            academic_info_obj = AcademicInfo.objects.get(fk_user_info=user_info_obj)
            company_appearance_obj = CompanyAppearance.objects.get(id=modal_company_visiting_id)
            company_obj = Company.objects.get(id=company_appearance_obj.fk_company.id)

            if AppleCompanyAppearance.objects.filter(fk_company_appearance=company_appearance_obj,
                                                     fk_user_info=user_info_obj).exists():
                apple_company_appearance_obj = AppleCompanyAppearance.objects.get(
                    fk_company_appearance=company_appearance_obj, fk_user_info=user_info_obj)
                if modal_student_resume:
                    academic_info_obj.resume = modal_student_resume
                    academic_info_obj.save()
                for i in apple_company_appearance_obj.fk_company_appearance.fk_company_appearance_date_time_list.all():
                    if CompanyAppearanceTestResult.objects.filter(
                            fk_appled_company_appearance=apple_company_appearance_obj,
                            fk_user_info=user_info_obj,
                            fk_selection_process_test_id=i.fk_selection_process_test.id).exists():
                        pass
                    else:
                        company_appearance_test_result_obj = CompanyAppearanceTestResult(
                            fk_appled_company_appearance=apple_company_appearance_obj, fk_user_info=user_info_obj,
                            fk_selection_process_test_id=i.fk_selection_process_test.id)
                        company_appearance_test_result_obj.save()
            else:
                apple_company_appearance_obj = AppleCompanyAppearance(fk_company=company_obj,
                                                                      fk_company_appearance_id=modal_company_visiting_id,
                                                                      fk_user_info=user_info_obj,
                                                                      fk_academic_info=academic_info_obj)
                apple_company_appearance_obj.save()
                if modal_student_resume:
                    academic_info_obj.resume = modal_student_resume
                    academic_info_obj.save()
                for i in apple_company_appearance_obj.fk_company_appearance.fk_company_appearance_date_time_list.all():
                    if CompanyAppearanceTestResult.objects.filter(
                            fk_appled_company_appearance=apple_company_appearance_obj,
                            fk_user_info=user_info_obj,
                            fk_selection_process_test_id=i.fk_selection_process_test.id).exists():
                        pass
                    else:
                        company_appearance_test_result_obj = CompanyAppearanceTestResult(
                            fk_appled_company_appearance=apple_company_appearance_obj, fk_user_info=user_info_obj,
                            fk_selection_process_test_id=i.fk_selection_process_test.id)
                        company_appearance_test_result_obj.save()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def cancel_company_registration(request):
    """
    cancel company registration by student
    :param request:
    :return:
    """
    try:
        modal_appledcompanyappearance_id = request.POST.get("modal_appledcompanyappearance_id")
        print("modal_appledcompanyappearance_id", modal_appledcompanyappearance_id)
        apple_company_appearance_obj = AppleCompanyAppearance.objects.get(id=modal_appledcompanyappearance_id)
        apple_company_appearance_obj.delete()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def view_visiting_company_detail(request, id):
    """
    view visiting company detail page
    :param request:
    :param id:
    :return:
    """
    try:
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            print("user_info_obj", user_info_obj)
            company_appearance_obj = CompanyAppearance.objects.filter(id=id)
            companyappearance_get_obj = CompanyAppearance.objects.get(id=id)
            company_obj = Company.objects.get(id=CompanyAppearance.objects.get(id=id).fk_company.id)
            company_appearance_not_apply_obj = list(CompanyAppearance.objects.filter(
                fk_company_appearance_date_time_list__date__lte=datetime.datetime.now().strftime(
                    '%Y-%m-%d')).values_list(
                'id', flat=True).distinct())
            if int(id) in company_appearance_not_apply_obj:
                apply_status = "Not Apply"
            else:
                apply_status = "Apply"
            if AppleCompanyAppearance.objects.filter(fk_company_appearance=companyappearance_get_obj,
                                                     fk_user_info=user_info_obj).exists():
                apple_company_appearance_obj = AppleCompanyAppearance.objects.get(
                    fk_company_appearance=companyappearance_get_obj, fk_user_info=user_info_obj)
                applied_status = "Applied"
                appled_company_appearance_id = apple_company_appearance_obj.id
            else:
                applied_status = "Not Applied"
                appled_company_appearance_id = ""

            print("apply_status", apply_status)
            print("applied_status", applied_status)
            print("appled_company_appearance_id", appled_company_appearance_id)
            return render(request, "placement_student_view_company_appearance_detail.html",
                          {"companyappearance_get_obj": companyappearance_get_obj,
                           "company_appearance_obj": company_appearance_obj, "user_info_obj": user_info_obj,
                           "company_obj": company_obj, "apply_status": apply_status, "applied_status": applied_status,
                           "appled_company_appearance_id": appled_company_appearance_id})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def view_company_appearances_detail(request, id):
    """
    view company appearances detail page
    :param request:
    :param id:
    :return:
    """
    try:
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            company_appearance_obj = CompanyAppearance.objects.get(id=id)
            apple_company_appearance_obj = AppleCompanyAppearance.objects.filter(fk_company_appearance_id=id)
            company_appearance_test_result_obj = CompanyAppearanceTestResult.objects.filter(
                fk_appled_company_appearance__fk_company_appearance__id=id)
            placed_student_count = AppleCompanyAppearance.objects.filter(fk_company_appearance_id=id,
                                                                         placement_status="Placed").count()
            date_list = list(
                CompanyAppearance.objects.filter(id=id).values_list('fk_company_appearance_date_time_list__date',
                                                                    flat=True))
            max_date = max(date_list)
            min_date = min(date_list)
            return render(request, "placement_view_company_appearance_detail.html",
                          {"max_date": max_date, "min_date": min_date, "placed_student_count": placed_student_count,
                           "company_appearance_test_result_obj": company_appearance_test_result_obj,
                           "user_info_obj": user_info_obj,
                           "user_operation_obj": user_operation_obj, "company_appearance_obj": company_appearance_obj,
                           "apple_company_appearance_obj": apple_company_appearance_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def add_test_result_placement(request, id):
    """
    add test result placement page
    :param request:
    :param id:
    :return:
    """
    try:
        session = request.session.get('user_id')
        print("id", id)
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            company_appearance_obj = CompanyAppearance.objects.get(id=id)
            apple_company_appearance_obj = AppleCompanyAppearance.objects.filter(fk_company_appearance_id=id)
            return render(request, "placement_add_test_result.html",
                          {"user_info_obj": user_info_obj, "user_operation_obj": user_operation_obj,
                           "company_appearance_obj": company_appearance_obj,
                           "apple_company_appearance_obj": apple_company_appearance_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_test_result_by_subject(request):
    """
    filter test result by subject page
    :param request:
    :return:
    """
    try:
        test_name = request.POST.get("test_name")
        company_appearance_id = request.POST.get("company_appearance_id")
        company_appearance_obj = CompanyAppearance.objects.get(id=company_appearance_id)
        company_appearance_test_result_obj = CompanyAppearanceTestResult.objects.filter(
            fk_appled_company_appearance__fk_company_appearance__id=company_appearance_id,
            fk_selection_process_test_id=test_name)
        print("company_appearance_test_result_obj", company_appearance_test_result_obj)
        apple_company_appearance_obj = AppleCompanyAppearance.objects.filter(
            fk_company_appearance_id=company_appearance_id)
        render_string = render_to_string("placement_filter_test_result_by_subject.html",
                                         {"company_appearance_test_result_obj": company_appearance_test_result_obj,
                                          "company_appearance_obj": company_appearance_obj,
                                          "apple_company_appearance_obj": apple_company_appearance_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def save_test_result_by_subject(request):
    """
    save test result by subject
    :param request:
    :return:
    """
    try:
        test_name = request.POST.get("test_name")
        test_result = request.POST.get("test_result")
        user_id = request.POST.get("user_id")
        company_appearance_id = request.POST.get("company_appearance_id")
        if CompanyAppearanceTestResult.objects.filter(fk_appled_company_appearance_id=company_appearance_id,
                                                      fk_user_info_id=user_id,
                                                      fk_selection_process_test_id=test_name).exists():
            company_appearance_test_result_obj = CompanyAppearanceTestResult.objects.get(
                fk_appled_company_appearance_id=company_appearance_id, fk_user_info_id=user_id,
                fk_selection_process_test_id=test_name)
            company_appearance_test_result_obj.test_status = test_result
            company_appearance_test_result_obj.save()
        else:
            company_appearance_test_result_obj = CompanyAppearanceTestResult(
                fk_appled_company_appearance_id=company_appearance_id, fk_user_info_id=user_id,
                fk_selection_process_test_id=test_name, test_status=test_result)
            company_appearance_test_result_obj.save()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def save_all_student_test_result_by_subject(request):
    """
    save all student test result by subject
    :param request:
    :return:
    """
    try:
        dict = json.loads(request.POST.get("dict"))
        test_name = request.POST.get("test_name")
        print("dict", dict)
        print("test_name", test_name)
        for i in dict:
            if CompanyAppearanceTestResult.objects.filter(
                    fk_appled_company_appearance_id=i['appled_company_appearance_id'],
                    fk_user_info_id=i['user_id'],
                    fk_selection_process_test_id=test_name).exists():
                company_appearance_test_result_obj = CompanyAppearanceTestResult.objects.get(
                    fk_appled_company_appearance_id=i['appled_company_appearance_id'], fk_user_info_id=i['user_id'],
                    fk_selection_process_test_id=test_name)
                company_appearance_test_result_obj.test_status = i['test_result']
                company_appearance_test_result_obj.save()
            else:
                company_appearance_test_result_obj = CompanyAppearanceTestResult(
                    fk_appled_company_appearance_id=i['appled_company_appearance_id'], fk_user_info_id=i['user_id'],
                    fk_selection_process_test_id=test_name, test_status=i['test_result'])
                company_appearance_test_result_obj.save()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def save_placement_status(request):
    """
    save placement status Placed or Not Placed
    :param request:
    :return:
    """
    try:
        placement_status = request.POST.get("placement_status")
        id = request.POST.get("id")
        apple_company_appearance_obj = AppleCompanyAppearance.objects.get(id=id)
        apple_company_appearance_obj.placement_status = placement_status
        apple_company_appearance_obj.save()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def placement_student_performance(request, id):
    """
    placement student performance
    :param request:
    :param id:
    :return:
    """
    try:
        session = request.session.get('user_id')
        print("id", id)
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            academic_info_obj = AcademicInfo.objects.get(fk_user_info_id=id)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            apple_company_appearance_obj = AppleCompanyAppearance.objects.filter(fk_user_info_id=id)
            placed_company_obj = AppleCompanyAppearance.objects.filter(fk_user_info_id=id, placement_status="Placed")
            company_appearance_test_result_obj = CompanyAppearanceTestResult.objects.filter(fk_user_info_id=id)
            selection_process_test_obj = SelectionProcessTest.objects.all()
            return render(request, "placement_student_performance.html",
                          {"user_info_obj": user_info_obj, "placed_company_obj": placed_company_obj,
                           "academic_info_obj": academic_info_obj, "user_operation_obj": user_operation_obj,
                           "company_appearance_test_result_obj": company_appearance_test_result_obj,
                           "selection_process_test_obj": selection_process_test_obj,
                           "apple_company_appearance_obj": apple_company_appearance_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def download_excel_file(request):
    """
    download excel file
    :param request:
    :return:
    """
    try:
        id = request.POST.get('id')
        if os.path.isfile(settings.BASE_DIR + '/media/Placement_Apply_Student/Student_Apply.csv'):
            os.remove(settings.BASE_DIR + '/media/Placement_Apply_Student/Student_Apply.csv')

        header_fields = ['Name', 'Course', 'Semester', 'Section']
        data_fileds = []
        with open(settings.BASE_DIR + '/media/Placement_Apply_Student/Student_Apply.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(header_fields)
        for i in AppleCompanyAppearance.objects.filter(fk_company_appearance_id=id):
            data_fileds.append(str(i.fk_user_info.first_name) + " " + str(i.fk_user_info.last_name))
            academic_info_obj = AcademicInfo.objects.get(fk_user_info=i.fk_user_info)
            data_fileds.append(str(academic_info_obj.fk_course.course))
            data_fileds.append(str(academic_info_obj.fk_semesters.semester))
            data_fileds.append(str(academic_info_obj.fk_sections.sections))
            with open(settings.BASE_DIR + '/media/Placement_Apply_Student/Student_Apply.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(data_fileds)
            data_fileds = []
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_company_appearances(request):
    """
    filter company appearances
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        filter_company_name = request.POST.get("filter_company_name")
        filter_company_type = request.POST.get("filter_company_type")
        filter_company_location = request.POST.get("filter_company_location")
        filter_job_type = request.POST.get("filter_job_type")
        filter_from_date = request.POST.get("filter_from_date")
        filter_to_date = request.POST.get("filter_to_date")
        if filter_from_date:
            filter_from_date = datetime.datetime.strptime(str(filter_from_date), '%d-%m-%Y').strftime('%Y-%m-%d')
        if filter_to_date:
            filter_to_date = datetime.datetime.strptime(str(filter_to_date), '%d-%m-%Y').strftime('%Y-%m-%d')

        company_obj = "Company.objects"
        company_appearance_obj = "CompanyAppearance.objects"
        company_appearance_job_type_detail_obj = ""
        company_appearance_date_time_obj = ""
        if filter_from_date and filter_to_date:
            company_appearance_date_time_obj = list(
                CompanyAppearanceDateTime.objects.filter(date__range=[filter_from_date, filter_to_date]).values_list(
                    'id', flat=True).distinct())
        elif filter_from_date:
            company_appearance_date_time_obj = list(
                CompanyAppearanceDateTime.objects.filter(date=filter_from_date).values_list('id', flat=True).distinct())
        elif filter_to_date:
            company_appearance_date_time_obj = list(
                CompanyAppearanceDateTime.objects.filter(date=filter_to_date).values_list('id', flat=True).distinct())

        print("company_appearance_date_time_obj", company_appearance_date_time_obj)
        if filter_job_type:
            company_appearance_job_type_detail_obj = list(
                CompanyAppearanceJobTypeDetail.objects.filter(fk_job_type__id=filter_job_type).values_list('id',
                                                                                                           flat=True).distinct())

        if filter_company_name:
            company_obj += ".filter(id=filter_company_name)"
        if filter_company_type:
            company_obj += ".filter(fk_company_type_id=filter_company_type)"

        if company_appearance_job_type_detail_obj:
            company_appearance_obj += ".filter(fk_company_appearance_job_type_detail_list__in=company_appearance_job_type_detail_obj)"
        if company_appearance_date_time_obj:
            company_appearance_obj += ".filter(fk_company_appearance_date_time_list__in=company_appearance_date_time_obj).distinct()"
            company_appearance_list_obj = list(CompanyAppearance.objects.filter(
                fk_company_appearance_date_time_list__in=company_appearance_date_time_obj).values_list('fk_company__id',
                                                                                                       flat=True).distinct())
            print("company_appearance_list_obj",company_appearance_list_obj)
            company_obj += ".filter(id__in=company_appearance_list_obj)"

        if company_obj == "Company.objects":
            company_obj += ".all()"
        if company_appearance_obj == "CompanyAppearance.objects":
            company_appearance_obj += ".all()"

        print(company_appearance_date_time_obj)
        print(company_obj)
        print(company_appearance_obj)

        company_obj = eval(company_obj)
        company_appearance_obj = eval(company_appearance_obj)

        for i in company_appearance_obj:
            print(i.id)
            dict_data['company_appearance_id'] = i.id
            date_list = list(
                CompanyAppearance.objects.filter(id=i.id).values_list('fk_company_appearance_date_time_list__date',
                                                                      flat=True))
            dict_data['max_date'] = max(date_list)
            dict_data['min_date'] = min(date_list)
            list_data.append(dict_data)
            dict_data = {}
        render_string = render_to_string("placement_filter_company_appearance.html",
                                         {"list_data": list_data, "company_obj": company_obj,
                                          "company_appearance_obj": company_appearance_obj})
        return HttpResponse(render_string)




    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def search_student_performance(request):
    """
    search student performance
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            course_obj = Course.objects.all()
            semesters_obj = Semester.objects.all()
            sections_obj = Section.objects.all()
            academic_info_obj = AcademicInfo.objects.filter(fk_user_info__fk_user_type__user_type="Student")
            return render(request, "placement_search_student_performance.html",
                          {"user_info_obj": user_info_obj, "user_operation_obj": user_operation_obj,
                           "course_obj": course_obj,
                           "semesters_obj": semesters_obj, "sections_obj": sections_obj,
                           "academic_info_obj": academic_info_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_search_student_performance(request):
    """
    filter search student performance
    :param request:
    :return:
    """
    try:
        filter_student_name = request.POST.get("filter_student_name")
        filter_course = request.POST.get("filter_course")
        filter_semesters = request.POST.get("filter_semesters")
        filter_section = request.POST.get("filter_section")
        academic_info_obj = "AcademicInfo.objects"
        if filter_student_name:
            academic_info_obj += ".filter(Q(fk_user_info__first_name__icontains=filter_student_name) | Q(fk_user_info__middle_name__icontains=filter_student_name) | Q(fk_user_info__last_name__icontains=filter_student_name),fk_user_info__fk_user_type__user_type='Student')"
        if filter_course:
            academic_info_obj += ".filter(fk_course_id=filter_course)"
        if filter_semesters:
            academic_info_obj += ".filter(fk_semesters__id=filter_semesters)"
        if filter_section:
            academic_info_obj += ".filter(fk_sections_id=filter_section)"
        if academic_info_obj == "AcademicInfo.objects":
            academic_info_obj += ".all()"

        print(academic_info_obj)
        academic_info_obj = eval(academic_info_obj)
        render_string = render_to_string("placement_filter_search_student_performance.html",
                                         {"academic_info_obj": academic_info_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def student_my_performance(request):
    """
    student my performance
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            academic_info_obj = AcademicInfo.objects.get(fk_user_info_id=user_info_obj.id)
            apple_company_appearance_obj = AppleCompanyAppearance.objects.filter(fk_user_info_id=user_info_obj.id)
            placed_company_obj = AppleCompanyAppearance.objects.filter(fk_user_info_id=user_info_obj.id,
                                                                       placement_status="Placed")
            company_appearance_test_result_obj = CompanyAppearanceTestResult.objects.filter(
                fk_user_info_id=user_info_obj.id)
            selection_process_test_obj = SelectionProcessTest.objects.all()
            return render(request, "placement_my_performance.html",
                          {"user_info_obj": user_info_obj, "apple_company_appearance_obj": apple_company_appearance_obj,
                           "company_appearance_test_result_obj": company_appearance_test_result_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')
