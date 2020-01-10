from django.contrib import admin
from django.urls import path

from authenticate_user.views import authenticate_user, activate_deactivate_user, filter_authenticate_user, \
    delete_register_request, assign_user_role

urlpatterns = [
    path('authenticate-user/', authenticate_user, name='authenticate-user'),
    path('activate-deactivate-user/', activate_deactivate_user, name='activate-deactivate-user'),
    path('filter-authenticate-user/', filter_authenticate_user, name='filter-authenticate-user'),
    path('delete-register-request/', delete_register_request, name='delete-register-request'),
    path('assign-user-role/', assign_user_role, name='assign-user-role'),
]