from django.contrib import admin

# Register your models here.
from authentication.models import UserInfo, AddressDetail, AcademicInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(UserInfo, UserInfoAdmin)


class AddressDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'address')


admin.site.register(AddressDetail, AddressDetailAdmin)


class AcademicInfoAdmin(admin.ModelAdmin):
    list_display = ('fk_user_info', 'roll_no')


admin.site.register(AcademicInfo, AcademicInfoAdmin)
