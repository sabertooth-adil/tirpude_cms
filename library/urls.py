from django.contrib import admin
from django.urls import path
from library import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('books_purchase/', views.books_purchase, name='books_purchase'),
                  path('add_books_purchase/', views.add_books_purchase, name='add_books_purchase'),
                  path('delete_books_purchase/', views.delete_books_purchase, name='delete_books_purchase'),
                  path('edit_books_purchase/', views.edit_books_purchase, name='edit_books_purchase'),
                  path('update_books_purchase/', views.update_books_purchase, name='update_books_purchase'),
                  path('filter_books_purchase/', views.filter_books_purchase, name='filter_books_purchase'),
                  path('purchase_change_title/', views.purchase_change_title, name='purchase_change_title'),
                  path('purchase_change_author_title/', views.purchase_change_author_title,
                       name='purchase_change_author_title'),

                  path('books_issue/', views.books_issue, name='books_issue'),
                  path('delete_issued_books/', views.delete_issued_books, name='delete_issued_books'),
                  path('issue_filter_student_name/', views.issue_filter_student_name, name='issue_filter_student_name'),
                  path('append_search_purchase_books_details/', views.append_search_purchase_books_details,
                       name='append_search_purchase_books_details'),
                  path('add_issue_books/', views.add_issue_books, name='add_issue_books'),
                  path('show_particular_students_books/', views.show_particular_students_books,
                       name='show_particular_students_books'),
                  path('delete_issue_books/', views.delete_issue_books, name='delete_issue_books'),

                  path('library_copies_count/', views.library_copies_count, name='library_copies_count'),
                  path('filter_books_issue/', views.filter_books_issue, name='filter_books_issue'),

                  path('issue_books_filter_change_title_author/', views.issue_books_filter_change_title_author,
                       name='issue_books_filter_change_title_author'),
                  path('issue_books_filter_change_title/', views.issue_books_filter_change_title,
                       name='issue_books_filter_change_title'),
                  path('issue_books_modal_filter_change_title_author/',
                       views.issue_books_modal_filter_change_title_author,
                       name='issue_books_modal_filter_change_title_author'),
                  path('issue_books_modal_filter_change_title/', views.issue_books_modal_filter_change_title,
                       name='issue_books_modal_filter_change_title'),
                  path('filter_modal_books_issue/', views.filter_modal_books_issue, name='filter_modal_books_issue'),

                  path('books_return/', views.books_return, name='books_return'),
                  path('append_search_books_issue_details/', views.append_search_books_issue_details,
                       name='append_search_books_issue_details'),
                  path('add_return_books/', views.add_return_books, name='add_return_books'),
                  path('filter_modal_books_return/', views.filter_modal_books_return, name='filter_modal_books_return'),
                  path('filter_books_return/', views.filter_books_return, name='filter_books_return'),
                  path('books_return_filter_change_title_author/', views.books_return_filter_change_title_author,
                       name='books_return_filter_change_title_author'),
                  path('books_return_filter_change_title/', views.books_return_filter_change_title,
                       name='books_return_filter_change_title'),
                  path('books_return_modal_filter_change_title_author/',
                       views.books_return_modal_filter_change_title_author,
                       name='books_return_modal_filter_change_title_author'),
                  path('books_return_modal_filter_change_title/', views.books_return_modal_filter_change_title,
                       name='books_return_modal_filter_change_title'),
                  path('books_scrap/', views.books_scrap, name='books_scrap'),
                  path('edit_books_scrap/', views.edit_books_scrap, name='edit_books_scrap'),
                  path('add_scrap_books/', views.add_scrap_books, name='add_scrap_books'),
                  path('books_scrap_filter_change_title/', views.books_scrap_filter_change_title,
                       name='books_scrap_filter_change_title'),
                  path('books_scrap_filter_change_title_author/', views.books_scrap_filter_change_title_author,
                       name='books_scrap_filter_change_title_author'),
                  path('filter_books_scrap/', views.filter_books_scrap, name='filter_books_scrap'),
                  path('filter_modal_books_scrap/', views.filter_modal_books_scrap, name='filter_modal_books_scrap'),
                  path('books_scrap_modal_filter_change_title_author/',
                       views.books_scrap_modal_filter_change_title_author,
                       name='books_scrap_modal_filter_change_title_author'),
                  path('books_scrap_modal_filter_change_title/', views.books_scrap_modal_filter_change_title,
                       name='books_scrap_modal_filter_change_title'),

                  path('available_books_report/', views.available_books_report, name='available_books_report'),
                  path('issued_books_report/', views.issued_books_report, name='issued_books_report'),
                  path('returned_books_report/', views.returned_books_report, name='returned_books_report'),
                  path('scrapped_books_report/', views.scrapped_books_report, name='scrapped_books_report'),
                  path('filter_available_books_report/', views.filter_available_books_report,
                       name='filter_available_books_report'),
                  path('filter_issued_books_report/', views.filter_issued_books_report,
                       name='filter_issued_books_report'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
