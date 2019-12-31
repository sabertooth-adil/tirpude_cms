from django.contrib import admin
from django.urls import path

from authentication.views import admin_home, admin_login, admin_signup, register_user, signup_user, sign_out_user, \
    profile_user, change_password, save_personal_info, save_other_details, save_academic_details, save_user_profile_pic, \
    update_profile_picture, get_citys_district_list, get_sub_cast_list, get_stream_or_field_list, \
    get_degree_stream_or_field_list, forgot_password

urlpatterns = [
    path('', admin_home,name='Admin_Home'),
    path('login/', admin_login,name='Admin_Login'),
    path('Signup/',admin_signup,name='Admin_Signup'),
    path('Register_user/',register_user,name='Register_User'),
    path('Signup_user/', signup_user,name='Signup_user'),
    path('Signout_user/', sign_out_user,name='Signout_user'),
    path('Profile_user/', profile_user, name='Profile_user'),
    path('ChangePassword/', change_password, name='ChangePassword'),
    path('SavePersonalInfo/', save_personal_info, name='SavePersonalInfo'),
    path('SaveOtherDetails/', save_other_details, name='SaveOtherDetails'),
    path('SaveAcademicDetails/', save_academic_details,name='SaveAcademicDetails'),
    path('SaveUserProfilePic/', save_user_profile_pic, name='SaveUserProfilePic'),
    path('UpdateProfilePicture/', update_profile_picture,name='UpdateProfilePicture'),
    path('GetCitysDistrictList/', get_citys_district_list, name='GetCitysDistrictList'),
    path('GetSubCastList/', get_sub_cast_list, name='GetSubCastList'),
    path('GetStreamorFieldList/', get_stream_or_field_list, name='GetStreamorFieldList'),
    path('GetDegreeStreamorFieldList/', get_degree_stream_or_field_list, name='GetDegreeStreamorFieldList'),
    path('ForgotPassword/', forgot_password, name='ForgotPassword'),
]