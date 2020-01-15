from django.urls import path
from leave_application import views

urlpatterns = [
    path('leave-application/', views.leave_application, name='leave_application'),
    path('leave-application-submit/', views.leave_application_submit, name='leave_application_submit'),
    path('approve-disapprove-application/', views.approve_disapprove_application,
         name='approve_disapprove_application'),
    path('view-leave-application-detail/', views.view_leave_application_detail, name='view_leave_application_detail'),
    path('leave-application-detail/', views.get_leave_application_detail, name='leave_application_detail'),
    path('filter-applications/', views.filter_leave_applications, name='filter_leave_applications'),
    path('delete-leave-application/', views.delete_leave_application, name='delete_leave_application'),
]
