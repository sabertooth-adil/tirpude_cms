from django.contrib import admin

from manage_student.models import *


# Register your models here.

class Assignments(admin.ModelAdmin):
    """
    Assignments Admin table
    """
    list_display = ("assignment_title", "assignment_info", "fk_subjects", "fk_user_info")


admin.site.register(Assignment, Assignments)


class SubmittedAssignments(admin.ModelAdmin):
    """
    Submitted Assignments Admin table
    """
    list_display = ("submission_date", "submitted_file", "fk_user_info", "fk_assignment_title")


admin.site.register(SubmittedAssignment, SubmittedAssignments)


class AcademicNotes(admin.ModelAdmin):
    """
    Academic Notes Admin table
    """
    list_display = (
        "notes_title", "notes_detail", "date_post", "fk_user_info", "fk_subjects", "fk_sections", "fk_semesters",
        "fk_course")


admin.site.register(AcademicNote, AcademicNotes)
