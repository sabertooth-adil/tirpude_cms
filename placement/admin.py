from django.contrib import admin

from placement.models import Company, CompanyAppearanceJobTypeDetail, CompanyAppearanceDateTime, CompanyAppearance, \
    AppleCompanyAppearance, CompanyAppearanceTestResult


class CompanyAdmin(admin.ModelAdmin):
    """
    Company Master Admin
    """
    list_display = ('id', 'company_name')


admin.site.register(Company, CompanyAdmin)


class CompanyAppearanceJobTypeDetailAdmin(admin.ModelAdmin):
    """
    Company Appearance Job Type Detail Admin
    """
    list_display = ('id', 'package', 'job_location')


admin.site.register(CompanyAppearanceJobTypeDetail, CompanyAppearanceJobTypeDetailAdmin)


class CompanyAppearanceDateTimeAdmin(admin.ModelAdmin):
    """
    Company Appearance Date, Time Admin
    """
    list_display = ('id', 'date', 'start_time', 'end_time')


admin.site.register(CompanyAppearanceDateTime, CompanyAppearanceDateTimeAdmin)


class CompanyAppearanceAdmin(admin.ModelAdmin):
    """
    Company Appearance Admin
    """
    list_display = ('id', 'fk_company')


admin.site.register(CompanyAppearance, CompanyAppearanceAdmin)


class AppleCompanyAppearanceAdmin(admin.ModelAdmin):
    """
    Apple Company Appearance Admin
    """
    list_display = ('id', 'applied_date')


admin.site.register(AppleCompanyAppearance, AppleCompanyAppearanceAdmin)


class CompanyAppearanceTestResultAdmin(admin.ModelAdmin):
    """
    Company Appearance Test Result Admin
    """
    list_display = ('id', 'fk_appled_company_appearance')


admin.site.register(CompanyAppearanceTestResult, CompanyAppearanceTestResultAdmin)
