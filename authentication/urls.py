from django.contrib import admin
from django.urls import path

from authentication.views import admin_home, admin_login, admin_signup, register_user, signup_user, signout_user, \
    profile_user, change_password, save_personal_info, save_other_details, save_academic_details, save_user_profile_pic, \
    update_profile_picture, get_city_district_list, get_sub_cast_list, get_stream_or_field_list, \
    get_degree_stream_or_field_list, forgot_password, error_handler_500

urlpatterns = [
    path('', admin_home, name='Admin_Home'),
    path('login/', admin_login, name='admin_login'),
    path('signup/', admin_signup, name='admin_signup'),
    path('register-user/', register_user, name='register_user'),
    path('signup-user/', signup_user, name='signup_user'),
    path('signout-user/', signout_user, name='signout_user'),
    path('profile-user/', profile_user, name='profile_user'),
    path('change-password/', change_password, name='change_password'),
    path('save-personal-info/', save_personal_info, name='save_personal_info'),
    path('save-other-details/', save_other_details, name='save_other_details'),
    path('save-academic-details/', save_academic_details, name='save_academic_details'),
    path('save-user-profile-pic/', save_user_profile_pic, name='SaveUserProfilePic'),
    path('update-profile-picture/', update_profile_picture, name='update_profile_picture'),
    path('get-city-district-list/', get_city_district_list, name='get_city_district_list'),
    path('get-sub-cast-list/', get_sub_cast_list, name='get_sub_cast_list'),
    path('get-stream-or-field-list/', get_stream_or_field_list, name='get_stream_or_field_list'),
    path('get_degree-stream-or-field-list/', get_degree_stream_or_field_list, name='get_degree_stream_or_field_list'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('error-page-500/', error_handler_500, name='error_handler_500'),
]
