from django.contrib import admin
from django.urls import path

from time_table.views import time_table, filter_time_table, save_update_date_note_timetable, edit_time_table, \
    add_time_table, \
    change_time_table_day, edit_day_time_table, update_time_table, delete_time_table_row, faculty_workload, \
    all_time_table, \
    all_faculty_workload, delete_time_table

urlpatterns = [
    path('time-table/', time_table,name='time-table'),
    path('filter-time-table/', filter_time_table, name='filter-time-table'),
    path('save-update-date-note-timetable/', save_update_date_note_timetable,name='save-update-date-note-timetable'),
    # path('edit-time-table/(?P<id>\d+)/$', edit_time_table, name='edit-time-table'),
    path('edit-time-table/<int:id>/', edit_time_table, name='edit-time-table'),
    path('add-time-table/', add_time_table, name='add-time-table'),
    path('change-time-table-day/', change_time_table_day, name='change-time-table-day'),
    path('edit-day-time-table/', edit_day_time_table, name='edit-day-time-table'),
    path('update-time-table/', update_time_table, name='update-time-table'),
    path('delete-time-table-row/', delete_time_table_row, name='delete-time-table-row'),
    path('faculty-workload/', faculty_workload, name='faculty-workload'),
    path('all-time-table/', all_time_table, name='all-time-table'),
    path('all-faculty-workload/', all_faculty_workload, name='all-faculty-workload'),
    path('delete-time-table/', delete_time_table, name='delete-time-table'),
]