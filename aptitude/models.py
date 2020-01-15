from django.db import models
from master_forms.models import Section, Semester, Course
from authentication.models import UserInfo


class AptitudeSet(models.Model):
    """
    Aptitude Set Database
    """
    fk_faculty = models.ForeignKey(UserInfo, null=True, blank=True, on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    fk_semesters = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    fk_sections = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100, blank=True, null=True)
    test_info = models.CharField(max_length=500, blank=True, null=True)
    question_type = models.CharField(max_length=20, blank=True, null=True)
    schedule = models.DateTimeField(blank=True, null=True)
    test_duration = models.CharField(max_length=50, blank=True, null=True)
    time_extend = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.test_name


class AptitudeQuestion(models.Model):
    """
    Aptitude Questions Database
    """
    fk_aptitude_set = models.ForeignKey(AptitudeSet, blank=True, null=True, on_delete=models.CASCADE)
    questions = models.CharField(max_length=1000, blank=True, null=True)
    option_a = models.CharField(max_length=100, blank=True, null=True)
    option_b = models.CharField(max_length=100, blank=True, null=True)
    option_c = models.CharField(max_length=100, blank=True, null=True)
    option_d = models.CharField(max_length=100, blank=True, null=True)
    answer = models.CharField(max_length=100, blank=True, null=True)
    solution = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.questions


class AllottedQuestion(models.Model):
    """
    Question and Aptitude Relation Database
    """
    fk_aptitude_set = models.ForeignKey(AptitudeSet, blank=True, null=True, on_delete=models.CASCADE)
    fk_question = models.ForeignKey(AptitudeQuestion, blank=True, null=True, on_delete=models.CASCADE)


class PublishTest(models.Model):
    """
    Published Test Database
    """
    fk_faculty_user_info = models.ForeignKey(UserInfo, null=True, blank=True, on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    fk_semesters = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    fk_sections = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    fk_aptitude_set = models.ForeignKey(AptitudeSet, blank=True, null=True, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100, blank=True, null=True)
    test_info = models.CharField(max_length=500, blank=True, null=True)
    schedule = models.DateTimeField(blank=True, null=True)
    test_duration = models.CharField(max_length=50, blank=True, null=True)
    time_extend = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.test_name


class AptitudeSession(models.Model):
    """
    Students Aptitude Session Database
    """
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_publish_test = models.ForeignKey(PublishTest, blank=True, null=True, on_delete=models.CASCADE)
    fk_aptitude_set = models.ForeignKey(AptitudeSet, blank=True, null=True, on_delete=models.CASCADE)
    time_start = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.status


class StudentAptitudeAnswer(models.Model):
    """
    Students Aptitude Answer Database
    """
    fk_aptitude_session = models.ForeignKey(AptitudeSession, blank=True, null=True, on_delete=models.CASCADE)
    fk_aptitude_test = models.ForeignKey(AptitudeSet, blank=True, null=True, on_delete=models.CASCADE)
    fk_aptitude_question = models.ForeignKey(AptitudeQuestion, blank=True, null=True, on_delete=models.CASCADE)
    answer = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.answer


class AptitudeTestScore(models.Model):
    """
    Students Aptitude Test Score Database
    """
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_aptitude_test = models.ForeignKey(AptitudeSet, blank=True, null=True, on_delete=models.CASCADE)
    fk_aptitude_session = models.ForeignKey(AptitudeSession, blank=True, null=True, on_delete=models.CASCADE)
    out_of = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    percent = models.IntegerField(blank=True, null=True)

    def __int__(self):
        return str(self.percent)
