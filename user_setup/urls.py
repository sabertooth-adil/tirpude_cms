from django.contrib import admin
from django.urls import path

from user_setup.views import screens_modules, add_module_name, edit_module_name, update_module_name, delete_module, \
    add_screen_name, edit_screen_name, update_screen_name, delete_screen, manage_user, add_user_role, update_userright, \
    edit_manage_user, update_user_role_name, delete_manage_role, assign_user_role

urlpatterns = [
    path('screens-modules/', screens_modules, name='screens-modules'),
    path('add-module-name/', add_module_name, name='add-module-name'),
    path('edit-module-name/', edit_module_name, name='edit-module-name'),
    path('update-module-name/', update_module_name, name='update-module-name'),
    path('delete-module/', delete_module, name='delete-module'),
    path('add-screen-name/', add_screen_name, name='add-screen-name'),
    path('edit-screen-name/', edit_screen_name, name='edit-screen-name'),
    path('update-screen-name/', update_screen_name, name='update-screen-name'),
    path('delete-screen/', delete_screen, name='delete-screen'),

    path('manage-user/', manage_user, name='manage-user'),
    path('add_user_role/', add_user_role, name='add_user_role'),
    path('update-userright/', update_userright, name='update-userright'),
    path('edit-manage-user/(?P<id>\d+)/$', edit_manage_user, name='edit-manage-user'),
    path('update-user-role-name/', update_user_role_name, name='update-user-role-name'),
    path('delete-manage-role/', delete_manage_role, name='delete-manage-role'),
    path('assign-user-role/', assign_user_role, name='assign-user-role'),
]
