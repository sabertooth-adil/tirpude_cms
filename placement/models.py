from django.contrib.auth.models import User, models
import datetime

from authentication.models import UserInfo, AcademicInfo
from master_forms.models import CompanyType, JobType, SelectionProcessTest


class Company(models.Model):
    """
    Company Master
    """
    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_main_address = models.CharField(max_length=500, blank=True, null=True)
    company_location = models.CharField(max_length=100, blank=True, null=True)
    fk_company_type = models.ForeignKey(CompanyType, blank=True, null=True, on_delete=models.CASCADE)
    contact_person_one_name = models.CharField(max_length=100, blank=True, null=True)
    contact_person_one_email = models.CharField(max_length=50, blank=True, null=True)
    contact_person_one_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    contact_person_two_name = models.CharField(max_length=100, blank=True, null=True)
    contact_person_two_email = models.CharField(max_length=50, blank=True, null=True)
    contact_person_two_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    company_other_detail = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.company_name


class CompanyAppearanceJobTypeDetail(models.Model):
    """
    Company Appearance and Job Type, Package, job Location Detail
    """
    fk_job_type = models.ManyToManyField(JobType, blank=True, null=True)
    package = models.CharField(max_length=50, blank=True, null=True)
    job_location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.package + '-' + self.job_location


class CompanyAppearanceDateTime(models.Model):
    """
    Company Appearance Date, Time, Selection Process test Detail
    """
    date = models.DateField(max_length=20, blank=True, null=True)
    start_time = models.TimeField(max_length=20, blank=True, null=True)
    end_time = models.TimeField(max_length=20, blank=True, null=True)
    fk_selection_process_test = models.ForeignKey(SelectionProcessTest, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)


class CompanyAppearance(models.Model):
    """
    Company Appearance,Interview Location, other detail, Date, Time, And All other Detail
    """
    fk_company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    company_interview_location = models.CharField(max_length=500, blank=True, null=True)
    company_visiting_other_detail = models.CharField(max_length=500, blank=True, null=True)
    fk_company_appearance_job_type_detail_list = models.ManyToManyField(CompanyAppearanceJobTypeDetail, blank=True,
                                                                        null=True)
    fk_company_appearance_date_time_list = models.ManyToManyField(CompanyAppearanceDateTime, blank=True, null=True)

    def __str__(self):
        return self.company_visiting_other_detail


class AppleCompanyAppearance(models.Model):
    """
    Student which Apple Company Appearance
    """
    fk_company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    fk_company_appearance = models.ForeignKey(CompanyAppearance, blank=True, null=True, on_delete=models.CASCADE)
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_academic_info = models.ForeignKey(AcademicInfo, blank=True, null=True, on_delete=models.CASCADE)
    applied_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    placement_status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.applied_date)


class CompanyAppearanceTestResult(models.Model):
    """
    Test Result Of Company Appearance Test Result
    """
    fk_appled_company_appearance = models.ForeignKey(AppleCompanyAppearance, blank=True, null=True,
                                                     on_delete=models.CASCADE)
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_selection_process_test = models.ForeignKey(SelectionProcessTest, blank=True, null=True, on_delete=models.CASCADE)
    test_status = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.id)
