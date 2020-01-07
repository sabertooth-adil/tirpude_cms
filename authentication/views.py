from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import random
from django.conf import settings
from django.core.mail import EmailMessage
import base64
import datetime
import traceback

from authentication.models import UserInfo, AddressDetail, AcademicInfo
from master_forms.models import City, District, SubCast, StreamOrField, DegreeStreamOrField, Course, Semester, Section, \
    Gender, UserType, YearOfAdmission, State, Tehsil, MotherTongue, Religion, BloodGroup, Nationality, Category, \
    Reserved, ApplyingConcession, PhysicallyChallenged, Degree, TwelvethOrDiploma, UserOperation, Subject, Cast


def handler404(request, exception):
    return render(request, "404.html")


def handler400(request, exception):
    return render(request, "400.html")

def error_handler_500(request):
    return render(request,"500.html")

def error_save(error):
    time = str(datetime.datetime.now())
    with open("error_log.txt", "a") as myfile:
        myfile.write(time+"\n")
        myfile.write(error+"\n\n")
    print(error)
    return error


def random_with_n_digits(n):
    """
    Generate random n number digite
    
    """
    try:
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return random.randint(range_start, range_end)
    except Exception as e:
        with open("error_log.text", "a") as myfile:
            myfile.write(e)


@csrf_exempt
def get_city_district_list(request):
    """
        Get Cities and districts list

    :param request:
    :return:
    """
    try:
        state_id = request.POST.get("state_id")
        city_list = list(City.objects.filter(fk_state_id=state_id).values_list("id", "city"))
        district_list = list(District.objects.filter(fk_state_id=state_id).values_list("id", "district"))
        return JsonResponse({"city_list": city_list, "district_list": district_list})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def get_sub_cast_list(request):
    """
        Get sub casts list

    :param request:
    :return:
    """
    try:
        cast = request.POST.get("cast")
        sub_cast_list = list(SubCast.objects.filter(fk_cast_id=cast).values_list("id", "sub_cast"))
        return JsonResponse({"sub_cast_list": sub_cast_list})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def get_stream_or_field_list(request):
    """
        Get streams or fields list of twelveth or diploma

    :param request:
    :return:
    """
    try:
        twelveth_or_diploma = request.POST.get("twelveth_or_diploma")
        stream_or_field_list = list(
            StreamOrField.objects.filter(fk_twelveth_or_diploma_id=twelveth_or_diploma).values_list("id",
                                                                                                    "stream_or_field_name"))
        return JsonResponse({"stream_or_field_list": stream_or_field_list})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def get_degree_stream_or_field_list(request):
    """
        Get streams or fields list of twelveth or diploma

    :param request:
    :return:
    """
    try:
        degree = request.POST.get("degree")
        degree_stream_or_field_list = list(
            DegreeStreamOrField.objects.filter(fk_degree_id=degree).values_list("id", "stream_or_field_name"))
        return JsonResponse({"degree_stream_or_field_list": degree_stream_or_field_list})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def admin_home(request):
    try:
        return render(request, "homepage.html")
    except Exception as e:
        with open("error_log.txt", "a") as myfile:
            myfile.write(e)


def admin_login(request):
    """
        home page view

    :param request:
    :return:
    """
    return render(request, "homepage_login.html")


def admin_signup(request):
    """
        Admin signup page view

    :param request:
    :return:
    """
    try:
        obj_course = Course.objects.all()
        obj_semesters = Semester.objects.all()
        obj_sections = Section.objects.all()
        obj_gender = Gender.objects.all()
        obj_user_type = UserType.objects.all()
        obj_year_of_admission = YearOfAdmission.objects.all()
        return render(request, "homepage_signup.html",
                      {"obj_course": obj_course, "obj_semesters": obj_semesters, "obj_sections": obj_sections,
                       "obj_gender": obj_gender, "obj_user_type": obj_user_type,
                       "obj_year_of_admission": obj_year_of_admission})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def register_user(request):
    """
        Register new user

    :param request:
    :return:
    """
    try:
        registered_as = request.POST.get("registered_as")
        registered_as_text = request.POST.get("registered_as_text")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone_no")
        course = request.POST.get("course")
        admission_year = request.POST.get("admission_year")
        sections = request.POST.get("sections")
        semesters = request.POST.get("semesters")
        gender = request.POST.get("gender")
        password = request.POST.get("password")

        if UserInfo.objects.filter(email=email).exists():
            return JsonResponse({"msg": "Email Already Exists", "status": "0"})
        elif UserInfo.objects.filter(phone_no=phone_no).exists():
            return JsonResponse({"msg": "Phone Number Already Exists", "status": "0"})
        else:
            obj_user_info = UserInfo(fk_user_type_id=registered_as, first_name=first_name, middle_name=middle_name,
                                     last_name=last_name, email=email, phone_no=phone_no, password=password,
                                     fk_gender_id=gender)
            obj_user_info.save()
            obj_address_detail = AddressDetail(fk_user_info_id=obj_user_info.id)
            obj_address_detail.save()
            if registered_as_text == "Student":
                obj_academic_info = AcademicInfo(fk_user_info_id=obj_user_info.id, fk_course_id=course,
                                                 fk_year_of_admission_id=admission_year, fk_sections_id=sections,
                                                 fk_semesters_id=semesters)
                obj_academic_info.save()
            else:
                pass
            request.session["user_id"] = obj_user_info.id
            return JsonResponse({"msg": "Registed Successfully", "status": "1"})
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')

@csrf_exempt
def signup_user(request):
    """
        Login User

    :param request:
    :return:
    """
    try:
        id_username = request.POST.get("id_username")
        id_password = request.POST.get("id_password")
        if UserInfo.objects.filter(email=id_username, password=id_password).exists():
            if UserInfo.objects.filter(email=id_username, password=id_password, status="Active").exists():
                obj_user_info = UserInfo.objects.get(email=id_username, password=id_password)
                request.session["user_id"] = obj_user_info.id
                return HttpResponse("success")
            else:
                return HttpResponse("unauthorized user")
        else:
            return HttpResponse("error")
    except Exception as e:
        return redirect('error_handler_500')

def signout_user(request):
    """
        Sign out user

    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        if session:
            del request.session["user_id"]
            return redirect("/")
        else:
            return redirect("/")
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def profile_user(request):
    """
        User profile page view

    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        state_obj = State.objects.all()
        city_obj = City.objects.all()
        district_obj = District.objects.all()
        tehsil_obj = Tehsil.objects.all()
        gender_obj = Gender.objects.all()
        mother_tongue_obj = MotherTongue.objects.all()
        religion_obj = Religion.objects.all()
        blood_group_obj = BloodGroup.objects.all()
        nationality_obj = Nationality.objects.all()
        category_obj = Category.objects.all()
        reserved_obj = Reserved.objects.all()
        applying_concession_obj = ApplyingConcession.objects.all()
        cast_obj = Cast.objects.all()
        sub_cast_obj = SubCast.objects.all()
        physically_challenged_obj = PhysicallyChallenged.objects.all()
        degree_obj = Degree.objects.all()
        degree_stream_or_field_obj = DegreeStreamOrField.objects.all()
        address_detail_obj = AddressDetail.objects.get(fk_user_info_id=session)
        if session:
            stream_or_field_obj = StreamOrField.objects.all()
            twelveth_or_diploma_obj = TwelvethOrDiploma.objects.all()
            user_info_obj = UserInfo.objects.get(id=session)
            if user_info_obj.fk_user_type.user_type == "Student":
                academic_info_obj = AcademicInfo.objects.get(fk_user_info_id=session)
                return render(request, "student_profile.html",
                              {"user_info_obj": user_info_obj, "academic_info_obj": academic_info_obj,
                               "state_obj": state_obj, "city_obj": city_obj, "gender_obj": gender_obj,
                               "mother_tongue_obj": mother_tongue_obj, "religion_obj": religion_obj,
                               "blood_group_obj": blood_group_obj, "nationality_obj": nationality_obj,
                               "twelveth_or_diploma_obj": twelveth_or_diploma_obj,
                               "stream_or_field_obj": stream_or_field_obj, "district_obj": district_obj,
                               "tehsil_obj": tehsil_obj, "address_detail_obj": address_detail_obj,
                               "category_obj": category_obj, "reserved_obj": reserved_obj,
                               "applying_concession_obj": applying_concession_obj, "cast_obj": cast_obj,
                               "sub_cast_obj": sub_cast_obj, "physically_challenged_obj": physically_challenged_obj,
                               "degree_obj": degree_obj, "degree_stream_or_field_obj": degree_stream_or_field_obj})
            else:
                user_operations_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
                subjects_obj = Subject.objects.all()
                return render(request, "faculty_profile.html",
                              {"user_info_obj": user_info_obj, "subject_obj": subjects_obj, "state_obj": state_obj,
                               "city_obj": city_obj, "gender_obj": gender_obj, "mother_tongue_obj": mother_tongue_obj,
                               "religion_obj": religion_obj, "blood_group_obj": blood_group_obj,
                               "nationality_obj": nationality_obj, "district_obj": district_obj, "tehsil_obj":
                                   tehsil_obj,
                               "address_detail_obj": address_detail_obj, "user_operations_obj": user_operations_obj})
        else:
            return redirect("/")
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def change_password(request):
    """
        When user wants to change his/her account password

    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        if UserInfo.objects.filter(id=session).count() > 0:
            obj = UserInfo.objects.get(id=session)
            if old_password == obj.password:
                obj.password = new_password
                obj.save()
                send_data = {"status": "1", "msg": "Password Changed Successfully!"}
            else:
                send_data = {"status": "0", "msg": "Old Password is Wrong"}
        else:
            send_data = {"status": "0", "msg": "User Not Exists"}
        return JsonResponse(send_data)
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def forgot_password(request):
    """
    Creating new password when user forget the
    password
    :param request:
    :return:
    """
    try:
        input_forget_password = request.POST.get("input_forget_password")
        if UserInfo.objects.filter(email=input_forget_password).exists():
            obj = UserInfo.objects.get(email=input_forget_password)
            new_password = random_with_n_digits(8)
            obj.password = new_password
            obj.save()
            send_psw = str(new_password)
            send_mail = str(input_forget_password)
            subject = "Request for password recovery"
            message = "Hello " + obj.first_name + " " + obj.last_name + ", \nYou have recently requested for forgot " \
                                                                        "password.\n\nYour new password is " \
                      + send_psw + "\n\nThank you."
            from_mail = settings.EMAIL_HOST_USER
            email = EmailMessage(subject, message, to=[send_mail], from_email=from_mail)
            email.send()
            send_data = {"status": "1",
                         "msg": "Your new password has been sent on your registred email id, please check your email"
                                " and re-login"}
        else:
            send_data = {"status": "0", "msg": "Email Not Exists"}
        return JsonResponse(send_data)
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def save_personal_info(request):
    """
        Saving user personal info

    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        user_info_obj = UserInfo.objects.get(id=session)
        address_detail_obj = AddressDetail.objects.get(fk_user_info_id=session)
        user_info_obj.first_name = request.POST.get("first_name")
        user_info_obj.middle_name = request.POST.get("middle_name")
        user_info_obj.last_name = request.POST.get("last_name")
        user_info_obj.phone_no = request.POST.get("phone_no")
        user_info_obj.phone_no2 = request.POST.get("phone_no2")
        user_info_obj.fk_gender_id = request.POST.get("gender")
        user_info_obj.aadhar_no = request.POST.get("aadhar_no")
        user_info_obj.dob = datetime.datetime.strptime(str(request.POST.get("dob_date")), "%d-%m-%Y").strftime("%Y-%m-%d")
        user_info_obj.fk_nationality_id = request.POST.get("nationality")
        user_info_obj.fk_blood_group_id = request.POST.get("blood_group")
        user_info_obj.save()
        address_detail_obj.address = request.POST.get("permanent_address")
        address_detail_obj.fk_city_id = request.POST.get("permanent_city")
        address_detail_obj.fk_state_id = request.POST.get("permanent_state")
        address_detail_obj.fk_district_id = request.POST.get("permanent_district")
        address_detail_obj.tehsil = request.POST.get("permanent_tehsil")
        address_detail_obj.pin_code = request.POST.get("permanent_pincode")
        address_detail_obj.correspondence_address = request.POST.get("correspondence_address")
        address_detail_obj.fk_correspondence_state_id = request.POST.get("correspondence_state")
        address_detail_obj.fk_correspondence_district_id = request.POST.get("correspondence_district")
        address_detail_obj.correspondence_tehsil = request.POST.get("correspondence_tehsil")
        address_detail_obj.fk_correspondence_city_id = request.POST.get("correspondence_city")
        address_detail_obj.correspondence_pin_code = request.POST.get("correspondence_pin_code")
        address_detail_obj.save()
        return HttpResponse("success")
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error500')


@csrf_exempt
def save_other_details(request):
    """
        Saving user personal info

    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        user_info_obj = UserInfo.objects.get(id=session)
        academic_info_obj = AcademicInfo.objects.get(fk_user_info_id=user_info_obj.id)
        academic_info_obj.fk_domicile_of_state_id = request.POST.get("domicile_of_state")
        academic_info_obj.fk_category_id = request.POST.get("category")
        academic_info_obj.fk_reserved_id = request.POST.get("reserved")
        academic_info_obj.fk_applying_concession_id = request.POST.get("applying_for_concession")
        academic_info_obj.fk_cast_id = request.POST.get("cast")
        academic_info_obj.fk_sub_cast_id = request.POST.get("sub_cast")
        academic_info_obj.fk_physically_challenged_id = request.POST.get("physically_challenged")
        academic_info_obj.guardian_name = request.POST.get("guardian_full_name")
        academic_info_obj.occupation_of_guardian = request.POST.get("occupation_of_the_guardian")
        academic_info_obj.annual_income_of_guardian = request.POST.get("annual_income_of_the_guardian")
        academic_info_obj.relationship_with_guardian = request.POST.get("relationship_with_guardian")
        academic_info_obj.guardian_mobile_no = request.POST.get("guardian_mobile_no")
        academic_info_obj.save()
        return HttpResponse("success")
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error500')


@csrf_exempt
def save_academic_details(request):
    """
        Saving user academic details

    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        academic_info_obj = AcademicInfo.objects.get(fk_user_info_id=session)
        academic_info_obj.school_name = request.POST.get("school_name")
        academic_info_obj.school_board = request.POST.get("school_board")
        academic_info_obj.school_place = request.POST.get("school_place")
        academic_info_obj.tenth_year_of_passing = datetime.datetime.strptime(
            str(request.POST.get("date_of_school_passing")),
            "%d-%m-%Y").strftime("%Y-%m-%d")
        academic_info_obj.tenth_marks = request.POST.get("school_total_marks")
        academic_info_obj.tenth_out_of = request.POST.get("school_marks_out_of")
        academic_info_obj.school_percentage = request.POST.get("school_percentage")

        academic_info_obj.fk_twelveth_or_diploma_id = request.POST.get("twelveth_or_diploma")
        academic_info_obj.college_name = request.POST.get("college_name")
        academic_info_obj.college_board_or_university = request.POST.get("college_board_or_university")
        academic_info_obj.fk_stream_or_field_id = request.POST.get("college_stream_or_field")
        academic_info_obj.college_place = request.POST.get("college_place")
        academic_info_obj.college_date_of_passing = datetime.datetime.strptime(
            str(request.POST.get("college_date_of_passing")),
            "%d-%m-%Y").strftime("%Y-%m-%d")
        academic_info_obj.college_total_marks = request.POST.get("college_total_marks")
        academic_info_obj.college_marks_out_of = request.POST.get("college_marks_out_of")
        academic_info_obj.college_percentage = request.POST.get("college_percentage")
        degree = request.POST.get("degree")
        if degree:
            academic_info_obj.fk_degree_id = degree
        academic_info_obj.degree_college_name = request.POST.get("degree_college_name")
        academic_info_obj.degree_college_board_or_university = request.POST.get("degree_college_board_or_university")
        degree_college_stream_or_field = request.POST.get("degree_college_stream_or_field")
        if degree_college_stream_or_field:
            academic_info_obj.fk_degree_stream_or_field_id = degree_college_stream_or_field
        academic_info_obj.degree_college_place = request.POST.get("degree_college_place")
        degree_college_date_of_passing = request.POST.get("degree_college_date_of_passing")
        if degree_college_date_of_passing:
            academic_info_obj.degree_college_date_of_passing = datetime.datetime.strptime(
                str(request.POST.get("degree_college_date_of_passing")), "%d-%m-%Y").strftime("%Y-%m-%d")
        degree_college_total_marks = request.POST.get("degree_college_total_marks")
        if degree_college_total_marks:
            academic_info_obj.degree_college_total_marks = request.POST.get("degree_college_total_marks")
        degree_college_marks_out_of = request.POST.get("degree_college_marks_out_of")
        if degree_college_marks_out_of:
            academic_info_obj.degree_college_marks_out_of = request.POST.get("degree_college_marks_out_of")
        degree_college_percentage = request.POST.get("degree_college_percentage")
        if degree_college_percentage:
            academic_info_obj.degree_college_percentage = request.POST.get("degree_college_percentage")
        academic_info_obj.save()
        return HttpResponse("success")
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error500')


@csrf_exempt
def save_user_profile_pic(request):
    """
        Saving user profile pic

    :param request:
    :return:
    """
    try:
        session = request.session.get("user_id")
        user_info_obj = UserInfo.objects.get(id=session)
        company_logo_file = request.FILES.get("company_logo_file")
        if company_logo_file:
            user_info_obj.profile_image = company_logo_file
        user_info_obj.save()
        return redirect("profile_user")
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error500')


def upload_profile(img):
    """
    Upload user profile pic
    :param img:
    :return:
    """
    try:
        current = str(datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S"))
        path = settings.BASE_DIR + "/media/"
        img_n = "profile_images/" + "Profile_" + current + ".jpg"
        destination = open(path + img_n, "wb")
        img = img.split("base64")[1]
        destination.write(base64.b64decode(img))
        destination.close()
        return img_n
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error500')


@csrf_exempt
def update_profile_picture(request):
    """
        Updating user profile pic

    :param request:
    :return:
    """
    try:
        base64string = request.POST.get("base64string")
        session = request.session.get("user_id")
        user_info_obj = UserInfo.objects.get(id=session)
        user_info_obj.profile_image = upload_profile(base64string)
        user_info_obj.save()
        return HttpResponse("success")
    except Exception as e:
        error_save(str(traceback.format_exc()))
        return redirect('error500')
