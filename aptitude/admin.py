from django.contrib import admin
from aptitude.models import *


# Register your models here.

class AptitudeTest(admin.ModelAdmin):
    list_display = ("test_name", "test_info", "id")


admin.site.register(AptitudeSet, AptitudeTest)


class AptitudeQuestions(admin.ModelAdmin):
    list_display = ("questions", "answer", "id", "fk_aptitude_set")


admin.site.register(AptitudeQuestion, AptitudeQuestions)
