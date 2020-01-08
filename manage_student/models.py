from django.db import models
from master_forms.models import Subject, Section, Semester, Course
from authentication.models import UserInfo


class AcademicNote(models.Model):
    """
    Academic Note Database
    """
    notes_title = models.CharField(max_length=200, blank=True, null=True)
    notes_detail = models.TextField(null=True, blank=True)
    notes_file = models.FileField(upload_to="notes/", null=True, blank=True)
    date_post = models.DateField(max_length=20, blank=True, null=True)
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_subjects = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE)
    fk_sections = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    fk_semesters = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)


class AcademicSyllabus(models.Model):
    """
    Academic Syllabus Database
    """
    syllabus_title = models.CharField(max_length=200, blank=True, null=True)
    syllabus_detail = models.TextField(null=True, blank=True)
    syllabus_file = models.FileField(upload_to="syllabus/", null=True, blank=True)
    date_post = models.DateField(max_length=20, blank=True, null=True)
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_subjects = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE)
    fk_semesters = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
