from django.urls import path

from manage_student.views import *

urlpatterns = [
    path('save-notes/', save_notes, name='save_notes'),
    path('notes/', notes, name='notes'),
    path('edit-notes', edit_notes, name='edit_notes'),
    path('update-notes/', update_notes, name='update_notes'),
    path('delete-notes/', delete_notes, name='delete_notes'),
    path('add_syllabus/', add_syllabus, name='add_syllabus'),
    path('syllabus/', syllabus, name='syllabus'),
    path('delete_syllabus/', delete_syllabus, name='delete_syllabus'),
    path('edit_syllabus/', edit_syllabus, name='edit_syllabus'),
    path('update_syllabus/', update_syllabus, name='update_syllabus'),
    path('assignment/', assignment, name='assignment'),
    path('save-assignment/', save_assignment, name='save_assignment'),
    path('edit-assignment/', edit_assignment, name='edit_assignment'),
    path('assignment-get-student-list/', assignment_get_student_list, name='assignment_get_student_list'),
    path('delete-assignment/', delete_assignment, name='delete_assignment'),
    path('edit-student-list/', edit_assignment, name='edit_student_list'),
    path('filter_notes/', filter_notes, name='filter_notes'),
    path('filter_assignment/', filter_assignments, name='filter_assignments'),
]
