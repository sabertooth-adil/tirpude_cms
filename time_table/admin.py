from django.contrib import admin

from time_table.models import TimeTableMaster, TimeTableDetail


class TimeTableMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_date', 'to_date')


admin.site.register(TimeTableMaster, TimeTableMasterAdmin)


class TimeTableDetailAdmin(admin.ModelAdmin):
    list_display = ('fk_day', 'fk_subjects', 'lecture_break')


admin.site.register(TimeTableDetail, TimeTableDetailAdmin)
