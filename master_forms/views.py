from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
import traceback
from authentication.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
        print(error)
        return error
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def subject_views(request):
    """
    Page for master table subject
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            subject_obj = Subject.objects.all()
            course_obj = Course.objects.all()
            semester_obj = Semester.objects.all()
            return render(request, "master_subject.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "subject_obj": subject_obj, "course_obj": course_obj, "semester_obj": semester_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_subject(request):
    """
    Deleting any subject from master table subject
    :param request:
    :return:
    """
    try:
        subject_id = request.POST.get("id")
        print("subject_id",subject_id)
        subject_obj = Subject.objects.get(id=subject_id)
        subject_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_subject(request):
    """
    Editing any details from master table subject
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        id = request.POST.get("id")
        subject_obj = Subject.objects.get(id=id)
        dict_data["id"] = subject_obj.id
        dict_data["fk_course"] = subject_obj.fk_course.id
        dict_data["fk_semester"] = subject_obj.fk_semesters.id
        dict_data["subject"] = subject_obj.subjects
        dict_data["compulsory_attendance"] = subject_obj.compulsory_attendance
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_subject(request):
    """
    Adding new subject in the master table subject
    :param request:
    :return:
    """
    try:
        course = request.POST.get("course")
        semester = request.POST.get("semester")
        subject = request.POST.get("subject")
        compulsory_attendance = request.POST.get("compulsory_attendance")
        subject_obj = Subject(fk_course_id=course, fk_semesters_id=semester, subjects=subject,
                              compulsory_attendance=compulsory_attendance)
        subject_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_subject(request):
    """
    Update any details from master table subject
    :param request:
    :return:
    """
    try:
        subject_id = request.POST.get("subject_id")
        master_edit_course = request.POST.get("edit_course")
        master_edit_semester = request.POST.get("edit_semester")
        master_edit_subject = request.POST.get("edit_subject")
        edit_compulsory_attendance = request.POST.get("edit_compulsory_attendance")
        subjects_obj = Subject.objects.get(id=subject_id)
        subjects_obj.fk_course_id = master_edit_course
        subjects_obj.fk_semesters_id = master_edit_semester
        subjects_obj.subjects = master_edit_subject
        subjects_obj.compulsory_attendance = edit_compulsory_attendance
        subjects_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def course_views(request):
    """
    Page for master table course
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            course_obj = Course.objects.all()
            return render(request, "master_course.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "course_obj": course_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_course(request):
    """
    Deleting any course from master table course
    :param request:
    :return:
    """
    try:
        course_id = request.POST.get("id")
        course_obj = Course.objects.get(id=course_id)
        course_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_course(request):
    """
    Editing any details from master table course
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        course_id = request.POST.get("id")
        course_obj = Course.objects.get(id=course_id)
        dict_data["id"] = course_obj.id
        dict_data["course"] = course_obj.course
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_course(request):
    """
    Adding new course in the master table course
    :param request:
    :return:
    """
    try:
        course = request.POST.get("course")
        course_obj = Course(course=course)
        course_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_course(request):
    """
    Update any details from master table course
    :param request:
    :return:
    """
    try:
        course_id = request.POST.get("course_id")
        course_edit = request.POST.get("edit_course")
        course_obj = Course.objects.get(id=course_id)
        course_obj.course = course_edit
        course_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def stream_or_field(request):
    """
    Page for master table college stream/fields
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            twelveth_or_diploma_obj = TwelvethOrDiploma.objects.all()
            stream_or_field_obj = StreamOrField.objects.all()
            return render(request, "master_stream_or_field.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "twelveth_or_diploma_obj": twelveth_or_diploma_obj,
                           "stream_or_field_obj": stream_or_field_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_stream_or_field(request):
    """
    Deleting any stream/fields from master table college stream/fields
    :param request:
    :return:
    """
    try:
        stream_id = request.POST.get("id")
        stream_or_field_obj = StreamOrField.objects.get(id=stream_id)
        stream_or_field_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_stream_or_field(request):
    """
    Editing any stream/fields details from master table college stream/fields
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        stream_id = request.POST.get("id")
        stream_or_field_obj = StreamOrField.objects.get(id=stream_id)
        dict_data["id"] = stream_or_field_obj.id
        dict_data["fk_twelveth_or_diploma"] = stream_or_field_obj.fk_twelveth_or_diploma.id
        dict_data["stream_or_field_name"] = stream_or_field_obj.stream_or_field_name
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_stream_or_field(request):
    """
    Adding new stream/fields details in the master table college stream/fields
    :param request:
    :return:
    """
    try:
        twelveth_or_diploma = request.POST.get("twelveth_or_diploma")
        stream_or_field_name = request.POST.get("stream_or_field_name")
        stream_or_field_obj = StreamOrField(fk_twelveth_or_diploma_id=twelveth_or_diploma,
                                            stream_or_field_name=stream_or_field_name)
        stream_or_field_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_stream_or_field(request):
    """
    Update any details from master table college stream/fields
    :param request:
    :return:
    """
    try:
        stream_or_field_id = request.POST.get("stream_or_field_id")
        edit_twelveth_or_diploma = request.POST.get("edit_twelveth_or_diploma")
        edit_stream_or_field_name = request.POST.get("edit_stream_or_field_name")
        stream_or_field_obj = StreamOrField.objects.get(id=stream_or_field_id)
        stream_or_field_obj.fk_twelveth_or_diploma_id = edit_twelveth_or_diploma
        stream_or_field_obj.stream_or_field_name = edit_stream_or_field_name
        stream_or_field_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def degree_views(request):
    """
    Page for master table degree
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            degree_obj = Degree.objects.all()
            return render(request, "master_degree.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "degree_obj": degree_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_degree(request):
    """
    Deleting any degree from master table degree
    :param request:
    :return:
    """
    try:
        degree_id = request.POST.get("id")
        degree_obj = Degree.objects.get(id=degree_id)
        degree_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_degree(request):
    """
    Editing any details from master table degree
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        degree_id = request.POST.get("id")
        degree_obj = Degree.objects.get(id=degree_id)
        dict_data["id"] = degree_obj.id
        dict_data["degree"] = degree_obj.degree
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_degree(request):
    """
    Adding new degree in master table degree
    :param request:
    :return:
    """
    try:
        degree = request.POST.get("degree")
        degree_obj = Degree(degree=degree)
        degree_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_degree(request):
    """
    Update any details from master table degree
    :param request:
    :return:
    """
    try:
        degree_id = request.POST.get("degree_id")
        master_edit_degree = request.POST.get("edit_degree")
        degree_obj = Degree.objects.get(id=degree_id)
        degree_obj.degree = master_edit_degree
        degree_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def degree_stream_or_field(request):
    """
    Page for master table Degree Stream/Fields
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            degree_obj = Degree.objects.all()
            degree_stream_or_field_obj = DegreeStreamOrField.objects.all()
            return render(request, "master_degree_stream_field.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "degree_obj": degree_obj,
                           "degree_stream_or_field_obj": degree_stream_or_field_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_degree_stream_or_field(request):
    """
    Deleting any degree Stream/Fields from master table Degree Stream/Fields
    :param request:
    :return:
    """
    try:
        degree_id = request.POST.get("id")
        degree_stream_or_field_obj = DegreeStreamOrField.objects.get(id=degree_id)
        degree_stream_or_field_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_degree_stream_or_field(request):
    """
    Editing any details from master table Degree Stream/Fields
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        degree_id = request.POST.get("id")
        degree_stream_or_field_obj = DegreeStreamOrField.objects.get(id=degree_id)
        dict_data["id"] = degree_stream_or_field_obj.id
        dict_data["fk_degree"] = degree_stream_or_field_obj.fk_degree.id
        dict_data["stream_or_field_name"] = degree_stream_or_field_obj.stream_or_field_name
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_degree_stream_or_field(request):
    """
    Adding new degree Stream/Field in master table Degree Stream/Fields
    :param request:
    :return:
    """
    try:
        degree = request.POST.get("degree")
        stream_or_field_name = request.POST.get("stream_or_field_name")
        degree_stream_or_field_obj = DegreeStreamOrField(fk_degree_id=degree, stream_or_field_name=stream_or_field_name)
        degree_stream_or_field_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_degree_stream_or_field(request):
    """
    Update any details from master table Degree Stream/Fields
    :param request:
    :return:
    """
    try:
        stream_or_field_id = request.POST.get("stream_or_field_id")
        master_edit_degree = request.POST.get("edit_degree")
        edit_stream_or_field_name = request.POST.get("edit_stream_or_field_name")
        degree_stream_or_field_obj = DegreeStreamOrField.objects.get(id=stream_or_field_id)
        degree_stream_or_field_obj.fk_degree_id = master_edit_degree
        degree_stream_or_field_obj.stream_or_field_name = edit_stream_or_field_name
        degree_stream_or_field_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def semester_views(request):
    """
    Page for master table Semester
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            semester_obj = Semester.objects.all()
            return render(request, "master_semesters.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "semesters_obj": semester_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_semester(request):
    """
    Adding new semester in master table Semester
    :param request:
    :return:
    """
    try:
        semester = request.POST.get("semester")
        semester_obj = Semester(semester=semester)
        semester_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_semester(request):
    """
    Editing any details from master table Semester
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        sem_id = request.POST.get("id")
        semester_obj = Semester.objects.get(id=sem_id)
        dict_data["id"] = semester_obj.id
        dict_data["semester"] = semester_obj.semester
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_semester(request):
    """
    Update any details from master table Semester
    :param request:
    :return:
    """
    try:
        semester_id = request.POST.get("semester_id")
        master_edit_semester = request.POST.get("edit_semester")
        semester_obj = Semester.objects.get(id=semester_id)
        semester_obj.semester = master_edit_semester
        semester_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_semester(request):
    """
    Deleting any Semester from master table Semester
    :param request:
    :return:
    """
    try:
        sem_id = request.POST.get("id")
        semester_obj = Semester.objects.get(id=sem_id)
        semester_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def section_view(request):
    """
    Page for master table Section
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            section_obj = Section.objects.all()
            return render(request, "master_sections.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "section_obj": section_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_section(request):
    """
    Adding new section in master table Section
    :param request:
    :return:
    """
    try:
        section = request.POST.get("section")
        section_obj = Section(sections=section)
        section_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_section(request):
    """
    Editing any details from master table Section
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        sec_id = request.POST.get("id")
        section_obj = Section.objects.get(id=sec_id)
        dict_data["id"] = section_obj.id
        dict_data["section"] = section_obj.sections
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_section(request):
    """
    Update any details from master table Section
    :param request:
    :return:
    """
    try:
        section_id = request.POST.get("section_id")
        master_edit_section = request.POST.get("edit_section")
        section_obj = Section.objects.get(id=section_id)
        section_obj.sections = master_edit_section
        section_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_section(request):
    """
    Deleting any section from master table Section
    :param request:
    :return:
    """
    try:
        sec_id = request.POST.get("id")
        section_obj = Section.objects.get(id=sec_id)
        section_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def category_views(request):
    """
    Page for master table Categories
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            category_obj = Category.objects.all()
            return render(request, "master_category.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "category_obj": category_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_category(request):
    """
    Adding new Category in master table Categories
    :param request:
    :return:
    """
    try:
        category = request.POST.get("category")
        category_obj = Category(category=category)
        category_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_category(request):
    """
    Editing any details from master table Categories
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        category_id = request.POST.get("id")
        category_obj = Category.objects.get(id=category_id)
        dict_data["id"] = category_obj.id
        dict_data["category"] = category_obj.category
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_category(request):
    """
    Update any details from master table Categories
    :param request:
    :return:
    """
    try:
        category_id = request.POST.get("category_id")
        master_edit_category = request.POST.get("edit_category")
        category_obj = Category.objects.get(id=category_id)
        category_obj.category = master_edit_category
        category_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_category(request):
    """
    Deleting any Category from master table Categories
    :param request:
    :return:
    """
    try:
        category_id = request.POST.get("id")
        category_obj = Category.objects.get(id=category_id)
        category_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def reserved_category_views(request):
    """
    Page for master table Reserved Categories
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            reserved_obj = Reserved.objects.all()
            return render(request, "master_reserved.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "reserved_obj": reserved_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_reserved_category(request):
    """
    Adding new Category in master table Reserved Categories
    :param request:
    :return:
    """
    try:
        reserved = request.POST.get("reserved")
        reserved_obj = Reserved(reserved=reserved)
        reserved_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_reserved_category(request):
    """
    Editing any details from master table Reserved Categories
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        category_id = request.POST.get("id")
        reserved_obj = Reserved.objects.get(id=category_id)
        dict_data["id"] = reserved_obj.id
        dict_data["category"] = reserved_obj.reserved
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_reserved_category(request):
    """
    Update any details from master table Reserved Categories
    :param request:
    :return:
    """
    try:
        reserved_id = request.POST.get("reserved_id")
        edit_reserved = request.POST.get("edit_reserved")
        reserved_obj = Reserved.objects.get(id=reserved_id)
        reserved_obj.reserved = edit_reserved
        reserved_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_reserved_category(request):
    """
    Deleting any Category from master table Reserved Categories
    :param request:
    :return:
    """
    try:
        category_id = request.POST.get("id")
        reserved_obj = Reserved.objects.get(id=category_id)
        reserved_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def apply_concession(request):
    """
    Page for master table Concession
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            apply_concession_obj = ApplyingConcession.objects.all()
            return render(request, "master_concession.html",
                          {"user_operation_obj": user_operation_obj, "user_operation_obj": user_operation_obj,
                           "applyingconcession_obj": apply_concession_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_concession(request):
    """
    Adding new Cancession in master table Concession
    :param request:
    :return:
    """
    try:
        concession = request.POST.get("concession")
        apply_concession_obj = ApplyingConcession(applying_concession=concession)
        apply_concession_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_concession(request):
    """
    Editing any details from master table Concession
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        concession_id = request.POST.get("id")
        apply_concession_obj = ApplyingConcession.objects.get(id=concession_id)
        dict_data["id"] = apply_concession_obj.id
        dict_data["applying_concession"] = apply_concession_obj.applying_concession
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_concession(request):
    """
    Update any details from master table Concession
    :param request:
    :return:
    """
    try:
        concession_id = request.POST.get("concession_id")
        master_edit_concession = request.POST.get("edit_concession")
        apply_concession_obj = ApplyingConcession.objects.get(id=concession_id)
        apply_concession_obj.applying_concession = master_edit_concession
        apply_concession_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_concession(request):
    """
    Deleting any Concession from master table Concession
    :param request:
    :return:
    """
    try:
        concession_id = request.POST.get("id")
        apply_concession_obj = ApplyingConcession.objects.get(id=concession_id)
        apply_concession_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def caste(request):
    """
    Page for master table Caste
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            cast_obj = Cast.objects.all()
            return render(request, "master_caste.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "cast_obj": cast_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_caste(request):
    """
    Adding new caste in master table Caste
    :param request:
    :return:
    """
    try:
        casts = request.POST.get("casts")
        cast_obj = Cast(cast=casts)
        cast_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_caste(request):
    """
    Editing any details from master table Caste
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        caste_id = request.POST.get("id")
        cast_obj = Cast.objects.get(id=caste_id)
        dict_data["id"] = cast_obj.id
        dict_data["applying_concession"] = cast_obj.cast
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_caste(request):
    """
    Update any details from master table Reserved Caste
    :param request:
    :return:
    """
    try:
        cast_id = request.POST.get("cast_id")
        edit_cast = request.POST.get("edit_cast")
        cast_obj = Cast.objects.get(id=cast_id)
        cast_obj.cast = edit_cast
        cast_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_caste(request):
    """
    Deleting any Caste from master table Reserved Caste
    :param request:
    :return:
    """
    try:
        caste_id = request.POST.get("id")
        cast_obj = Cast.objects.get(id=caste_id)
        cast_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def sub_caste(request):
    """
    Page for master table Sub Caste
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            caste_obj = Cast.objects.all()
            sub_caste_obj = SubCast.objects.all()
            return render(request, "master_subcaste.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "cast_obj": caste_obj,
                           "subcast_obj": sub_caste_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_sub_caste(request):
    """
    Adding new sub caste in master table Sub Caste
    :param request:
    :return:
    """
    try:
        caste = request.POST.get("cast")
        sub_caste = request.POST.get("subcasts")
        sub_caste_obj = SubCast(fk_cast_id=caste, sub_cast=sub_caste)
        sub_caste_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_sub_caste(request):
    """
    Editing any details from master table Sub Caste
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        caste_id = request.POST.get("id")
        sub_caste_obj = SubCast.objects.get(id=caste_id)
        dict_data["id"] = sub_caste_obj.id
        dict_data["fk_cast"] = sub_caste_obj.fk_cast.id
        dict_data["sub_cast"] = sub_caste_obj.sub_cast
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_sub_caste(request):
    """
    Update any details from master table Sub Caste
    :param request:
    :return:
    """
    try:
        sub_caste_id = request.POST.get("sub_caste_id")
        master_edit_caste = request.POST.get("master_edit_caste")
        master_edit_sub_caste = request.POST.get("master_edit_sub_caste")
        sub_caste_obj = SubCast.objects.get(id=sub_caste_id)
        sub_caste_obj.fk_cast_id = master_edit_caste
        sub_caste_obj.sub_cast = master_edit_sub_caste
        sub_caste_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_sub_caste(request):
    """
    Deleting any Sub Caste from master table Sub Caste
    :param request:
    :return:
    """
    try:
        caste_id = request.POST.get("id")
        sub_caste_obj = SubCast.objects.get(id=caste_id)
        sub_caste_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def state(request):
    """
    Page for master table State
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            state_obj = State.objects.all().order_by("state")
            return render(request, "master_state.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "state_obj": state_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_state(request):
    """
    Adding new state in master table State
    :param request:
    :return:
    """
    try:
        master_state = request.POST.get("master_state")
        state_obj = State(state=master_state)
        state_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_state(request):
    """
    Editing any details from master table State
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        state_id = request.POST.get("id")
        state_obj = State.objects.get(id=state_id)
        dict_data["id"] = state_obj.id
        dict_data["state"] = state_obj.state
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_state(request):
    """
    Update any details from master table State
    :param request:
    :return:
    """
    try:
        state_id = request.POST.get("state_id")
        master_edit_state = request.POST.get("master_edit_state")
        state_obj = State.objects.get(id=state_id)
        state_obj.state = master_edit_state
        state_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_state(request):
    """
    Deleting any state from master table state
    :param request:
    :return:
    """
    try:
        delete_id = request.POST.get("id")
        state_obj = State.objects.get(id=delete_id)
        state_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def city_views(request):
    """
    Page for master table city
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            city_list_obj = City.objects.all().order_by("city")
            page = request.GET.get("page", 1)
            paginator = Paginator(city_list_obj, 10)
            try:
                city_obj = paginator.page(page)
            except PageNotAnInteger:
                city_obj = paginator.page(1)
            except EmptyPage:
                city_obj = paginator.page(paginator.num_pages)
            state_obj = State.objects.all()
            return render(request, "master_city.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "city_obj": city_obj,
                           "state_obj": state_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_city(request):
    """
    Adding new city in master table City
    :param request:
    :return:
    """
    try:
        master_state = request.POST.get("master_state")
        city = request.POST.get("city")
        city_obj = City(fk_state_id=master_state, city=city)
        city_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_city(request):
    """
    Editing any details from master table City
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        edit_id = request.POST.get("id")
        city_obj = City.objects.get(id=edit_id)
        dict_data["id"] = city_obj.id
        dict_data["fk_state"] = city_obj.fk_state.id
        dict_data["city"] = city_obj.city
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_city(request):
    """
    Update any details from master table City
    :param request:
    :return:
    """
    try:
        city_id = request.POST.get("city_id")
        master_edit_state = request.POST.get("master_edit_state")
        master_edit_city = request.POST.get("master_edit_city")
        city_obj = City.objects.get(id=city_id)
        city_obj.fk_state_id = master_edit_state
        city_obj.city = master_edit_city
        city_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_city(request):
    """
    Deleting any city from master table City
    :param request:
    :return:
    """
    try:
        delete_id = request.POST.get("id")
        city_obj = City.objects.get(id=delete_id)
        city_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def district(request):
    """
    Page for master table District
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            district_obj = District.objects.all().order_by("district")
            state_obj = State.objects.all()
            return render(request, "master_district.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "district_obj": district_obj, "state_obj": state_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_district(request):
    """
    Adding new district in master table District
    :param request:
    :return:
    """
    try:
        master_state = request.POST.get("master_state")
        master_district = request.POST.get("master_district")
        district_obj = District(fk_state_id=master_state, district=master_district)
        district_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_district(request):
    """
    Editing any details from master table District
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        edit_id = request.POST.get("id")
        district_obj = District.objects.get(id=edit_id)
        dict_data["id"] = district_obj.id
        dict_data["fk_state"] = district_obj.fk_state.id
        dict_data["district"] = district_obj.district
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_district(request):
    """
    Update any details from master table District
    :param request:
    :return:
    """
    try:
        district_id = request.POST.get("district_id")
        master_edit_state = request.POST.get("master_edit_state")
        master_edit_district = request.POST.get("master_edit_district")
        district_obj = District.objects.get(id=district_id)
        district_obj.fk_state_id = master_edit_state
        district_obj.district = master_edit_district
        district_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_district(request):
    """
    Deleting any District from master table District
    :param request:
    :return:
    """
    try:
        delete_id = request.POST.get("id")
        city_obj = District.objects.get(id=delete_id)
        city_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


def academic_session(request):
    """
    Page for master table Academic Session
    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
            academic_session_obj = AcademicSession.objects.all()
            return render(request, "master_academic_session.html",
                          {"user_operation_obj": user_operation_obj, "user_info_obj": user_info_obj,
                           "academic_session_obj": academic_session_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def add_academic_session(request):
    """
    Adding new academic session in master table Academic Session
    :param request:
    :return:
    """
    try:
        academic_session_start_date = request.POST.get("academic_session_start_date")
        academic_session_end_date = request.POST.get("academic_session_end_date")
        if academic_session_start_date:
            academic_session_start_date = datetime.datetime.strptime(
                str(request.POST.get("academic_session_start_date")),
                "%d-%m-%Y").strftime("%Y-%m-%d")
        if academic_session_end_date:
            academic_session_end_date = datetime.datetime.strptime(str(request.POST.get("academic_session_end_date")),
                                                                   "%d-%m-%Y").strftime("%Y-%m-%d")
        academic_session_obj = AcademicSession(start_date=academic_session_start_date,
                                               end_date=academic_session_end_date)
        academic_session_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def edit_academic_session(request):
    """
    Editing any details from master table Academic Session
    :param request:
    :return:
    """
    try:
        list_data = []
        dict_data = {}
        academic_id = request.POST.get("id")
        academic_session_obj = AcademicSession.objects.get(id=academic_id)
        dict_data["id"] = academic_session_obj.id
        dict_data["start_date"] = datetime.datetime.strptime(str(academic_session_obj.start_date), "%Y-%m-%d").strftime(
            "%d-%m-%Y")
        dict_data["end_date"] = datetime.datetime.strptime(str(academic_session_obj.end_date), "%Y-%m-%d").strftime(
            "%d-%m-%Y")
        list_data.append(dict_data)
        return JsonResponse({"list": list_data})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def update_academic_session(request):
    """
    Update any details from master table Academic Session
    :param request:
    :return:
    """
    try:
        academic_session_id = request.POST.get("academic_session_id")
        edit_academic_session_start_date = request.POST.get("edit_academic_session_start_date")
        edit_academic_session_end_date = request.POST.get("edit_academic_session_end_date")
        academic_session_obj = AcademicSession.objects.get(id=academic_session_id)
        if edit_academic_session_start_date:
            academic_session_obj.start_date = datetime.datetime.strptime(str(edit_academic_session_start_date),
                                                                         "%d-%m-%Y").strftime("%Y-%m-%d")
        if edit_academic_session_end_date:
            academic_session_obj.end_date = datetime.datetime.strptime(str(edit_academic_session_end_date),
                                                                       "%d-%m-%Y").strftime("%Y-%m-%d")
        academic_session_obj.save()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")


@csrf_exempt
def delete_academic_session(request):
    """
    Deleting any academic session from master table Academic Session
    :param request:
    :return:
    """
    try:
        academic_id = request.POST.get("id")
        academic_session_obj = AcademicSession.objects.get(id=academic_id)
        academic_session_obj.delete()
        return HttpResponse("success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect("error_handler_500")
