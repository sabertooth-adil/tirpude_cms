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

    def __str__(self):
        return self.notes_title


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

    def __str__(self):
        return self.syllabus_title


class Assignment(models.Model):
    """
    Assignment Database
    """
    assignment_title = models.CharField(max_length=200, blank=True, null=True)
    assignment_info = models.CharField(max_length=2000, blank=True, null=True)
    assignment_file = models.FileField(upload_to="assignments/", null=True, blank=True)
    date_post = models.DateField(max_length=20, blank=True, null=True)
    date_final = models.DateField(max_length=20, blank=True, null=True)
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_subjects = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE)
    fk_sections = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    fk_semesters = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.assignment_title


class SubmittedAssignment(models.Model):
    """
    Submitted Assignment Database
    """
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_assignment_title = models.ForeignKey(Assignment, blank=True, null=True, on_delete=models.CASCADE)
    submission_date = models.DateField(max_length=20, blank=True, null=True)
    submitted_file = models.FileField(upload_to="submitted_assignments/", null=True, blank=True)

    def __str__(self):
        return str(self.submission_date)


