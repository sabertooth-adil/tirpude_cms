from django.contrib import admin
from aptitude.models import *
# Register your models here.

class aptitudeset(admin.ModelAdmin):
	list_display = ('test_name','test_info','id')
admin.site.register(AptitudeSet,aptitudeset)

class aptitudequestion(admin.ModelAdmin):
	list_display = ('questions','answer','id','fk_aptitude_set')
admin.site.register(AptitudeQuestion,aptitudequestion)