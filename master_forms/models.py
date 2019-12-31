from django.db import models
from django.contrib.auth.models import User, models
from django.utils import timezone
import datetime


class AcademicSession(models.Model):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.start_date + '-' + self.end_date


class Modules(models.Model):
    module_name = models.CharField(max_length=100, blank=True, null=True)
    module_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.module_name


class Screen(models.Model):
    fk_modules = models.ForeignKey(Modules, on_delete=models.CASCADE, null=True, blank=True)
    screen_name = models.CharField(max_length=100, blank=True, null=True)
    screen_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.fk_modules.module_name


class UserType(models.Model):
    user_type = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user_type


class UserRole(models.Model):
    user_role = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user_role


class YearofAdmission(models.Model):
    year_of_admission = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.year_of_admission


class UserOperations(models.Model):
    status = models.CharField(max_length=50, blank=True, null=True)
    special_data = models.CharField(max_length=50, blank=True, null=True, default="N")
    view_data = models.CharField(max_length=50, blank=True, null=True, default="N")
    edit_data = models.CharField(max_length=50, blank=True, null=True, default="N")
    save_data = models.CharField(max_length=50, blank=True, null=True, default="N")
    delete_data = models.CharField(max_length=50, blank=True, null=True, default="N")
    fk_modules = models.ForeignKey(Modules, blank=True, null=True, on_delete=models.CASCADE)
    fk_screen = models.ForeignKey(Screen, blank=True, null=True, on_delete=models.CASCADE)
    fk_user_role = models.ForeignKey(UserRole, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.status


class Nationality(models.Model):
    nationality = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nationality


class State(models.Model):
    state = models.CharField(max_length=30, blank=True, null=True)
    fk_nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.state


class City(models.Model):
    city = models.CharField(max_length=30, blank=True, null=True)
    fk_state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.city


class District(models.Model):
    district = models.CharField(max_length=30, blank=True, null=True)
    fk_state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.district


class Tehsil(models.Model):
    tehsil = models.CharField(max_length=30, blank=True, null=True)
    fk_state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.tehsil


class PostalCode(models.Model):
    postal_code = models.CharField(max_length=30, blank=True, null=True)
    fk_city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.postal_code


class MotherTongue(models.Model):
    mother_tongue = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.mother_tongue


class Religion(models.Model):
    religion = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.religion


class Gender(models.Model):
    gender = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.gender


class BloodGroup(models.Model):
    blood_group = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.blood_group


class Course(models.Model):
    course = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.course


class Semesters(models.Model):
    semester = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.semester


class Sections(models.Model):
    sections = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.sections


class TwelvethOrDiploma(models.Model):
    twelveth_or_diploma = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.twelveth_or_diploma


class StreamOrField(models.Model):
    fk_twelveth_or_diploma = models.ForeignKey(TwelvethOrDiploma, blank=True, null=True, on_delete=models.CASCADE)
    stream_or_field_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.stream_or_field_name


class Subjects(models.Model):
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    fk_semesters = models.ForeignKey(Semesters, blank=True, null=True, on_delete=models.CASCADE)
    subjects = models.CharField(max_length=100, blank=True, null=True)
    compulsory_attendance = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.subjects


class Days(models.Model):
    day = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.day


class Time(models.Model):
    time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.time


class Lecture(models.Model):
    lecture = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.lecture


class Category(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.category


class Reserved(models.Model):
    reserved = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.reserved


class ApplyingConcession(models.Model):
    applying_concession = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.applying_concession


class Cast(models.Model):
    cast = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.cast


class SubCast(models.Model):
    fk_cast = models.ForeignKey(Cast, blank=True, null=True, on_delete=models.CASCADE)
    sub_cast = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.sub_cast


class Degree(models.Model):
    degree = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.degree


class DegreeStreamOrField(models.Model):
    fk_degree = models.ForeignKey(Degree, blank=True, null=True, on_delete=models.CASCADE)
    stream_or_field_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.stream_or_field_name


class PhysicallyChallenged(models.Model):
    physically_challenged = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.physically_challenged
