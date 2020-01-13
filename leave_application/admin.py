from django.contrib import admin
from leave_application.models import LeaveReason, LeaveApplication

admin.site.register(LeaveApplication)
admin.site.register(LeaveReason)
