from django.contrib import admin
from event.models import *


# Register your models here.
class StudentEvents(admin.ModelAdmin):
    list_display = ("id", "event_title", "start_date", "end_date", "event_type")


admin.site.register(StudentEvent, StudentEvents)


class Activity(admin.ModelAdmin):
    list_display = (
        "id", "fk_student_events", "activity_name", "activity_details", "activity_type", "activity_venue",
        "schedule_date",
        "start_time", "end_time")


admin.site.register(EventActivity, Activity)


class EventMembers(admin.ModelAdmin):
    list_display = ("id", "fk_student_events", "fk_user_info", "fk_course", "fk_semesters", "fk_sections")


admin.site.register(EventMember, EventMembers)


class ActivityMembers(admin.ModelAdmin):
    list_display = ("fk_event_member", "roles", "task")


admin.site.register(ActivityMember, ActivityMembers)


class ActivityItems(admin.ModelAdmin):
    list_display = ("fk_activity", "item", "item_cost", "item_quantity")


admin.site.register(ActivityItem, ActivityItems)


class ActivityGrpMembers(admin.ModelAdmin):
    list_display = ("fk_events_registrations", "fk_activity", "grp_member_name")


admin.site.register(ActivityGroupMember, ActivityGrpMembers)


class EventRegistrations(admin.ModelAdmin):
    list_display = ("id", "fk_student_events", "first_name", "college")


admin.site.register(EventRegistration, EventRegistrations)
