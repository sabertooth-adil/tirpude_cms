from django.urls import path
from library import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('book-purchase/', views.book_purchase, name='book_purchase'),
                  path('filter-title/', views.filter_title, name='filter_title'),
                  path('filter-author-title/', views.filter_author_title, name='filter_author_title'),
                  path('add-book-purchase/', views.add_book_purchase, name='add_book_purchase'),
                  path('delete-book-purchase/', views.delete_book_purchase, name='delete_book_purchase'),
                  path('edit-book-purchase/', views.edit_book_purchase, name='edit_book_purchase'),
                  path('update-book-purchase/', views.update_book_purchase, name='update_book_purchase'),
                  path('filter-book-purchase/', views.filter_book_purchase, name='filter_book_purchase'),

                  path('book-issue/', views.book_issue, name='book_issue'),
                  path('delete-issued-book/', views.delete_issued_book, name='delete_issued_book'),
                  path('issue-filter-student-name/', views.issue_filter_student_name, name='issue_filter_student_name'),
                  path('append-search-purchase-book-details/', views.append_search_purchase_book_details,
                       name='append_search_purchase_books_details'),
                  path('add-issue-book/', views.add_issue_book, name='add_issue_book'),
                  path('show-particular-student-book/', views.show_particular_student_book,
                       name='show_particular_student_book'),
                  path('delete-issue-book/', views.delete_issue_book, name='delete_issue_book'),
                  path('library-copies-count/', views.library_copies_count, name='library_copies_count'),
                  path('filter-book-issue/', views.filter_book_issue, name='filter_book_issue'),
                  path('filter-modal-book-issue/', views.filter_modal_book_issue, name='filter_modal_book_issue'),

                  path('book-return/', views.book_return, name='book_return'),
                  path('append-search-book-issue-details/', views.append_search_book_issue_details,
                       name='append_search_book_issue_details'),
                  path('add-return-book/', views.add_return_book, name='add_return_book'),
                  path('filter-modal-book-return/', views.filter_modal_book_return, name='filter_modal_book_return'),
                  path('filter-book-return/', views.filter_book_return, name='filter_book_return'),

                  path('book-scrap/', views.book_scrap, name='book_scrap'),
                  path('edit-book-scrap/', views.edit_book_scrap, name='edit_book_scrap'),
                  path('add-scrap-book/', views.add_scrap_book, name='add_scrap_book'),
                  path('filter-book-scrap/', views.filter_book_scrap, name='filter_book_scrap'),
                  path('filter-modal-book-scrap/', views.filter_modal_book_scrap, name='filter_modal_book_scrap'),

                  path('available-book-report/', views.available_book_report, name='available_book_report'),
                  path('issued-book-report/', views.issued_book_report, name='issued_book_report'),
                  path('returned-book-report/', views.returned_book_report, name='returned_book_report'),
                  path('scrapped-book-report/', views.scrapped_book_report, name='scrapped_book_report'),
                  path('filter-available-book-report/', views.filter_available_book_report,
                       name='filter_available_books_report'),
                  path('filter-issued-book-report/', views.filter_issued_book_report,
                       name='filter_issued_book_report'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
