from django.contrib.auth.models import User
from master_forms.models import *
from authentication.models import *


class Notice(models.Model):
    """
    This is the Models for Notice Page
    """
    notice_body = models.TextField(null=True, blank=True)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    fk_semester = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    fk_section = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    audience = models.CharField(max_length=20, null=True, blank=True)
    notice_title = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(max_length=20, blank=True, null=True, default=datetime.date.today)

    def __str__(self):
        return self.notice_title
