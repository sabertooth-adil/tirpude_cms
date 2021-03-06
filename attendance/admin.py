from django.contrib import admin

from attendance.models import StudentAttendance


class StudentAttendanceAdmin(admin.ModelAdmin):
    """
    Student Attendance Admin
    """
    list_display = ('date', 'attendance_status', 'fk_student_user_info')


admin.site.register(StudentAttendance, StudentAttendanceAdmin)
