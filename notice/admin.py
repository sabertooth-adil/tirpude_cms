from django.contrib import admin
from .models import *


class NoticeAdmin(admin.ModelAdmin):
    """
    Admin Table for Notice model
    """
    list_display = ('id', 'audience', 'notice_title', 'date')


admin.site.register(Notice, NoticeAdmin)
