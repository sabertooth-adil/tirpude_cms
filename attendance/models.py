from django.contrib.auth.models import User, models
import datetime

from authentication.models import UserInfo
from master_forms.models import Course, Semester, Section, Subject


class StudentAttendance(models.Model):
    """
    Student Attendance
    """
    fk_student_user_info = models.ForeignKey(UserInfo, null=True, blank=True, related_name='fk_student_user_info',
                                             on_delete=models.CASCADE)
    fk_faculty_user_info = models.ForeignKey(UserInfo, null=True, blank=True, related_name='fk_faculty_user_info',
                                             on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    fk_semesters = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    fk_sections = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    fk_subjects = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField(max_length=30, blank=True, null=True)
    attendance_status = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.attendance_status
