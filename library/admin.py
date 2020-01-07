from django.contrib import admin
from .models import *


# Register your models here.


class BooksPurchaseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'fk_user_info', 'title', 'author', 'publisher', 'published_date', 'isbn', 'price', 'no_of_copies',
        'purchase_date', 'subject')


admin.site.register(BooksPurchase, BooksPurchaseAdmin)


class BooksIssueAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'fk_user_info', 'fk_book_purchase', 'fk_course', 'fk_semester', 'fk_section', 'issue_date', 'due_date')


admin.site.register(BooksIssue, BooksIssueAdmin)


class BooksIssueDataAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'fk_user_info', 'fk_book_purchase', 'book_issue_fk', 'fk_course', 'fk_semester', 'fk_section',
        'issue_date',
        'due_date'
    )


admin.site.register(BooksIssueData, BooksIssueDataAdmin)


class BooksReturnedAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_user_info', 'fk_books_issue_data', 'return_date')


admin.site.register(BooksReturned, BooksReturnedAdmin)


class BooksScrappedAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_user_info', 'fk_book_purchase', 'scrap_date', 'reason_for_scrap', 'scrap_copies')


admin.site.register(BooksScrapped, BooksScrappedAdmin)
