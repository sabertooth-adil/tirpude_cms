from django.contrib import admin
from django.urls import path

from placement.views import company, add_company, edit_company, update_company, delete_company, company_appearances, \
    edit_company_appearances, add_company_visiting_selection_precess_date_time, edit_company_visiting_selection_precess_date_time, \
    update_company_visiting_selection_precess_date_time, delete_company_visiting_selection_precess_date_time, \
    add_company_visiting_job_type_package_job_location, edit_company_visiting_job_type_package_job_location, \
    update_company_visiting_job_type_package_job_location, delete_company_visiting_job_type_package_job_location, \
    add_company_visting_detail, edit_visiting_company_detail, update_company_visting_detail, student_company_appearances, \
    apply_visiting_company_modal_detail, apply_visiting_company, cancel_company_registration, \
    view_visiting_company_detail, view_company_appearances_detail, add_test_result_placement, \
    filter_test_result_by_subject, save_test_result_by_subject, save_all_student_test_result_by_subject, \
    save_placement_status, placement_student_performance, filter_company_appearances, search_student_performance, \
    filter_search_student_performance, student_my_performance, download_excel_file

urlpatterns = [
    path('download-excel-file/', download_excel_file),
    path('company/', company, name='company'),
    path('add-company/', add_company, name='add-company'),
    path('edit-company/', edit_company, name='edit-company'),
    path('update-company/', update_company, name='update-company'),
    path('delete-company/', delete_company, name='delete-company'),
    path('company-appearances/', company_appearances, name='company-appearances'),
    path('edit-company-appearances/(?P<id>\d+)/$', edit_company_appearances,
         name='edit-company-appearances'),
    path('add-company-visiting-selection-precess-date-time/', add_company_visiting_selection_precess_date_time,
         name='add-company-visiting-selection-precess-date-time'),
    path('edit-company-visiting-selection-precess-date-time/',
         edit_company_visiting_selection_precess_date_time,
         name='edit-company-visiting-selection-precess-date-time'),
    path('update-company-visiting-selection-precess-date-time/',
         update_company_visiting_selection_precess_date_time,
         name='update-company-visiting-selection-precess-date-time'),
    path('delete-company-visiting-selection-precess-date-time/',
         delete_company_visiting_selection_precess_date_time,
         name='delete-company-visiting-selection-precess-date-time'),
    path('add-company-visiting-job-type-package-job-location/',
         add_company_visiting_job_type_package_job_location,
         name='add-company-visiting-job-type-package-job-location'),
    path('edit-company-visiting-job-type-package-job-location/',
         edit_company_visiting_job_type_package_job_location,
         name='edit-company-visiting-job-type-package-job-location'),
    path('update-company-visiting-job-type-package-job-location/',
         update_company_visiting_job_type_package_job_location,
         name='update-company-visiting-job-type-package-job-location'),
    path('delete-company-visiting-job-type-package-job-location/',
         delete_company_visiting_job_type_package_job_location,
         name='delete-company-visiting-job-type-package-job-location'),
    path('add-company-visting-detail/', add_company_visting_detail, name='add-company-visting-detail'),
    path('edit-visiting-company-detail/', edit_visiting_company_detail,
         name='edit-visiting-company-detail'),
    path('update-company-visting-detail/', update_company_visting_detail,
         name='update-company-visting-detail'),
    path('student-company-appearances/', student_company_appearances, name='student-company-appearances'),
    path('apply-visiting-company-modal-detail/', apply_visiting_company_modal_detail,
         name='apply-visiting-company-modal-detail'),
    path('apply-visiting-company/', apply_visiting_company, name='apply-visiting-company'),
    path('cancel-company-registration/', cancel_company_registration,
         name='cancel-company-registration'),
    path('view-visiting-company-detail/(?P<id>\d+)/$', view_visiting_company_detail,
         name='view-visiting-company-detail'),
    path('view-company-appearances-detail/(?P<id>\d+)/$', view_company_appearances_detail,
         name='view-company-appearances-detail'),
    path('add-test-result-placement/(?P<id>\d+)/$', add_test_result_placement,
         name='add-test-result-placement'),
    path('filter-test-result-by-subject/', filter_test_result_by_subject,
         name='filter-test-result-by-subject'),
    path('save-test-result-by-subject/', save_test_result_by_subject,
         name='save-test-result-by-subject'),
    path('save-all-student-test-result-by-subject/', save_all_student_test_result_by_subject,
         name='save-all-student-test-result-by-subject'),
    path('save-placement-status/', save_placement_status, name='save-placement-status'),
    path('placement-student-performance/(?P<id>\d+)/$', placement_student_performance,
         name='placement-student-performance'),
    path('filter-company-appearances/', filter_company_appearances,
         name='filter-company-appearances'),
    path('search-student-performance/', search_student_performance, name='search-student-performance'),
    path('filter-search-student-performance/', filter_search_student_performance,
         name='filter-search-student-performance'),
    path('student-my-performance/', student_my_performance, name='student-my-performance'),
]