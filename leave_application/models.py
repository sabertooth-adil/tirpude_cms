from django.contrib.auth.models import User, models
import datetime
from authentication.models import UserInfo, Course
from master_forms.models import UserType, Semester, Section


class LeaveReason(models.Model):
    """
      Reasons for leave applications
    """
    reason_to_leave = models.CharField(max_length=200)

    def __str__(self):
        return self.reason_to_leave


class LeaveApplication(models.Model):
    """
         Leave application model for students and faculty
    """
    fk_user_info = models.ForeignKey(UserInfo, null=True, blank=True, related_name='fk_user_info', on_delete=models.CASCADE)
    fk_faculty_user = models.ForeignKey(UserInfo, null=True, blank=True, related_name='fk_faculty_user', on_delete=models.CASCADE)
    fk_leave_reason = models.ForeignKey(LeaveReason, blank=True, null=True, on_delete=models.CASCADE)
    fk_sections = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    fk_semesters = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    fk_user_type = models.ForeignKey(UserType, blank=True, null=True, on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    reason = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="leaveApplications/", null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    action_status = models.CharField(max_length=20, blank=True, null=True, default="Pending")
    date_post = models.DateField(default=datetime.date.today, null=True, blank=True)

    def __str__(self):
        return self.fk_user_info.first_name