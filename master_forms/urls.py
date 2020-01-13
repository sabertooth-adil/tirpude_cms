from django.urls import path
from master_forms import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('subject-views/', views.subject_views, name='subject_views'),
    path('delete-subject/', views.delete_subject, name='DeleteSubject'),
    path('edit-subject/', views.edit_subject, name='EditSubject'),
    path('add-subject/', views.add_subject, name='AddSubject'),
    path('update-subject/', views.update_subject, name='UpdateSubject'),

    path('course-views/', views.course_views, name='course_views'),
    path('delete-course/', views.delete_course, name='delete_course'),
    path('edit-course/', views.edit_course, name='edit_course'),
    path('add-course/', views.add_course, name='add_course'),
    path('update-course/', views.update_course, name='update_course'),

    path('stream-or-field/', views.stream_or_field, name='stream_or_field'),
    path('delete-stream-or-field/', views.delete_stream_or_field, name='delete_stream_or_field'),
    path('edit-stream-or-field/', views.edit_stream_or_field, name='edit_stream_or_field'),
    path('add-stream-or-field/', views.add_stream_or_field, name='add_stream_or_field'),
    path('update-stream-or-field/', views.update_stream_or_field, name='update_stream_or_field'),

    path('degree-views/', views.degree_views, name='degree_views'),
    path('delete-degree/', views.delete_degree, name='delete_degree'),
    path('edit-degree/', views.edit_degree, name='edit_degree'),
    path('add-degree/', views.add_degree, name='add_degree'),
    path('update-degree/', views.update_degree, name='update_degree'),

    path('degree-stream-or-field/', views.degree_stream_or_field, name='degree_stream_or_field'),
    path('delete-degree-stream-or-field/', views.delete_degree_stream_or_field, name='delete_degree_stream_or_field'),
    path('edit-degree-stream-or-field/', views.edit_degree_stream_or_field, name='edit_degree_stream_or_field'),
    path('add-degree-stream-or-field/', views.add_degree_stream_or_field, name='add_degree_stream_or_field'),
    path('update-degree-stream-or-field/', views.update_degree_stream_or_field, name='update_degree_stream_or_field'),

    path('semester-views/', views.semester_views, name='semester_views'),
    path('add-semester/', views.add_semester, name='add_semester'),
    path('edit-semester/', views.edit_semester, name='edit_semester'),
    path('update-semester/', views.update_semester, name='update_semester'),
    path('delete-semester/', views.delete_semester, name='delete_semester'),

    path('section-view/', views.section_view, name='section_view'),
    path('add-section/', views.add_section, name='add_section'),
    path('edit-section/', views.edit_section, name='edit_section'),
    path('update-section/', views.update_section, name='update_section'),
    path('delete-section/', views.delete_section, name='delete_section'),

    path('category-views/', views.category_views, name='category_views'),
    path('add-category/', views.add_category, name='add_category'),
    path('edit-category/', views.edit_category, name='edit_category'),
    path('update-category/', views.update_category, name='update_category'),
    path('delete-category/', views.delete_category, name='delete_category'),

    path('reserved-category-views/', views.reserved_category_views, name='reserved_category_views'),
    path('add-reserved-category/', views.add_reserved_category, name='add_reserved_category'),
    path('edit-reserved-category/', views.edit_reserved_category, name='edit_reserved_category'),
    path('update-reserved-category/', views.update_reserved_category, name='update_reserved_category'),
    path('delete-reserved-category/', views.delete_reserved_category, name='delete_reserved_category'),

    path('apply-concession/', views.apply_concession, name='apply_concession'),
    path('add-concession/', views.add_concession, name='add_concession'),
    path('edit-concession/', views.edit_concession, name='edit_concession'),
    path('update-concession/', views.update_concession, name='update_concession'),
    path('delete-concession/', views.delete_concession, name='delete_concession'),

    path('caste/', views.caste, name='caste'),
    path('add-caste/', views.add_caste, name='add_caste'),
    path('edit-caste/', views.edit_caste, name='edit_caste'),
    path('update-caste/', views.update_caste, name='update_caste'),
    path('delete-caste/', views.delete_caste, name='delete_caste'),

    path('sub_caste/', views.sub_caste, name='sub_caste'),
    path('add-sub-caste/', views.add_sub_caste, name='add_sub_caste'),
    path('edit-sub-caste/', views.edit_sub_caste, name='edit_sub_caste'),
    path('update-sub-caste/', views.update_sub_caste, name='update_sub_caste'),
    path('delete-sub-caste/', views.delete_sub_caste, name='delete_sub_caste'),

    path('state/', views.state, name='state'),
    path('add-state/', views.add_state, name='add_state'),
    path('edit-state/', views.edit_state, name='edit_state'),
    path('update-state/', views.update_state, name='update_state'),
    path('delete-state/', views.delete_state, name='delete_state'),

    path('city-views/', views.city_views, name='city_views'),
    path('add-city/', views.add_city, name='add_city'),
    path('edit-city/', views.edit_city, name='edit_city'),
    path('update-city/', views.update_city, name='update_city'),
    path('delete-city/', views.delete_city, name='delete_city'),

    path('district/', views.district, name='district'),
    path('add-district/', views.add_district, name='add_district'),
    path('edit-district/', views.edit_district, name='edit_district'),
    path('update-district/', views.update_district, name='update_district'),
    path('delete-district/', views.delete_district, name='delete_district'),

    path('academic-session/', views.academic_session, name='academic_session'),
    path('add-academic-session/', views.add_academic_session, name='add_academic_session'),
    path('edit-academic-session/', views.edit_academic_session, name='edit_academic_session'),
    path('update-academic-session/', views.update_academic_session, name='update_academic_session'),
    path('delete-academic-session/', views.delete_academic_session, name='delete_academic_session'),
]
