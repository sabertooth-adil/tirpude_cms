from django.contrib.auth.models import User
from master_forms.models import *
from authentication.models import *


class BooksPurchase(models.Model):
    """
    This is the Models for Books Purchase or Books Available in the library
    """
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    published_date = models.DateField(max_length=20, blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    no_of_copies = models.IntegerField(blank=True, null=True)
    purchase_date = models.DateField(max_length=30, blank=True, null=True)
    subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.isbn


class BooksIssue(models.Model):
    """
    This is the Models for Books Issue in the library
    """
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_book_purchase = models.ForeignKey(BooksPurchase, blank=True, null=True,
                                         on_delete=models.CASCADE)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    fk_semester = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    fk_section = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    issue_date = models.DateField(max_length=30, blank=True, null=True)
    due_date = models.DateField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.fk_book_purchase.title


class BooksIssueData(models.Model):
    """
    This is the Models for complete or all records of Books Issued in the library
    """
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_book_purchase = models.ForeignKey(BooksPurchase, blank=True, null=True, on_delete=models.CASCADE)
    book_issue_fk = models.CharField(max_length=20, blank=True, null=True)
    fk_course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
    fk_semester = models.ForeignKey(Semester, blank=True, null=True, on_delete=models.CASCADE)
    fk_section = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    issue_date = models.DateField(max_length=30, blank=True, null=True)
    due_date = models.DateField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.fk_book_purchase.title


class BooksReturned(models.Model):
    """
    This is the Models for Books Returned in the library
    """
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_books_issue_data = models.ForeignKey(BooksIssueData, blank=True, null=True, on_delete=models.CASCADE)
    return_date = models.DateField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.fk_books_issue_data.fk_book_purchase.title


class BooksScrapped(models.Model):
    """
    This is the Models for Books Scrapped in the library
    """
    fk_user_info = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    fk_book_purchase = models.ForeignKey(BooksPurchase, blank=True, null=True, on_delete=models.CASCADE)
    scrap_date = models.DateField(max_length=30, blank=True, null=True)
    reason_for_scrap = models.CharField(max_length=200, blank=True, null=True)
    scrap_copies = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.fk_book_purchase.title
