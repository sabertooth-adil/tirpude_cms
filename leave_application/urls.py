from django.urls import path
from leave_application import views

urlpatterns = [
    path('leave-application/', views.leave_application, name='leave-application'),
    path('leave-application-submit/', views.leave_application_submit, name='leave-application-submit'),
    path('approve-disapprove-application/', views.approve_disapprove_application, name='approve-disapprove-application'),
    path('view-leave-application-detail/', views.view_leave_application_detail, name='view-leave-application-detail'),
    path('leave-application-detail/', views.get_leave_application_detail, name='leave-application-detail'),
    path('filter-applications/', views.filter_leave_applications, name='filter-leave-applications'),
    path('delete-leave-application/', views.delete_leave_application, name='delete-leave-application'),
    ]