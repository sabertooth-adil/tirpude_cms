from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils import timezone
import pandas as pd

import datetime
from .models import *
import traceback

from authentication.models import UserInfo, AcademicInfo
from master_forms.models import Semester, Section, Course, UserOperation


def error_save(error):
    """
    Redirecting to error page
    :param error:
    :return:
    """
    time = str(datetime.datetime.now())
    with open("error_log.txt", "a") as my_file:
        my_file.write(time + "\n")
        my_file.write(error + "\n\n")
    print(error)
    return error


@csrf_exempt
def aptitude_test(request):
    """
    Faculty Aptitude Test page view
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            dict_data = {}
            my_list_data = []
            test_obj = AptitudeSet.objects.all().order_by('schedule')
            section_obj = Section.objects.all()
            semesters_obj = Semester.objects.all()
            course_obj = Course.objects.all()
            faculty_obj = UserInfo.objects.filter(fk_user_type__user_type="Faculty")
            time_now = timezone.now() + timezone.timedelta(hours=5.5)
            time_extend = time_now + timezone.timedelta(hours=1)

            for i in AptitudeSet.objects.all():
                try:
                    print((i.schedule < time_now) and (i.time_extend > time_now))
                    if (i.schedule < time_now) and (i.time_extend > time_now):
                        AptitudeSet.objects.filter(id=i.id).update(status="Active")
                    elif (i.schedule < time_now) and (i.time_extend < time_now):
                        AptitudeSet.objects.filter(id=i.id).update(status="Attempted")
                except:
                    pass

            if user_info_obj.fk_user_type.user_type == "Faculty":
                user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
                for i in test_obj:
                    dict_data['id'] = i.id
                    dict_data['total'] = AllottedQuestion.objects.filter(fk_aptitude_set_id=i.id).count()
                    my_list_data.append(dict_data)
                    dict_data = {}
                return render(request, "aptitude_test.html",
                              {"user_operation_obj": user_operation_obj, "test_obj": test_obj, "my_list": my_list_data,
                               "user_info_obj": user_info_obj,
                               "section_obj": section_obj, "semesters_obj": semesters_obj, "course_obj": course_obj,
                               "faculty_obj": faculty_obj})
            else:

                for i in test_obj:
                    dict_data['id'] = i.id
                    dict_data['total'] = AllottedQuestion.objects.filter(fk_aptitude_set_id=i.id).count()
                    my_list_data.append(dict_data)
                    dict_data = {}
                time_dict = {}
                timelist = []
                for i in test_obj:
                    time_dict['id'] = i.id
                    if i.schedule:
                        time_dict['time'] = i.schedule.strftime("%Y-%m-%d %H:%M")
                    else:
                        time_dict['time'] = ""
                    timelist.append(time_dict)
                    time_dict = {}

                aptitudescore_obj = AptitudeTestScore.objects.filter(fk_user_info_id=session)
                print("aptitudescore ", aptitudescore_obj)
                return render(request, "student_aptitude.html",
                              {"test_obj": test_obj, "my_list": my_list_data, "time_now": time_now,
                               "time_extend": time_extend, "aptitudescore_obj": aptitudescore_obj, "timelist": timelist,
                               "user_info_obj": user_info_obj})
        else:
            return redirect("/")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def aptitude_test_details(request):
    """
    Saving Aptitude test details
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        test_name = request.POST.get("test_name")
        # question_type = request.POST.get("question_type")
        test_id = request.POST.get("test_id")
        test_info = request.POST.get("test_info")
        schedule = request.POST.get("schedule")
        test_duration = request.POST.get("test_duration")
        course = request.POST.get("course")
        sem = request.POST.get("sem")
        section = request.POST.get("section")
        test_obj = AptitudeSet.objects.all()
        try:
            time_extend = pd.to_datetime(schedule) + pd.Timedelta(minutes=int(test_duration))
            schedule = pd.to_datetime(schedule)
            if len(str(schedule)) < 5:
                schedule = None
                time_extend = None
        except:
            time_extend = None

        print("Time extend ", time_extend)

        if not schedule:
            schedule = None
        if not course:
            course = None
        if not sem:
            sem = None
        if not section:
            section = None

        # if test id is 1 ,create new test.
        if test_id == "1":
            if AptitudeSet.objects.filter(test_name=test_name, schedule=schedule, fk_course_id=course,
                                          fk_semesters_id=sem,
                                          fk_sections_id=section).exists():
                render_string = render_to_string("aptitidetestmaster_div.html", {"test_obj": test_obj})
                return JsonResponse({"render_string": render_string, "id": "0", "status": "0"})

            else:
                aptitude_set_obj = AptitudeSet(test_name=test_name,
                                               test_info=test_info,
                                               test_duration=test_duration,
                                               schedule=schedule,
                                               question_type="Objective",
                                               status="Unassigned",
                                               time_extend=time_extend,
                                               fk_course_id=course,
                                               fk_semesters_id=sem,
                                               fk_sections_id=section,
                                               fk_faculty_id=session)
                aptitude_set_obj.save()

                # question_obj = AptitudeQuestion.objects.filter(fk_aptitude_set="1")
                AllottedQuestion.objects.filter(fk_aptitude_set="1").update(fk_aptitude_set=aptitude_set_obj.id)
                try:
                    test_active = AptitudeSet.objects.get(id=aptitude_set_obj.id).schedule > (
                            timezone.now() + timezone.timedelta(hours=5.5) - timezone.timedelta(minutes=1))
                except:
                    test_active = False

                print("Test Active is ", test_active)

                if test_active:
                    AptitudeSet.objects.filter(id=aptitude_set_obj.id).update(status="Scheduled")

                render_string = render_to_string("aptitidetestmaster_div.html", {"test_obj": test_obj})
                return JsonResponse({"render_string": render_string, "id": aptitude_set_obj.id, "status": "1"})

        # If test id is not 1 it will update the test of given id.
        else:
            aptitude_set_obj = AptitudeSet.objects.get(id=test_id)
            aptitude_set_obj.test_name = test_name
            aptitude_set_obj.test_info = test_info
            aptitude_set_obj.test_duration = test_duration
            aptitude_set_obj.schedule = schedule
            aptitude_set_obj.time_extend = time_extend
            aptitude_set_obj.fk_course_id = course
            aptitude_set_obj.fk_sections_id = section
            aptitude_set_obj.fk_semesters_id = sem
            aptitude_set_obj.save()
            AllottedQuestion.objects.filter(fk_aptitude_set=test_id).delete()
            AllottedQuestion.objects.filter(fk_aptitude_set="1").update(fk_aptitude_set=test_id)
            try:
                test_active = AptitudeSet.objects.get(id=aptitude_set_obj.id).schedule > (
                        timezone.now() + timezone.timedelta(hours=5.5) - timezone.timedelta(minutes=1))
            except:
                test_active = False
            if test_active:
                print("Test_active")
                AptitudeSet.objects.filter(id=test_id).update(status="Scheduled")

            render_string = render_to_string("aptitidetestmaster_div.html", {"test_obj": test_obj})
            return JsonResponse({"render_string": render_string, "id": aptitude_set_obj.id, "status": "1"})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def delete_master_aptitude_details(request):
    """
    Delete aptitude test details
    :param request:
    :return:
    """
    try:
        test_id = request.POST.get("id")
        aptitude_set_obj = AptitudeSet.objects.get(id=test_id)
        aptitude_set_obj.delete()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def edit_master_aptitude_details(request):
    """
    Edit aptitude test details
    :param request:
    :return:
    """
    try:
        test_id = request.POST.get("id")
        edit_view = request.POST.get("edit_view")
        test_obj = AptitudeSet.objects.all()
        aptitude_set_obj = AptitudeSet.objects.get(id=test_id)
        section_obj = Section.objects.all()
        semesters_obj = Semester.objects.all()
        course_obj = Course.objects.all()
        faculty_obj = UserInfo.objects.filter(fk_user_type__user_type="Faculty")

        if test_id == "1":
            temp_questions = AllottedQuestion.objects.filter(fk_aptitude_set_id=test_id)
            temp_questions.delete()

        AllottedQuestion.objects.filter(fk_aptitude_set="1").delete()
        question_obj = AllottedQuestion.objects.filter(fk_aptitude_set_id=test_id)

        for i in question_obj:
            question = AllottedQuestion.objects.get(id=i.id)
            question.id = None
            question.fk_aptitude_set_id = "1"
            question.save()

        dict_data = {}
        my_list_data = []
        for i in test_obj:
            dict_data['id'] = i.id
            dict_data['total'] = AllottedQuestion.objects.filter(fk_aptitude_set_id=i.id).count()
            my_list_data.append(dict_data)
            dict_data = {}

        question_obj = AllottedQuestion.objects.filter(fk_aptitude_set_id="1")

        render_string = render_to_string("edit_questions.html",
                                         {"aptitude_set_obj": aptitude_set_obj, "faculty_obj": faculty_obj,
                                          "question_obj": question_obj, "my_list": my_list_data,
                                          "test_obj": test_obj, "section_obj": section_obj,
                                          "semesters_obj": semesters_obj, "course_obj": course_obj,
                                          "edit_view": edit_view})
        return JsonResponse({"render_string": render_string, "id": aptitude_set_obj.id})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def add_question(request):
    """
    Add Question in aptitude test
    :param request:
    :return:
    """
    try:
        question_type = request.POST.get('question_type')
        aptitude_id = request.POST.get("aptitude_id")
        question = request.POST.get("question")
        option_a = request.POST.get("optionA")
        option_b = request.POST.get("optionB")
        option_c = request.POST.get("optionC")
        option_d = request.POST.get("optionD")
        answer = request.POST.get("que_answer")
        solution = request.POST.get("solution")
        key = request.POST.get("key")
        questionid = request.POST.get("questionid")
        print(key)
        if key == "Update":
            print("key", key)
            if request.method == 'POST':
                apt_question = AptitudeQuestion(questions=question,
                                                option_a=option_a,
                                                option_b=option_b,
                                                option_c=option_c,
                                                option_d=option_d,
                                                answer=answer,
                                                solution=solution)
                apt_question.save()

                AllottedQuestion.objects.filter(fk_aptitude_set="1",
                                                fk_question=questionid).update(fk_question=apt_question.id)
        else:
            print("key", key)
            if request.method == 'POST':
                apt_question = AptitudeQuestion(questions=question,
                                                option_a=option_a,
                                                option_b=option_b,
                                                option_c=option_c,
                                                option_d=option_d,
                                                answer=answer,
                                                solution=solution)
                apt_question.save()

                allotedquestion_obj = AllottedQuestion(fk_aptitude_set_id="1",
                                                       fk_question_id=apt_question.id)
                allotedquestion_obj.save()

        question_obj = AllottedQuestion.objects.filter(fk_aptitude_set_id="1")
        print(question_obj)

        if question_type == "Objective":
            render_string = render_to_string("aptitude_question_list.html", {"question_obj": question_obj})
            return HttpResponse(render_string)
        else:
            render_string = render_to_string("subjective_question_list.html", {"question_obj": question_obj})
            return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def edit_question(request):
    """
    Edit Question
    :param request:
    :return:
    """
    try:
        question_id = request.POST.get("id")
        question_obj = AptitudeQuestion.objects.get(id=question_id)
        return JsonResponse({"question": question_obj.questions, "optionA": question_obj.option_a,
                             "optionB": question_obj.option_b, "optionC": question_obj.option_c,
                             "optionD": question_obj.option_d, "answer": question_obj.answer})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def delete_aptitude_question(request):
    """
    Delete Question
    :param request:
    :return:
    """
    try:
        question_id = request.POST.get("id")
        question_obj = AllottedQuestion.objects.get(id=question_id)
        question_obj.delete()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def select_question(request):
    """
    Select Question from other aptitude test
    :param request:
    :return:
    """
    try:
        test_id = request.POST.get("test_id")
        question_obj = AllottedQuestion.objects.filter(fk_aptitude_set_id=test_id)
        question_type = AptitudeSet.objects.get(id=test_id).question_type
        render_string = render_to_string("select_questions.html",
                                         {"question_obj": question_obj, "question_type": question_type})
        return JsonResponse({"render_string": render_string})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def add_selected_question(request):
    """
    Add selected question in current aptitude test
    :param request:
    :return:
    """
    try:
        id_list = request.POST.getlist("id_list[]")
        aptitude_id = request.POST.get("aptitude_id")
        print(len(id_list))
        for i in id_list:
            question = AllottedQuestion.objects.get(id=i)
            print(question.id)
            question.id = None
            question.fk_aptitude_set_id = "1"
            question.save()

        question_obj = AllottedQuestion.objects.filter(fk_aptitude_set_id="1")

        render_string = render_to_string("aptitude_question_list.html", {"question_obj": question_obj})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def start_aptitude_test(request, id):
    """
    start
    :param request:
    :param id:
    :return:
    """
    try:
        session = request.session.get('user_id')
        user_info_obj = UserInfo.objects.get(id=session)
        time_now = timezone.now() + timezone.timedelta(hours=5.5)

        aptitude_obj = AptitudeSet.objects.get(id=id)
        question_obj = AllottedQuestion.objects.filter(fk_aptitude_set_id=id)

        if AptitudeSession.objects.filter(fk_user_info_id=session, fk_aptitude_set_id=id, status="active"):
            time_now = AptitudeSession.objects.filter(fk_user_info_id=session, fk_aptitude_set_id=aptitude_obj.id)[
                0].time_start
            duration = time_now + timezone.timedelta(minutes=int(aptitude_obj.test_duration))
            apt_session_obj = AptitudeSession.objects.get(fk_user_info_id=session, fk_aptitude_set_id=aptitude_obj.id,
                                                          status="active")
            student_apt_answer_obj = StudentAptitudeAnswer.objects.filter(fk_aptitude_session_id=apt_session_obj.id)
            print(student_apt_answer_obj)
        else:
            duration = time_now + timezone.timedelta(minutes=int(aptitude_obj.test_duration))
            apt_session = AptitudeSession(fk_aptitude_set_id=id,
                                          fk_user_info_id=session,
                                          time_start=time_now,
                                          status="active")
            apt_session.save()

            for i in question_obj:
                student_apt_answer = StudentAptitudeAnswer(fk_aptitude_session_id=apt_session.id,
                                                           fk_aptitude_question_id=i.fk_question.id)
                student_apt_answer.save()

            apt_session_obj = apt_session
            student_apt_answer_obj = StudentAptitudeAnswer.objects.filter(fk_aptitude_session_id=apt_session_obj.id)
        duration = duration.strftime("%Y-%m-%d %H:%M")
        return render(request, "student_aptitude_test.html",
                      {"aptitude_obj": aptitude_obj, "question_obj": question_obj,
                       "duration": duration, "apt_session_obj": apt_session_obj,
                       "student_apt_answer_obj": student_apt_answer_obj,
                       "user_info_obj": user_info_obj})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def select_answer(request):
    """
    Select objective answer in aptitude test
    :param request:
    :return:
    """
    try:
        apt_session_id = request.POST.get('apt_session_id')
        question_id = request.POST.get('question_id')
        answer = request.POST.get('answer')
        aptitude_test_id = request.POST.get('aptitude_test_id')
        if StudentAptitudeAnswer.objects.filter(fk_aptitude_session_id=apt_session_id,
                                                fk_aptitude_question_id=question_id):
            StudentAptitudeAnswer.objects.filter(fk_aptitude_session_id=apt_session_id,
                                                 fk_aptitude_question_id=question_id).update(answer=answer)
        else:
            student_apt_answer = StudentAptitudeAnswer(fk_aptitude_session_id=apt_session_id,
                                                       fk_aptitude_test_id=aptitude_test_id,
                                                       fk_aptitude_question_id=question_id,
                                                       answer=answer)
            student_apt_answer.save()
        count = StudentAptitudeAnswer.objects.filter(fk_aptitude_session_id=apt_session_id,
                                                     answer__isnull=False).count()
        return JsonResponse({"questions_attempt": count})
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def submit_aptitude_test(request):
    """
    Submit aptitude test
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        apt_session_id = request.POST.get('apt_session_id')
        aptitude_id = request.POST.get('aptitude_id')

        student_apt_answer_obj = StudentAptitudeAnswer.objects.filter(fk_aptitude_session_id=apt_session_id)
        AptitudeSession.objects.filter(id=apt_session_id).update(status="Inactive")

        score = 0
        for i in student_apt_answer_obj:
            if i.answer == i.fk_aptitude_question.answer:
                score += 1

        percent = (score / student_apt_answer_obj.count()) * 100

        out_of = AllottedQuestion.objects.filter(fk_aptitude_set_id=aptitude_id).count()
        print("aptitude_id ", aptitude_id)
        print("out of ", out_of)
        aptitudescore_obj = AptitudeTestScore(fk_aptitude_session_id=apt_session_id,
                                              fk_user_info_id=session,
                                              fk_aptitude_test_id=aptitude_id,
                                              score=score,
                                              out_of=out_of,
                                              percent=percent)
        aptitudescore_obj.save()

        return HttpResponse("Success")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def aptitude_score(request):
    """
    Aptitude score page view
    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        if session:
            user_info_obj = UserInfo.objects.get(id=session)
            aptitude_set_obj = AptitudeSet.objects.filter(status="Attempted").order_by('schedule')
            section_obj = Section.objects.all()
            semesters_obj = Semester.objects.all()
            course_obj = Course.objects.all()
            faculty_obj = UserInfo.objects.filter(fk_user_type__user_type="Faculty")
            dict_data = {}
            my_list_data = []
            time_now = timezone.now() + timezone.timedelta(hours=5.5)

            for i in AptitudeSet.objects.all():
                try:
                    print((i.schedule < time_now) and (i.time_extend > time_now))
                    if (i.schedule < time_now) and (i.time_extend > time_now):
                        AptitudeSet.objects.filter(id=i.id).update(status="Active")
                    elif (i.schedule < time_now) and (i.time_extend < time_now):
                        AptitudeSet.objects.filter(id=i.id).update(status="Attempted")
                except:
                    pass

            if user_info_obj.fk_user_type.user_type == "Faculty":
                user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
                for i in aptitude_set_obj:
                    dict_data['id'] = i.id
                    dict_data['total'] = AptitudeTestScore.objects.filter(fk_aptitude_test_id=i.id).count()
                    my_list_data.append(dict_data)
                    dict_data = {}
                return render(request, "aptitude_score.html",
                              {"user_operation_obj": user_operation_obj, "AptitudeSet_obj": aptitude_set_obj,
                               "my_list": my_list_data, "section_obj": section_obj,
                               "semesters_obj": semesters_obj,
                               "course_obj": course_obj, "user_info_obj": user_info_obj,
                               "faculty_obj": faculty_obj})

            else:
                aptitudescore_obj = AptitudeTestScore.objects.filter(fk_user_info=session)
                return render(request, "student_score.html", {"aptitudescore_obj": aptitudescore_obj,
                                                              "AptitudeSet_obj": aptitude_set_obj,
                                                              "user_info_obj": user_info_obj})
        else:
            return redirect("/")
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def student_score_list(request):
    """
    Student score list page view
    :param request:
    :return:
    """
    try:
        score_id = request.POST.get('test_id')
        academic_obj = AcademicInfo.objects.all()
        aptitude_score_obj = AptitudeTestScore.objects.filter(fk_aptitude_test_id=score_id)

        render_string = render_to_string("student_score_list.html", {"aptitudescore_obj": aptitude_score_obj,
                                                                     "academic_obj": academic_obj})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def view_student_answer(request):
    """
    View answer which was selected by student
    in aptitude test
    :param request:
    :return:
    """
    try:
        score_id = request.POST.get('student_score_id')
        aptitude_session_id = AptitudeTestScore.objects.get(id=score_id).fk_aptitude_session_id
        student_apt_answer_obj = StudentAptitudeAnswer.objects.filter(fk_aptitude_session_id=aptitude_session_id)

        question_obj = AptitudeQuestion.objects.all()

        render_string = render_to_string("student_select_answer.html",
                                         {"student_apt_answer_obj": student_apt_answer_obj,
                                          "question_obj": question_obj})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_publish_list(request):
    """
    Filtering publish test on aptitude test score page
    :param request:
    :return:
    """
    try:
        course = request.POST.get("course")
        sem = request.POST.get("sem")
        section = request.POST.get("section")
        faculty = request.POST.get("faculty")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        dict_data = {}
        mylist_data = []

        if start_date:
            start_date = datetime.datetime.strptime(str(request.POST.get("start_date")), '%d/%m/%Y').strftime('%Y-%m-%d')
        if end_date:
            end_date = datetime.datetime.strptime(str(request.POST.get("end_date")), '%d/%m/%Y').strftime('%Y-%m-%d')

        filter_str = "AptitudeSet.objects.filter(status='Attempted')"
        if sem:
            filter_str += ".filter(fk_semesters_id=sem)"
        if course:
            filter_str += ".filter(fk_course_id=course)"
        if faculty:
            filter_str += ".filter(fk_faculty_id=faculty)"
        if section:
            filter_str += ".filter(fk_sections_id=section)"
        if start_date:
            filter_str += ".filter(schedule__gte=start_date)"
        if end_date:
            filter_str += ".filter(schedule__lte=end_date)"
        if filter_str == "AptitudeSet.objects":
            filter_str += ".all()"

        publish_test_obj = eval(filter_str)

        for i in publish_test_obj:
            dict_data['id'] = i.id
            dict_data['total'] = AptitudeTestScore.objects.filter(fk_aptitude_test_id=i.id).count()
            mylist_data.append(dict_data)
            dict_data = {}

        render_string = render_to_string("publish_test_list.html", {"publish_test_obj": publish_test_obj,
                                                                    "mylist": mylist_data})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_test_list(request):
    """
    Filtering aptitude test on main aptitude test page
    :param request:
    :return:
    """
    session = request.session.get('user_id')
    try:
        user_info_obj = UserInfo.objects.get(id=session)
        user_operations_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        course = request.POST.get("course")
        sem = request.POST.get("sem")
        section = request.POST.get("section")
        faculty = request.POST.get("faculty")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        dict_data = {}
        mylist_data = []

        if start_date:
            start_date = datetime.datetime.strptime(str(request.POST.get("start_date")), '%d/%m/%Y').strftime('%Y-%m-%d')

        if end_date:
            end_date = datetime.datetime.strptime(str(request.POST.get("end_date")), '%d/%m/%Y').strftime('%Y-%m-%d')

        filter_str = "AptitudeSet.objects.filter(status='Attempted')"
        if sem:
            filter_str += ".filter(fk_semesters_id=sem)"
        if course:
            filter_str += ".filter(fk_course_id=course)"
        if faculty:
            filter_str += ".filter(fk_faculty_id=faculty)"
        if section:
            filter_str += ".filter(fk_sections_id=section)"
        if start_date:
            filter_str += ".filter(schedule__gte=start_date)"
        if end_date:
            filter_str += ".filter(schedule__lte=end_date)"
        if filter_str == "AptitudeSet.objects":
            filter_str += ".all()"

        publish_test_obj = eval(filter_str)

        # publish_test_obj = AptitudeSet.objects.filter(fk_faculty_id=faculty, fk_course_id=course, fk_semesters_id=sem,
        # schedule__gte=start_date,schedule__lte=end_date)

        for i in publish_test_obj:
            print(i.id)
            dict_data['id'] = i.id
            dict_data['total'] = AllottedQuestion.objects.filter(fk_aptitude_set_id=i.id).count()
            mylist_data.append(dict_data)
            dict_data = {}

        print(mylist_data)
        render_string = render_to_string("aptitidetestmaster_div.html",
                                         {"useroperations_obj": user_operations_obj, "publish_test_obj": publish_test_obj,
                                          "my_list": mylist_data})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')



@csrf_exempt
def filter_select_list(request):
    """
    Filtering aptitude test to select questions for adding it
    in new aptitude test
    :param request:
    :return:
    """
    try:
        course = request.POST.get("course")
        sem = request.POST.get("sem")
        section = request.POST.get("section")
        faculty = request.POST.get("faculty")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        dict_data = {}
        mylist_data = []

        if start_date:
            start_date = datetime.datetime.strptime(str(request.POST.get("start_date")), '%d/%m/%Y').strftime('%Y-%m-%d')

        if end_date:
            end_date = datetime.datetime.strptime(str(request.POST.get("end_date")), '%d/%m/%Y').strftime('%Y-%m-%d')

        filter_str = "AptitudeSet.objects.filter(status='Attempted')"
        if sem:
            filter_str += ".filter(fk_semesters_id=sem)"
        if course:
            filter_str += ".filter(fk_course_id=course)"
        if faculty:
            filter_str += ".filter(fk_faculty_id=faculty)"
        if section:
            filter_str += ".filter(fk_sections_id=section)"
        if start_date:
            filter_str += ".filter(schedule__gte=start_date)"
        if end_date:
            filter_str += ".filter(schedule__lte=end_date)"
        if filter_str == "AptitudeSet.objects":
            filter_str += ".all()"

        publish_test_obj = eval(filter_str)
        print("start date, ", start_date)
        print("end date ", end_date)

        for i in publish_test_obj:
            dict_data['id'] = i.id
            dict_data['total'] = AllottedQuestion.objects.filter(fk_aptitude_set_id=i.id).count()
            mylist_data.append(dict_data)
            dict_data = {}

        render_string = render_to_string("aptitudeselecttable.html", {"publish_test_obj": publish_test_obj,
                                                                      "my_list": mylist_data})
        return HttpResponse(render_string)
    except Exception:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')
