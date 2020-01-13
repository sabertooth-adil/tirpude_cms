from django.urls import path

from aptitude.views import *

urlpatterns = [
    path('aptitude-test/', aptitude_test, name='aptitude_test'),
    path('aptitude-test-details/', aptitude_test_details, name='aptitude_test_details'),
    path('delete-master-aptitude-details/', delete_master_aptitude_details, name='delete_master_aptitude_details'),
    path('add-question/', add_question, name='add_question'),
    path('delete-aptitude-question/', delete_aptitude_question, name='delete_aptitude_question'),
    path('edit-master-aptitude-details/', edit_master_aptitude_details, name='edit_master_aptitude_details'),
    path('edit-question/', edit_question, name='edit_question'),
    path('select-question/', select_question, name='select_question'),
    path('add-selected-questions/', add_selected_question, name='add_select_questions'),
    path('start-aptitude-test/<int:id>', start_aptitude_test, name='start_aptitude_test'),
    path('select-answer/', select_answer, name='select_answer'),
    path('submit-aptitude-test/', submit_aptitude_test, name='submit_aptitude_test'),
    path('aptitude-score/', aptitude_score, name='aptitude_score'),
    path('student-score-list/', student_score_list, name='student_score_list'),
    path('view-student-answer/', view_student_answer, name='view_student_answer'),
    # path('FilterPublishList/', FilterPublishList, name='FilterPublishList'),
    # path('FilterTestList/', FilterTestList, name='FilterTestList'),
    # path('FilterSelectList/', FilterSelectList, name='FilterSelectList'),
]
