from django.contrib import admin
from django.urls import path

from attendance.views import attendance, GetSubjects, filter_attendance, add_attendance_detail, save_attendance_detail, \
    filter_attendance_detail, update_attendance_detail, single_student_attendance_detail, get_subject_attendance_detail

urlpatterns = [
    path('attendance/', attendance, name='attendance'),
    path('GetSubjects/', GetSubjects, name='GetSubjects'),
    path('filter-attendance/', filter_attendance, name='filter_attendance'),
    path('add-attendance-detail/', add_attendance_detail, name='add_attendance_detail'),
    path('save-attendance-detail/', save_attendance_detail, name='save_attendance_detail'),
    path('filter-attendance-detail/', filter_attendance_detail, name='filter_attendance_detail'),
    path('update-attendance-detail/', update_attendance_detail, name='update_attendance_detail'),
    path('single-student-attendance-detail/', single_student_attendance_detail, name='single_student_attendance_detail'),
    path('get-subject-attendance-detail/', get_subject_attendance_detail,name='get_subject_attendance_detail'),
    # path('FilterChartAttendance/', FilterChartAttendance, name='FilterChartAttendance'),
]