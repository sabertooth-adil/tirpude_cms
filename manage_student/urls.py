from django.urls import path

from manage_student.views import save_notes, notes, edit_notes, update_notes, delete_notes, add_syllabus, syllabus, \
    delete_syllabus, edit_syllabus, update_syllabus

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

]
