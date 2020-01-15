from django.contrib.auth.models import User, models
import datetime

from master_forms.models import UserType, UserRole, Gender, MotherTongue, Nationality, Religion, BloodGroup, City, \
    State, District, Course, Semester, Section, YearOfAdmission, TwelvethOrDiploma, StreamOrField, DegreeStreamOrField, \
    Degree, Category, Reserved, ApplyingConcession, Cast, SubCast, PhysicallyChallenged, AcademicSession


class UserInfo(models.Model):
    """
    Basic Detail Of User
    """
    status = models.CharField(default="Inactive", max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    profile_image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    dob = models.DateField(max_length=30, blank=True, null=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    phone_no2 = models.CharField(max_length=20, blank=True, null=True)
    aadhar_no = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    fk_user_type = models.ForeignKey(UserType, blank=True, null=True, on_delete=models.CASCADE)
    fk_user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE, null=True, blank=True)
    fk_gender = models.ForeignKey(Gender, blank=True, null=True, on_delete=models.CASCADE)
    fk_mother_tongue = models.ForeignKey(MotherTongue, blank=True, null=True, on_delete=models.CASCADE)
    fk_nationality = models.ForeignKey(Nationality, blank=True, null=True, on_delete=models.CASCADE)
    fk_religion = models.ForeignKey(Religion, blank=True, null=True, on_delete=models.CASCADE)
    fk_blood_group = models.ForeignKey(BloodGroup, blank=True, null=True, on_delete=models.CASCADE)
    registration_date = models.DateField(default=datetime.date.today, null=True, blank=True)

    # def __str__(self):
    #     return self.first_name + '-' + self.last_name


class AddressDetail(models.Model):
    """
    Correspondence/Permanent Address of Users
    """
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, blank=True)
    fk_city = models.ForeignKey(City, blank=True, null=True, on_delete=models.CASCADE, related_name='fk_city')
    fk_state = models.ForeignKey(State, blank=True, null=True, on_delete=models.CASCADE, related_name='fk_state')
    fk_district = models.ForeignKey(District, blank=True, null=True, on_delete=models.CASCADE,
                                    related_name='fk_district')
    tehsil = models.CharField(max_length=100, blank=True)
    pin_code = models.CharField(max_length=20, blank=True)
    correspondence_address = models.CharField(max_length=200, blank=True, null=True)
    fk_correspondence_city = models.ForeignKey(City, blank=True, null=True, on_delete=models.CASCADE,
                                               related_name='fk_correspondence_city')
    fk_correspondence_state = models.ForeignKey(State, blank=True, null=True, on_delete=models.CASCADE,
                                                related_name='fk_correspondence_state')
    fk_correspondence_district = models.ForeignKey(District, blank=True, null=True, on_delete=models.CASCADE,
                                                   related_name='fk_correspondence_district')
    correspondence_tehsil = models.CharField(max_length=100, blank=True)
    correspondence_pin_code = models.CharField(max_length=20, blank=True, null=True)

    # def __str__(self):
        # return str(self.id)


class AcademicInfo(models.Model):
    """
    Academic information of Student
    """
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    fk_semesters = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    fk_sections = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    fk_year_of_admission = models.ForeignKey(YearOfAdmission, blank=True, null=True, on_delete=models.CASCADE)
    roll_no = models.IntegerField(blank=True, null=True)

    school_name = models.CharField(max_length=100, blank=True, null=True)
    school_board = models.CharField(max_length=30, blank=True, null=True)
    school_place = models.CharField(max_length=30, blank=True, null=True)
    tenth_year_of_passing = models.DateField(max_length=30, blank=True, null=True)
    tenth_marks = models.IntegerField(blank=True, null=True)
    tenth_out_of = models.IntegerField(blank=True, null=True)
    school_percentage = models.CharField(max_length=10, blank=True, null=True)

    fk_twelveth_or_diploma = models.ForeignKey(TwelvethOrDiploma, blank=True, null=True, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=100, blank=True, null=True)
    college_board_or_university = models.CharField(max_length=30, blank=True, null=True)
    fk_stream_or_field = models.ForeignKey(StreamOrField, blank=True, null=True, on_delete=models.CASCADE)
    college_place = models.CharField(max_length=30, blank=True, null=True)
    college_date_of_passing = models.DateField(max_length=30, blank=True, null=True)
    college_total_marks = models.IntegerField(blank=True, null=True)
    college_marks_out_of = models.IntegerField(blank=True, null=True)
    college_percentage = models.CharField(max_length=30, blank=True, null=True)

    fk_degree = models.ForeignKey(Degree, blank=True, null=True, on_delete=models.CASCADE)
    fk_degree_stream_or_field = models.ForeignKey(DegreeStreamOrField, blank=True, null=True, on_delete=models.CASCADE)
    degree_college_name = models.CharField(max_length=100, blank=True, null=True)
    degree_college_board_or_university = models.CharField(max_length=100, blank=True, null=True)
    degree_college_place = models.CharField(max_length=100, blank=True, null=True)
    degree_college_date_of_passing = models.DateField(max_length=30, blank=True, null=True)
    degree_college_total_marks = models.IntegerField(blank=True, null=True)
    degree_college_marks_out_of = models.IntegerField(blank=True, null=True)
    degree_college_percentage = models.IntegerField(blank=True, null=True)

    guardian_name = models.CharField(max_length=30, blank=True, null=True)
    occupation_of_guardian = models.CharField(max_length=30, blank=True, null=True)
    annual_income_of_guardian = models.CharField(max_length=30, blank=True, null=True)
    relationship_with_guardian = models.CharField(max_length=30, blank=True, null=True)
    guardian_mobile_no = models.CharField(max_length=30, blank=True, null=True)

    fk_domicile_of_state = models.ForeignKey(State, blank=True, null=True, on_delete=models.CASCADE)
    fk_category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    fk_reserved = models.ForeignKey(Reserved, blank=True, null=True, on_delete=models.CASCADE)
    fk_applying_concession = models.ForeignKey(ApplyingConcession, blank=True, null=True, on_delete=models.CASCADE)
    fk_cast = models.ForeignKey(Cast, blank=True, null=True, on_delete=models.CASCADE)
    fk_sub_cast = models.ForeignKey(SubCast, blank=True, null=True, on_delete=models.CASCADE)
    fk_physically_challenged = models.ForeignKey(PhysicallyChallenged, blank=True, null=True, on_delete=models.CASCADE)

    resume = models.FileField(upload_to="resume/", null=True, blank=True)
    fk_academic_session = models.ForeignKey(AcademicSession, blank=True, null=True, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.fk_user_info.first_name
