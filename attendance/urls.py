from django.contrib import admin
from django.urls import path

from attendance.views import Attendance, GetSubjects, FilterAttendance, AddAttendanceDetail

urlpatterns = [
    path('Attendance/', Attendance, name='Attendance'),
    path('GetSubjects/', GetSubjects, name='GetSubjects'),
    path('FilterAttendance/', FilterAttendance, name='FilterAttendance'),
    path('AddAttendanceDetail/', AddAttendanceDetail, name='AddAttendanceDetail'),
]