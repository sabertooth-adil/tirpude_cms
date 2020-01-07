from django.urls import path

from manage_student.views import save_notes, notes, edit_notes, update_notes, delete_notes

urlpatterns = [
    path('save-notes/', save_notes, name='save_notes'),
    path('notes/', notes, name='Notes'),
    path('edit-notes', edit_notes, name='EditNotes'),
    path('update-notes/', update_notes, name='UpdateNotes'),
    path('delete-notes/', delete_notes, name='DeleteNotes'),
]
