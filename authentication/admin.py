from django.contrib import admin

# Register your models here.
from authentication.models import UserInfo, AddressDetail, AcademicInfo


class UserInfoAdmin(admin.ModelAdmin):
    """
    User Information Admin
    """
    list_display = ('first_name', 'last_name')


admin.site.register(UserInfo, UserInfoAdmin)


class AddressDetailAdmin(admin.ModelAdmin):
    """
    Address Detail Admin
    """
    list_display = ('id', 'address')


admin.site.register(AddressDetail, AddressDetailAdmin)


class AcademicInfoAdmin(admin.ModelAdmin):
    """
    Academic Information Admin
    """
    list_display = ('fk_user_info', 'roll_no')


admin.site.register(AcademicInfo, AcademicInfoAdmin)
