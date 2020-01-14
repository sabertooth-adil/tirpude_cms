from django.db import models
from django.contrib.auth.models import User, models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


class AcademicSession(models.Model):
    """
    Academic Session start and end date
    """
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.start_date + '-' + self.end_date)


class Module(models.Model):
    """
    Module in Project
    """
    module_name = models.CharField(max_length=100, blank=True, null=True)
    module_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.module_name


class Screen(models.Model):
    """
    Screens in Project
    """
    fk_module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, blank=True)
    screen_name = models.CharField(max_length=100, blank=True, null=True)
    screen_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.screen_name


class UserType(models.Model):
    """
    User Type
    """
    user_type = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user_type


class UserRole(models.Model):
    """
    User Role
    """
    user_role = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user_role


class YearOfAdmission(models.Model):
    """
    Year Of Admission
    """
    year_of_admission = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.year_of_admission


class UserOperation(models.Model):
    """
    Roles And Rights
    User Operation on each screen and Module that used in project
    """
    status = models.CharField(max_length=50, blank=True, null=True)
    special_data = models.CharField(max_length=50, blank=True, null=True, default="N")
    view_data = models.CharField(max_length=50, blank=True, null=True, default="N")
    edit_data = models.CharField(max_length=50, blank=True, null=True, default="N")
    save_data = models.CharField(max_length=50, blank=True, null=True, default="N")
    delete_data = models.CharField(max_length=50, blank=True, null=True, default="N")
    fk_module = models.ForeignKey(Module, blank=True, null=True, on_delete=models.CASCADE)
    fk_screen = models.ForeignKey(Screen, blank=True, null=True, on_delete=models.CASCADE)
    fk_user_role = models.ForeignKey(UserRole, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.status


class Nationality(models.Model):
    """
    Nationality e.g. Indian, Other
    """
    nationality = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nationality


class State(models.Model):
    """
    State
    """
    state = models.CharField(max_length=30, blank=True, null=True)
    fk_nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.state


class City(models.Model):
    """
    City
    """
    city = models.CharField(max_length=30, blank=True, null=True)
    fk_state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.city


class District(models.Model):
    """
    District
    """
    district = models.CharField(max_length=30, blank=True, null=True)
    fk_state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.district


class Tehsil(models.Model):
    """
    Tehsil
    """
    tehsil = models.CharField(max_length=30, blank=True, null=True)
    fk_state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.tehsil


class PostalCode(models.Model):
    """
    Postal Code
    """
    postal_code = models.CharField(max_length=30, blank=True, null=True)
    fk_city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.postal_code


class MotherTongue(models.Model):
    """
    Mother Tongue
    """
    mother_tongue = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.mother_tongue


class Religion(models.Model):
    """
    Religion
    """
    religion = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.religion


class Gender(models.Model):
    """
    Gender
    """
    gender = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.gender


class BloodGroup(models.Model):
    """
    Blood Group
    """
    blood_group = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.blood_group


class Course(models.Model):
    """
    Course
    """
    course = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.course


class Semester(models.Model):
    """
    Semester
    """
    semester = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.semester


class Section(models.Model):
    """
    Section
    """
    sections = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.sections


class TwelvethOrDiploma(models.Model):
    """
    Twelveth Or Diploma
    """
    twelveth_or_diploma = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.twelveth_or_diploma


class StreamOrField(models.Model):
    """
    Stream Or Field in Twelveth Or Diploma
    """
    fk_twelveth_or_diploma = models.ForeignKey(TwelvethOrDiploma, blank=True, null=True, on_delete=models.CASCADE)
    stream_or_field_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.stream_or_field_name


class Subject(models.Model):
    """
    Subject
    """
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    fk_semesters = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    subjects = models.CharField(max_length=100, blank=True, null=True)
    compulsory_attendance = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.subjects


class Day(models.Model):
    """
    Day in Week
    """
    day = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.day


class Time(models.Model):
    """
    Time of Lecture
    """
    time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return str(self.time)


class Lecture(models.Model):
    """
    Lecture in one Day
    """
    lecture = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.lecture


class Category(models.Model):
    """
    Category Open/Reserved
    """
    category = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.category


class Reserved(models.Model):
    """
    if Category id Reserved than sub-category
    """
    reserved = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.reserved


class ApplyingConcession(models.Model):
    """
    Applying Concession
    """
    applying_concession = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.applying_concession


class Cast(models.Model):
    """
    Cast
    """
    cast = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.cast


class SubCast(models.Model):
    """
    Sub-Cast
    """
    fk_cast = models.ForeignKey(Cast, blank=True, null=True, on_delete=models.CASCADE)
    sub_cast = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.sub_cast


class Degree(models.Model):
    """
    Degree
    """
    degree = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.degree


class DegreeStreamOrField(models.Model):
    """
    Stream Or Field in Degree
    """
    fk_degree = models.ForeignKey(Degree, blank=True, null=True, on_delete=models.CASCADE)
    stream_or_field_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.stream_or_field_name


class PhysicallyChallenged(models.Model):
    """
    Physically Challenged
    """
    physically_challenged = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.physically_challenged



class CompanyType(models.Model):
    """
    Company Type
    """
    company_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.company_type


class JobType(models.Model):
    """
    Job Type
    """
    job_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.job_type


class SelectionProcessTest(models.Model):
    """
    Selection Process Test
    """
    test_name = models.CharField(max_length=100, blank=True, null=True)
    test_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.test_name