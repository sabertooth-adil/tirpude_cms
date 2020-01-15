from django.contrib import admin

from time_table.models import TimeTableMaster, TimeTableDetail


class TimeTableMasterAdmin(admin.ModelAdmin):
    """
    Time Table Master Admin
    """
    list_display = ('id', 'from_date', 'to_date')


admin.site.register(TimeTableMaster, TimeTableMasterAdmin)


class TimeTableDetailAdmin(admin.ModelAdmin):
    """
    Time Table Detail Admin
    """
    list_display = ('fk_day', 'fk_subjects', 'lecture_break')


admin.site.register(TimeTableDetail, TimeTableDetailAdmin)
