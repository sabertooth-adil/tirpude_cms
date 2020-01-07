from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
import pandas as pd


def books_purchase(request):
    """
    Page for book purchase
    """
    session = request.session.get('user_id')
    user_info_obj = UserInfo.objects.get(id=session)
    user_operations_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
    books_purchase_obj = BooksPurchase.objects.all().order_by('purchase_date')
    books_subject_obj = Subject.objects.all()
    return render(request, "bookspurchase.html",
                  {"user_info_obj": user_info_obj, "useroperations_obj": user_operations_obj,
                   "books_subject_obj": books_subject_obj,
                   "books_purchase_obj": books_purchase_obj})


@csrf_exempt
def filter_title(request):
    """
    Filtering title by on clicking author
    """
    author = request.POST.get("author")
    if author:
        title_list = list(BooksPurchase.objects.filter(author=author).values_list('id', 'title'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def filter_author_title(request):
    """
    Filtering author and title by on clicking subject
    """
    subject = request.POST.get("subject")
    if subject:
        title_list = list(BooksPurchase.objects.filter(subject_id=subject).values_list('id', 'title', 'author'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def purchase_change_title(request):
    """
    Filtering title by on clicking author
    """
    author = request.POST.get("author")
    if author:
        title_list = list(BooksPurchase.objects.filter(author=author).values_list('id', 'title'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def purchase_change_author_title(request):
    """
    Filtering author and title by on clicking subject
    """
    subject = request.POST.get("subject")
    if subject:
        title_list = list(BooksPurchase.objects.filter(subject_id=subject).values_list('id', 'title', 'author'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def add_books_purchase(request):
    """
    Adding new books in the library
    """
    session = request.session.get('user_id')
    title = request.POST.get("title")
    author = request.POST.get("author")
    publisher = request.POST.get("publisher")
    published_date = datetime.datetime.strptime(str(request.POST.get("published_date")), '%d-%m-%Y').strftime(
        '%Y-%m-%d')
    isbn = request.POST.get("isbn")
    price = request.POST.get("price")
    no_of_copies = request.POST.get("no_of_copies")
    purchase_date = datetime.datetime.strptime(str(request.POST.get("purchase_date")), '%d-%m-%Y').strftime('%Y-%m-%d')
    subject = request.POST.get("subject")
    if request.method == 'POST':
        add_books = BooksPurchase(fk_user_info_id=session, title=title,
                                  author=author, publisher=publisher,
                                  published_date=published_date, isbn=isbn, price=price, no_of_copies=no_of_copies,
                                  purchase_date=purchase_date, subject_id=subject)
        add_books.save()
    return HttpResponse("success")


@csrf_exempt
def delete_books_purchase(request):
    """
    Deleting any books from books purchase
    """
    id = request.POST.get("id")
    books_obj = BooksPurchase.objects.get(id=id)
    books_obj.delete()
    return HttpResponse("success")


@csrf_exempt
def edit_books_purchase(request):
    """
    Editing any details from books purchase
    """
    list = []
    dict = {}
    id = request.POST.get("id")
    books_obj = BooksPurchase.objects.get(id=id)
    dict['id'] = books_obj.id
    dict['title'] = books_obj.title
    dict['author'] = books_obj.author
    dict['publisher'] = books_obj.publisher
    dict['published_date'] = datetime.datetime.strptime(str(books_obj.published_date), '%Y-%m-%d').strftime('%d-%m-%Y')
    dict['isbn'] = books_obj.isbn
    dict['price'] = books_obj.price
    dict['subject'] = books_obj.subject_id
    dict['no_of_copies'] = books_obj.no_of_copies
    dict['purchase_date'] = datetime.datetime.strptime(str(books_obj.purchase_date), '%Y-%m-%d').strftime('%d-%m-%Y')
    list.append(dict)
    return JsonResponse({"list": list})


@csrf_exempt
def update_books_purchase(request):
    """
    Update any details from books purchase
    """
    title_id = request.POST.get("title_id")
    edit_title = request.POST.get("edit_title")
    edit_author = request.POST.get("edit_author")
    edit_publisher = request.POST.get("edit_publisher")
    edit_published_date = request.POST.get("edit_published_date")
    edit_isbn = request.POST.get("edit_isbn")
    edit_no_of_copies = request.POST.get("edit_no_of_copies")
    edit_price = request.POST.get("edit_price")
    edit_purchase_date = request.POST.get("edit_purchase_date")
    edit_subject = request.POST.get("edit_subject")
    book_obj = BooksPurchase.objects.get(id=title_id)
    book_obj.title = edit_title
    book_obj.author = edit_author
    book_obj.publisher = edit_publisher
    book_obj.published_date = datetime.datetime.strptime(str(edit_published_date), '%d-%m-%Y').strftime('%Y-%m-%d')
    book_obj.isbn = edit_isbn
    book_obj.no_of_copies = edit_no_of_copies
    book_obj.price = edit_price
    book_obj.subject_id = edit_subject
    book_obj.purchase_date = datetime.datetime.strptime(str(edit_purchase_date), '%d-%m-%Y').strftime('%Y-%m-%d')
    book_obj.save()
    return HttpResponse("success")


@csrf_exempt
def filter_books_purchase(request):
    """
    Filter for books purchase
    """
    author = request.POST.get("author")
    title = request.POST.get("title")
    subject = request.POST.get("subject")
    isbn = request.POST.get("isbn")
    fromdate = request.POST.get("from_date")
    todate = request.POST.get("to_date")
    print("fromdate=", fromdate)
    print("todate=", todate)
    if fromdate:
        fromdate = datetime.datetime.strptime(str(request.POST.get("from_date")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if todate:
        todate = datetime.datetime.strptime(str(request.POST.get("to_date")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if author and title and isbn and subject and fromdate and todate:
        books_obj = BooksPurchase.objects.filter(author=author, title=title, isbn=isbn, subject_id=subject,
                                                 purchase_date__gte=fromdate, purchase_date__lte=todate)
    elif fromdate and isbn and title and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, title=title, author=author)
    elif todate and fromdate and isbn and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn,
                                                 author=author)
    elif todate and fromdate and isbn and title:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn,
                                                 title=title)
    elif todate and fromdate and isbn and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn,
                                                 subject_id=subject)
    elif subject and author and title:
        books_obj = BooksPurchase.objects.filter(subject_id=subject, author=author, title=title)
    elif isbn and title and author:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, title=title, author=author)
    elif fromdate and isbn and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, author=author)
    elif fromdate and isbn and title:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, title=title)
    elif fromdate and isbn and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, subject_id=subject)
    elif todate and title and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, title=title, author=author)
    elif todate and title and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, title=title, subject_id=subject)
    elif todate and isbn and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn, author=author)
    elif todate and isbn and title:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn, title=title)
    elif todate and isbn and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn, subject_id=subject)
    elif todate and fromdate and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, author=author)
    elif todate and fromdate and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate,
                                                 subject=subject)
    elif todate and fromdate and title:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, title=title)
    elif todate and fromdate and isbn:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn)
    elif author and subject:
        books_obj = BooksPurchase.objects.filter(author=author, subject_id=subject)
    elif subject and title:
        books_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
    elif author and title:
        books_obj = BooksPurchase.objects.filter(author=author, title=title)
    elif subject and title:
        books_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
    elif title and author:
        books_obj = BooksPurchase.objects.filter(title=title, author=author)
    elif title and subject:
        books_obj = BooksPurchase.objects.filter(title=title, subject_id=subject)
    elif isbn and author:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, author=author)
    elif isbn and title:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, title=title)
    elif isbn and subject:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, subject_id=subject)
    elif fromdate and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, author=author)
    elif fromdate and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, subject_id=subject)
    elif fromdate and title:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, title=title)
    elif fromdate and isbn:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn)
    elif todate and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, author=author)
    elif todate and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, subject_id=subject)
    elif todate and title:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, title=title)
    elif todate and isbn:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn)
    elif todate and fromdate:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate)
    elif author:
        books_obj = BooksPurchase.objects.filter(author=author)
    elif title:
        books_obj = BooksPurchase.objects.filter(title=title)
    elif subject:
        books_obj = BooksPurchase.objects.filter(subject_id=subject)
    elif isbn:
        books_obj = BooksPurchase.objects.filter(isbn=isbn)
    elif fromdate:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate)
    elif todate:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate)
    else:
        books_obj = BooksPurchase.objects.all()
    render_string = render_to_string("purchasebookfile.html", {"books_obj": books_obj})
    return HttpResponse(render_string)


def books_issue(request):
    """
    Page for book issue
    """
    session = request.session.get('user_id')
    user_info_obj = UserInfo.objects.get(id=session)
    user_operations_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
    books_purchase_obj = BooksPurchase.objects.all().order_by('published_date')
    books_issue_obj = BooksIssue.objects.all().order_by('issue_date')
    books_issue_data_obj = BooksIssueData.objects.all().order_by('issue_date')
    books_subject_obj = Subject.objects.all()
    course_obj = Course.objects.all()
    semesters_obj = Semester.objects.all()
    sections_obj = Section.objects.all()
    return render(request, "booksissue.html",
                  {"useroperations_obj": user_operations_obj, "books_data_obj": books_issue_data_obj,
                   "books_subject_obj": books_subject_obj,
                   "user_info_obj": user_info_obj, "books_issue_obj": books_issue_obj,
                   "books_purchase_obj": books_purchase_obj, "course_obj": course_obj,
                   "semesters_obj": semesters_obj, "sections_obj": sections_obj})


@csrf_exempt
def delete_issue_books(request):
    """
    Delete issued books while issuing any new books to any student
    """
    id = request.POST.get("id")
    books_issue_obj = BooksIssue.objects.get(id=id)
    books_issue_obj.delete()
    books_issue_data_obj = BooksIssueData.objects.get(book_issue_fk=id)
    books_issue_data_obj.delete()
    student_name = request.POST.get("student_name")
    edit_title = request.POST.get("title")
    books_no_copies = BooksPurchase.objects.get(title=edit_title).no_of_copies
    issue_no_copies = BooksIssue.objects.filter(fk_book_purchase__title=edit_title).count()
    remaining_copies = books_no_copies - issue_no_copies
    book_issue_copies_obj = BooksIssue.objects.filter(fk_user_info_id=student_name).count()
    return JsonResponse({"book_issue_copies_obj": book_issue_copies_obj, "books_no_copies": books_no_copies,
                         "issue_no_copies": issue_no_copies, "remaining_copies": remaining_copies})


@csrf_exempt
def issue_filter_student_name(request):
    """
    Filtering student name according to course
    """
    course = request.POST.get("edit_course")
    if course:
        student_list = list(
            AcademicInfo.objects.filter(fk_course_id=course).values_list('fk_user_info', 'fk_user_info__first_name',
                                                                         'fk_user_info__last_name'))
    else:
        pass
    return HttpResponse(json.dumps(student_list))


@csrf_exempt
def append_search_purchase_books_details(request):
    """
    Append book purchase details in the field
    """
    list = []
    dict = {}
    id = request.POST.get("id")
    books_obj = BooksPurchase.objects.get(id=id)
    dict['id'] = books_obj.id
    dict['title'] = books_obj.title
    dict['author'] = books_obj.author
    dict['publisher'] = books_obj.publisher
    dict['subject'] = books_obj.subject.subjects
    dict['isbn'] = books_obj.isbn
    list.append(dict)
    return JsonResponse({"list": list})


@csrf_exempt
def add_issue_books(request):
    """
    Adding issue books to database
    """
    session = request.session.get('user_id')
    user_info_obj = UserInfo.objects.get(id=session)
    user_operations_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
    edit_title = request.POST.get("title")
    book_purchase_id = request.POST.get("book_purchase_id")
    course = request.POST.get("course")
    semester = request.POST.get("semester")
    section = request.POST.get("section")
    student_name = request.POST.get("student_name")
    date_of_issue = datetime.datetime.strptime(str(request.POST.get("date_of_issue")), '%d-%m-%Y').strftime('%Y-%m-%d')
    due_date = pd.to_datetime(date_of_issue) + pd.Timedelta(days=15)
    books_obj = BooksIssue.objects.filter(fk_user_info_id=student_name)
    if request.method == 'POST':
        if books_obj.count() < 6:
            if not BooksIssue.objects.filter(fk_user_info_id=student_name, fk_book_purchase__title=edit_title).exists():
                add_books = BooksIssue(fk_book_purchase_id=book_purchase_id, due_date=due_date, fk_course_id=course,
                                       fk_semester_id=semester, fk_section_id=section, fk_user_info_id=student_name,
                                       issue_date=date_of_issue)
                add_books.save()
                data_add_books = BooksIssueData(fk_book_purchase_id=book_purchase_id, due_date=due_date,
                                                fk_course_id=course,
                                                fk_semester_id=semester, fk_section_id=section,
                                                fk_user_info_id=student_name,
                                                issue_date=date_of_issue, book_issue_fk=add_books.id)
                data_add_books.save()
                scrap_copies_no = 0
                books_scrapped_obj = BooksScrapped.objects.filter(fk_book_purchase__title=edit_title)
                for i in books_scrapped_obj:
                    scrap_copies_no += int(i.scrap_copies)
                print("books_scrapped_obj", scrap_copies_no)
                books_no_copies = BooksPurchase.objects.get(title=edit_title).no_of_copies
                actual_copies = books_no_copies - scrap_copies_no
                print("actual_copies", actual_copies)
                issue_no_copies = BooksIssue.objects.filter(fk_book_purchase__title=edit_title).count()
                remaining_copies = actual_copies - issue_no_copies
                books_obj = BooksIssue.objects.filter(fk_user_info_id=student_name)
                book_issue_copies_obj = BooksIssue.objects.filter(fk_user_info_id=student_name).count()
                render_string = render_to_string("appendissueadd.html",
                                                 {"user_operations_obj": user_operations_obj,
                                                  "book_issue_copies_obj": book_issue_copies_obj,
                                                  "books_obj": books_obj,
                                                  "books_no_copies": actual_copies, "issue_no_copies": issue_no_copies,
                                                  "remaining_copies": remaining_copies})
                return HttpResponse(render_string)
            else:
                return HttpResponse("same_books_not_exits")
        else:
            return HttpResponse("fail")


@csrf_exempt
def show_particular_students_books(request):
    """
    Showing particular issued books of student in table while issuing books
    """
    student_name = request.POST.get("student_name")
    edit_title = request.POST.get("title")
    scrap_copies_no = 0
    books_scrapped_obj = BooksScrapped.objects.filter(fk_book_purchase__title=edit_title)
    for i in books_scrapped_obj:
        scrap_copies_no += int(i.scrap_copies)
    books_no_copies = BooksPurchase.objects.get(title=edit_title).no_of_copies
    actual_copies = books_no_copies - scrap_copies_no
    issue_no_copies = BooksIssue.objects.filter(fk_book_purchase__title=edit_title).count()
    remaining_copies = actual_copies - issue_no_copies
    books_obj = BooksIssue.objects.filter(fk_user_info_id=student_name)
    book_issue_copies_obj = BooksIssue.objects.filter(fk_user_info_id=student_name).count()
    render_string = render_to_string("appendissueadd.html",
                                     {"book_issue_copies_obj": book_issue_copies_obj, "books_obj": books_obj,
                                      "books_no_copies": actual_copies, "issue_no_copies": issue_no_copies,
                                      "remaining_copies": remaining_copies})
    return HttpResponse(render_string)


@csrf_exempt
def delete_issued_books(request):
    """
    Delete issued books (i.e BooksIssueData) from Table
    """
    id = request.POST.get("id")
    books_obj = BooksIssueData.objects.get(id=id)
    books_obj.delete()
    return HttpResponse("success")


@csrf_exempt
def library_copies_count(request):
    """
    For showing the counts of total copies,issued copies,remaining copies of particular book in the library
    """
    edit_title = request.POST.get("edit_title")
    scrap_copies_no = 0
    books_scrapped_obj = BooksScrapped.objects.filter(fk_book_purchase__title=edit_title)
    for i in books_scrapped_obj:
        scrap_copies_no += int(i.scrap_copies)
    books_no_copies = BooksPurchase.objects.get(title=edit_title).no_of_copies
    actual_copies = books_no_copies - scrap_copies_no
    issue_no_copies = BooksIssue.objects.filter(fk_book_purchase__title=edit_title).count()
    remaining_copies = actual_copies - issue_no_copies
    return JsonResponse(
        {"books_no_copies": actual_copies, "issue_no_copies": issue_no_copies, "remaining_copies": remaining_copies})


@csrf_exempt
def issue_books_filter_change_title(request):
    """
    Filtering title by clicking author in filter
    """
    author = request.POST.get("author")
    if author:
        title_list = list(BooksPurchase.objects.filter(author=author).values_list('id', 'title'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def issue_books_filter_change_title_author(request):
    """
    Filtering title and author by clicking subject in filter
    """
    subject = request.POST.get("subject")
    if subject:
        title_list = list(BooksPurchase.objects.filter(subject_id=subject).values_list('id', 'title', 'author'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def issue_books_modal_filter_change_title(request):
    """
    Filtering title by clicking author in modal filter
    """
    author = request.POST.get("author")
    if author:
        title_list = list(BooksPurchase.objects.filter(author=author).values_list('id', 'title'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def issue_books_modal_filter_change_title_author(request):
    """
    Filtering title and author by clicking subject in modal filter
    """
    subject = request.POST.get("subject")
    if subject:
        title_list = list(BooksPurchase.objects.filter(subject_id=subject).values_list('id', 'title', 'author'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def filter_modal_books_issue(request):
    """
    Filter modal table of book issue
    """
    author = request.POST.get("author")
    title = request.POST.get("title")
    subject = request.POST.get("subject")
    isbn = request.POST.get("isbn")
    fromdate = request.POST.get("fromdate")
    todate = request.POST.get("todate")

    if fromdate:
        fromdate = datetime.datetime.strptime(str(request.POST.get("fromdate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if todate:
        todate = datetime.datetime.strptime(str(request.POST.get("todate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if author and title and isbn and subject and fromdate and todate:
        books_obj = BooksPurchase.objects.filter(author=author, title=title, isbn=isbn, subject_id=subject,
                                                 published_date__gte=fromdate, published_date__lte=todate)
    elif fromdate and isbn and title and author:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, title=title, author=author)
    elif todate and fromdate and isbn and author:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn,
                                                 author=author)
    elif todate and fromdate and isbn and title:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn,
                                                 title=title)
    elif todate and fromdate and isbn and subject:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn,
                                                 subject_id=subject)
    elif subject and title and author:
        books_obj = BooksPurchase.objects.filter(subject_id=subject, title=title, author=author)
        print("books_obj", books_obj)
    elif isbn and title and author:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, title=title, author=author)
    elif fromdate and isbn and author:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, author=author)
    elif fromdate and isbn and title:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, title=title)
    elif fromdate and isbn and subject:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, subject_id=subject)
    elif todate and title and author:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, title=title, author=author)
    elif todate and title and subject:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, title=title, subject_id=subject)
    elif todate and isbn and author:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn, author=author)
    elif todate and isbn and title:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn, title=title)
    elif todate and isbn and subject:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn, subject_id=subject)
    elif todate and fromdate and author:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate,
                                                 author=author)
    elif todate and fromdate and subject:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate,
                                                 subject_id=subject)
    elif todate and fromdate and title:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, title=title)
    elif todate and fromdate and isbn:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn)
    elif author and subject:
        books_obj = BooksPurchase.objects.filter(author=author, subject_id=subject)
    elif subject and title:
        books_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
    elif author and title:
        books_obj = BooksPurchase.objects.filter(author=author, title=title)
    elif subject and title:
        books_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
    elif title and author:
        books_obj = BooksPurchase.objects.filter(title=title, author=author)
    elif title and subject:
        books_obj = BooksPurchase.objects.filter(title=title, subject_id=subject)
    elif isbn and author:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, author=author)
    elif isbn and title:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, title=title)
    elif isbn and subject:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, subject_id=subject)
    elif fromdate and author:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, author=author)
    elif fromdate and subject:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, subject_id=subject)
    elif fromdate and title:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, title=title)
    elif fromdate and isbn:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn)
    elif todate and author:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, author=author)
    elif todate and subject:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, subject_id=subject)
    elif todate and title:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, title=title)
    elif todate and isbn:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn)
    elif todate and fromdate:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate)
    elif author:
        books_obj = BooksPurchase.objects.filter(author=author)
    elif title:
        books_obj = BooksPurchase.objects.filter(title=title)
    elif subject:
        books_obj = BooksPurchase.objects.filter(subject_id=subject)
    elif isbn:
        books_obj = BooksPurchase.objects.filter(isbn=isbn)
    elif fromdate:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate)
    elif todate:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate)
    else:
        books_obj = BooksPurchase.objects.all()
    render_string = render_to_string("issuedialogbookfile.html", {"bookss_obj": books_obj})
    return HttpResponse(render_string)


@csrf_exempt
def filter_books_issue(request):
    """
    Filter book issue table
    """
    author = request.POST.get("author")
    title = request.POST.get("title")
    isbn = request.POST.get("isbn")
    subject = request.POST.get("subject")
    fromdate = request.POST.get("fromdate")
    todate = request.POST.get("todate")

    if fromdate:
        fromdate = datetime.datetime.strptime(str(request.POST.get("fromdate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if todate:
        todate = datetime.datetime.strptime(str(request.POST.get("todate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if author and title and isbn and subject and fromdate and todate:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__author=author, fk_book_purchase__title=title,
                                                  fk_book_purchase__isbn=isbn, fk_book_purchase__subject=subject,
                                                  issue_date__gte=fromdate, issue_date__lte=todate)
    elif fromdate and isbn and title and author:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__title=title, fk_book_purchase__author=author)
    elif todate and fromdate and isbn and author:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__author=author)
    elif todate and fromdate and isbn and title:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__title=title)
    elif todate and fromdate and isbn and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__subject=subject)
    elif subject and title and author:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__subject=subject, fk_book_purchase__title=title,
                                                  fk_book_purchase__author=author).order_by('issue_date')
    elif isbn and title and author:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title,
                                                  fk_book_purchase__author=author)
    elif fromdate and isbn and author:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__author=author)
    elif fromdate and isbn and title:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__title=title).order_by('issue_date')
    elif fromdate and isbn and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__subject=subject).order_by('issue_date')
    elif todate and title and author:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title,
                                                  fk_book_purchase__author=author).order_by('issue_date')
    elif todate and title and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title,
                                                  fk_book_purchase__subject=subject).order_by('issue_date')
    elif todate and isbn and author:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__author=author).order_by('issue_date')
    elif todate and isbn and title:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__title=title).order_by('issue_date')
    elif todate and isbn and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__subject=subject).order_by('issue_date')
    elif todate and fromdate and author:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__author=author).order_by('issue_date')
    elif todate and fromdate and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__subject=subject).order_by('issue_date')
    elif todate and fromdate and title:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__title=title).order_by('issue_date')
    elif todate and fromdate and isbn:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__isbn=isbn).order_by('issue_date')
    elif author and subject:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__author=author,
                                                  fk_book_purchase__subject=subject).order_by('issue_date')
    elif title and author:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__title=title,
                                                  fk_book_purchase__author=author).order_by(
            'issue_date')
    elif title and subject:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__title=title,
                                                  fk_book_purchase__subject=subject).order_by('issue_date')
    elif isbn and author:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__author=author).order_by(
            'issue_date')
    elif isbn and title:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title).order_by(
            'issue_date')
    elif isbn and subject:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__subject=subject).order_by(
            'issue_date')
    elif fromdate and author:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__author=author).order_by(
            'issue_date')
    elif fromdate and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__subject=subject).order_by(
            'issue_date')
    elif fromdate and title:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__title=title).order_by(
            'issue_date')
    elif fromdate and isbn:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn).order_by(
            'issue_date')
    elif todate and author:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__author=author).order_by(
            'issue_date')
    elif todate and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__subject=subject).order_by(
            'issue_date')
    elif todate and title:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title).order_by(
            'issue_date')
    elif todate and isbn:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn).order_by(
            'issue_date')
    elif todate and fromdate:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate).order_by(
            'issue_date')
    elif author:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__author=author).order_by('issue_date')
    elif title:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__title=title).order_by('issue_date')
    elif subject:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__subject=subject).order_by('issue_date')
    elif isbn:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn).order_by('issue_date')
    elif fromdate:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate).order_by('issue_date')
    elif todate:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate).order_by('issue_date')
    else:
        books_obj = BooksIssueData.objects.all()
    render_string = render_to_string("issuedbookfilter.html", {"books_data_obj": books_obj})
    return HttpResponse(render_string)


def books_return(request):
    """
    Page for book return
    """
    session = request.session.get('user_id')
    user_info_obj = UserInfo.objects.get(id=session)
    user_operations_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
    books_purchase_obj = BooksPurchase.objects.all()
    books_issue_obj = BooksIssue.objects.all().order_by('issue_date')
    books_subject_obj = Subject.objects.all()
    course_obj = Course.objects.all()
    semesters_obj = Semester.objects.all()
    sections_obj = Section.objects.all()
    books_returned_obj = BooksReturned.objects.all().order_by('return_date')
    return render(request, "booksreturn.html",
                  {"user_operations_obj": user_operations_obj, "books_returned_obj": books_returned_obj,
                   "books_subject_obj": books_subject_obj,
                   "user_info_obj": user_info_obj, "books_issue_obj": books_issue_obj,
                   "books_purchase_obj": books_purchase_obj,
                   "course_obj": course_obj, "semesters_obj": semesters_obj, "sections_obj": sections_obj})


@csrf_exempt
def books_return_filter_change_title(request):
    """
    Filtering title by clicking author in filter
    """
    author = request.POST.get("author")
    if author:
        title_list = list(BooksPurchase.objects.filter(author=author).values_list('id', 'title'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def books_return_filter_change_title_author(request):
    """
    Filtering title and author by clicking subject in filter
    """
    subject = request.POST.get("subject")
    if subject:
        title_list = list(BooksPurchase.objects.filter(subject_id=subject).values_list('id', 'title', 'author'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def books_return_modal_filter_change_title_author(request):
    """
    Filtering title,author by clicking subject in modal filter
    """
    subject = request.POST.get("subject")
    if subject:
        title_list = list(BooksPurchase.objects.filter(subject_id=subject).values_list('id', 'title', 'author'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def books_return_modal_filter_change_title(request):
    """
    Filtering title by clicking author in modal filter
    """
    author = request.POST.get("author")
    if author:
        title_list = list(BooksPurchase.objects.filter(author=author).values_list('id', 'title'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def append_search_books_issue_details(request):
    """
    Append book issue details in the field
    """
    list = []
    dict = {}
    id = request.POST.get("id")
    print(id)
    books_obj = BooksIssue.objects.get(id=id)
    dict['id'] = books_obj.id
    dict['fk_purchase_id'] = books_obj.fk_book_purchase_id
    dict['title'] = books_obj.fk_book_purchase.title
    dict['author'] = books_obj.fk_book_purchase.author
    dict['publisher'] = books_obj.fk_book_purchase.publisher
    dict['subject'] = books_obj.fk_book_purchase.subject.subjects
    dict['isbn'] = books_obj.fk_book_purchase.isbn
    dict['course'] = books_obj.fk_course.course
    dict['semester'] = books_obj.fk_semester.semester
    dict['section'] = books_obj.fk_section.sections
    dict['issuedate'] = datetime.datetime.strptime(str(books_obj.issue_date), '%Y-%m-%d').strftime('%d-%m-%Y')
    dict['duedate'] = datetime.datetime.strptime(str(books_obj.due_date), '%Y-%m-%d').strftime('%d-%m-%Y')
    dict['studentname'] = books_obj.fk_user_info.first_name + ' ' + books_obj.fk_user_info.last_name
    dict['studentname_id'] = books_obj.fk_user_info_id
    list.append(dict)
    return JsonResponse({"list": list})


@csrf_exempt
def add_return_books(request):
    """
    Adding return books to database
    """
    student_name_id = request.POST.get("student_name_id")
    book_issue_id = request.POST.get("book_issue_id")
    fk_purchase_id = request.POST.get("fk_purchase_id")
    return_date = datetime.datetime.strptime(str(request.POST.get("return_date")), '%d-%m-%Y').strftime('%Y-%m-%d')

    if request.method == 'POST':
        book_issue_data_obj = BooksIssueData.objects.get(fk_user_info_id=student_name_id,
                                                         fk_book_purchase_id=fk_purchase_id,
                                                         book_issue_fk=book_issue_id)
        data_add_books = BooksReturned(fk_user_info_id=student_name_id, fk_books_issue_data_id=book_issue_data_obj.id,
                                       return_date=return_date)
        data_add_books.save()
        delete_books_obj = BooksIssue.objects.get(id=book_issue_id)
        delete_books_obj.delete()
        books_issue_obj = BooksIssue.objects.filter(fk_user_info_id=student_name_id)
        render_string = render_to_string("appendreturnadd.html", {"books_obj": books_issue_obj})
        return HttpResponse(render_string)


@csrf_exempt
def filter_books_return(request):
    """
    Filter book return table
    """
    author = request.POST.get("author")
    title = request.POST.get("title")
    isbn = request.POST.get("isbn")
    subject = request.POST.get("subject")
    fromdate = request.POST.get("fromdate")
    todate = request.POST.get("todate")

    if fromdate:
        fromdate = datetime.datetime.strptime(str(request.POST.get("fromdate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if todate:
        todate = datetime.datetime.strptime(str(request.POST.get("todate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if author and title and isbn and subject and fromdate and todate:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__author=author,
                                                 fk_books_issue_data__fk_book_purchase__title=title,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__subject=subject,
                                                 return_date__gte=fromdate, return_date__lte=todate)
    elif fromdate and isbn and title and author:
        books_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__title=title,
                                                 fk_books_issue_data__fk_book_purchase__author=author)
    elif todate and fromdate and isbn and author:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__author=author)
    elif todate and fromdate and isbn and title:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__title=title)
    elif todate and fromdate and isbn and subject:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__subject=subject)
    elif subject and title and author:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__subject=subject,
                                                 fk_books_issue_data__fk_book_purchase__title=title,
                                                 fk_books_issue_data__fk_book_purchase__author=author).order_by(
            'return_date')
    elif isbn and title and author:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__title=title,
                                                 fk_books_issue_data__fk_book_purchase__author=author)
    elif fromdate and isbn and author:
        books_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__author=author)
    elif fromdate and isbn and title:
        books_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__title=title).order_by(
            'return_date')
    elif fromdate and isbn and subject:
        books_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
            'return_date')
    elif todate and title and author:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                 fk_books_issue_data__fk_book_purchase__title=title,
                                                 fk_books_issue_data__fk_book_purchase__author=author).order_by(
            'return_date')
    elif todate and title and subject:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                 fk_books_issue_data__fk_book_purchase__title=title,
                                                 fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
            'return_date')
    elif todate and isbn and author:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__author=author).order_by(
            'return_date')
    elif todate and isbn and title:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__title=title).order_by(
            'return_date')
    elif todate and isbn and subject:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
            'return_date')
    elif todate and fromdate and author:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__author=author).order_by(
            'return_date')
    elif todate and fromdate and subject:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
            'return_date')
    elif todate and fromdate and title:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__title=title).order_by(
            'return_date')
    elif todate and fromdate and isbn:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn).order_by(
            'return_date')
    elif author and subject:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__author=author,
                                                 fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
            'return_date')
    elif title and author:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__title=title,
                                                 fk_books_issue_data__fk_book_purchase__author=author).order_by(
            'return_date')
    elif title and subject:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__title=title,
                                                 fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
            'return_date')
    elif isbn and author:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__author=author).order_by(
            'return_date')
    elif isbn and title:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__title=title).order_by(
            'return_date')
    elif isbn and subject:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                 fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
            'return_date')
    elif fromdate and author:
        books_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__author=author).order_by(
            'return_date')
    elif fromdate and subject:
        books_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
            'return_date')
    elif fromdate and title:
        books_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__title=title).order_by(
            'return_date')
    elif fromdate and isbn:
        books_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn).order_by(
            'return_date')
    elif todate and author:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                 fk_books_issue_data__fk_book_purchase__author=author).order_by(
            'return_date')
    elif todate and subject:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                 fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
            'return_date')
    elif todate and title:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                 fk_books_issue_data__fk_book_purchase__title=title).order_by(
            'return_date')
    elif todate and isbn:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                 fk_books_issue_data__fk_book_purchase__isbn=isbn).order_by(
            'return_date')
    elif todate and fromdate:
        books_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate).order_by(
            'return_date')
    elif author:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__author=author).order_by(
            'return_date')
    elif title:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__title=title).order_by(
            'return_date')
    elif subject:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
            'return_date')
    elif isbn:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__isbn=isbn).order_by(
            'return_date')
    elif fromdate:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__return_date__gte=fromdate).order_by('return_date')
    elif todate:
        books_obj = BooksReturned.objects.filter(fk_books_issue_data__return_date__lte=todate).order_by('return_date')
    else:
        books_obj = BooksReturned.objects.all()

    render_string = render_to_string("returnedbookfilter.html", {"books_data_obj": books_obj})
    return HttpResponse(render_string)


@csrf_exempt
def filter_modal_books_return(request):
    """
    Filter book issue modal table
    """
    author = request.POST.get("author")
    title = request.POST.get("title")
    subject = request.POST.get("subject")
    isbn = request.POST.get("isbn")
    fromdate = request.POST.get("fromdate")
    todate = request.POST.get("todate")

    if fromdate:
        fromdate = datetime.datetime.strptime(str(request.POST.get("fromdate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if todate:
        todate = datetime.datetime.strptime(str(request.POST.get("todate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if author and title and isbn and subject and fromdate and todate:
        books_obj = BooksIssue.objects.filter(fk_book_purchase__author=author, fk_book_purchase__title=title,
                                              fk_book_purchase__isbn=isbn, fk_book_purchase__subject=subject,
                                              issue_date__gte=fromdate, issue_date__lte=todate)
    elif fromdate and isbn and title and author:
        books_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                              fk_book_purchase__title=title, fk_book_purchase__author=author)
    elif todate and fromdate and isbn and author:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                              fk_book_purchase__isbn=isbn,
                                              fk_book_purchase__author=author)
    elif todate and fromdate and isbn and title:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                              fk_book_purchase__isbn=isbn,
                                              fk_book_purchase__title=title)
    elif todate and fromdate and isbn and subject:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                              fk_book_purchase__isbn=isbn,
                                              fk_book_purchase__subject=subject)
    elif subject and title and author:
        books_obj = BooksIssue.objects.filter(fk_book_purchase__subject=subject, fk_book_purchase__title=title,
                                              fk_book_purchase__author=author).order_by('issue_date')
    elif isbn and title and author:
        books_obj = BooksIssue.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title,
                                              fk_book_purchase__author=author)
    elif fromdate and isbn and author:
        books_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                              fk_book_purchase__author=author)
    elif fromdate and isbn and title:
        books_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                              fk_book_purchase__title=title).order_by('issue_date')
    elif fromdate and isbn and subject:
        books_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                              fk_book_purchase__subject=subject).order_by('issue_date')
    elif todate and title and author:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title,
                                              fk_book_purchase__author=author).order_by('issue_date')
    elif todate and title and subject:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title,
                                              fk_book_purchase__subject=subject).order_by('issue_date')
    elif todate and isbn and author:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                              fk_book_purchase__author=author).order_by('issue_date')
    elif todate and isbn and title:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                              fk_book_purchase__title=title).order_by('issue_date')
    elif todate and isbn and subject:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                              fk_book_purchase__subject=subject).order_by('issue_date')
    elif todate and fromdate and author:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                              fk_book_purchase__author=author).order_by('issue_date')
    elif todate and fromdate and subject:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                              fk_book_purchase__subject=subject).order_by('issue_date')
    elif todate and fromdate and title:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                              fk_book_purchase__title=title).order_by('issue_date')
    elif todate and fromdate and isbn:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                              fk_book_purchase__isbn=isbn).order_by('issue_date')
    elif author and subject:
        books_obj = BooksIssue.objects.filter(fk_book_purchase__author=author,
                                              fk_book_purchase__subject=subject).order_by(
            'issue_date')
    elif title and author:
        books_obj = BooksIssue.objects.filter(fk_book_purchase__title=title, fk_book_purchase__author=author).order_by(
            'issue_date')
    elif title and subject:
        books_obj = BooksIssue.objects.filter(fk_book_purchase__title=title,
                                              fk_book_purchase__subject=subject).order_by(
            'issue_date')
    elif isbn and author:
        books_obj = BooksIssue.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__author=author).order_by(
            'issue_date')
    elif isbn and title:
        books_obj = BooksIssue.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title).order_by(
            'issue_date')
    elif isbn and subject:
        books_obj = BooksIssue.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__subject=subject).order_by(
            'issue_date')
    elif fromdate and author:
        books_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__author=author).order_by(
            'issue_date')
    elif fromdate and subject:
        books_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__subject=subject).order_by(
            'issue_date')
    elif fromdate and title:
        books_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__title=title).order_by(
            'issue_date')
    elif fromdate and isbn:
        books_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn).order_by(
            'issue_date')
    elif todate and author:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__author=author).order_by(
            'issue_date')
    elif todate and subject:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__subject=subject).order_by(
            'issue_date')
    elif todate and title:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title).order_by(
            'issue_date')
    elif todate and isbn:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn).order_by(
            'issue_date')
    elif todate and fromdate:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate).order_by('issue_date')
    elif author:
        books_obj = BooksIssue.objects.filter(fk_book_purchase__author=author).order_by('issue_date')
    elif title:
        books_obj = BooksIssue.objects.filter(fk_book_purchase__title=title).order_by('issue_date')
    elif subject:
        books_obj = BooksIssue.objects.filter(fk_book_purchase__subject=subject).order_by('issue_date')
    elif isbn:
        books_obj = BooksIssue.objects.filter(fk_book_purchase__isbn=isbn).order_by('issue_date')
    elif fromdate:
        books_obj = BooksIssue.objects.filter(issue_date__gte=fromdate).order_by('issue_date')
    elif todate:
        books_obj = BooksIssue.objects.filter(issue_date__lte=todate).order_by('issue_date')
    else:
        books_obj = BooksIssue.objects.all()

    render_string = render_to_string("returndialogbookfile.html", {"books_obj": books_obj})
    return HttpResponse(render_string)


def books_scrap(request):
    """
    Page for books scrap
    """
    session = request.session.get('user_id')
    user_info_obj = UserInfo.objects.get(id=session)
    user_operations_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
    books_purchase_obj = BooksPurchase.objects.all().order_by('published_date')
    books_subject_obj = Subject.objects.all()
    books_scrapped_obj = BooksScrapped.objects.all().order_by('scrap_date')
    return render(request, "booksscrap.html",
                  {"user_operations_obj": user_operations_obj, "user_info_obj": user_info_obj,
                   "books_scrapped_obj": books_scrapped_obj,
                   "books_subject_obj": books_subject_obj,
                   "books_purchase_obj": books_purchase_obj})


@csrf_exempt
def edit_books_scrap(request):
    """
    Append book purchase details in the field
    """
    list = []
    dict = {}
    id = request.POST.get("id")
    print(id)
    books_obj = BooksPurchase.objects.get(id=id)
    dict['id'] = books_obj.id
    dict['title'] = books_obj.title
    dict['author'] = books_obj.author
    dict['publisher'] = books_obj.publisher
    dict['subject'] = books_obj.subject.subjects
    dict['isbn'] = books_obj.isbn
    list.append(dict)
    return JsonResponse({"list": list})


@csrf_exempt
def add_scrap_books(request):
    """
    Adding BooksScrapped details to database
    """
    session = request.session.get('user_id')
    book_purchase_id = request.POST.get("book_purchase_id")
    scrap_copies = request.POST.get("scrap_copies")
    reason_for_scrap = request.POST.get("reason_for_scrap")
    scrap_date = datetime.datetime.strptime(str(request.POST.get("scrap_date")), '%d-%m-%Y').strftime('%Y-%m-%d')

    if request.method == 'POST':
        add_books = BooksScrapped(fk_user_info_id=session, fk_book_purchase_id=book_purchase_id, scrap_date=scrap_date,
                                  reason_for_scrap=reason_for_scrap, scrap_copies=scrap_copies)
        add_books.save()
    return HttpResponse("success")


@csrf_exempt
def books_scrap_filter_change_title(request):
    """
    Filtering title by on clicking author
    """
    author = request.POST.get("author")
    if author:
        title_list = list(BooksPurchase.objects.filter(author=author).values_list('id', 'title'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def books_scrap_filter_change_title_author(request):
    """
    Filtering author and title by on clicking subject
    """
    subject = request.POST.get("subject")
    if subject:
        title_list = list(BooksPurchase.objects.filter(subject_id=subject).values_list('id', 'title', 'author'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def filter_books_scrap(request):
    """
    Filter for books scrap
    """
    author = request.POST.get("author")
    title = request.POST.get("title")
    subject = request.POST.get("subject")
    isbn = request.POST.get("isbn")
    fromdate = request.POST.get("fromdate")
    todate = request.POST.get("todate")

    if fromdate:
        fromdate = datetime.datetime.strptime(str(request.POST.get("fromdate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if todate:
        todate = datetime.datetime.strptime(str(request.POST.get("todate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if author and title and isbn and subject and fromdate and todate:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__author=author, fk_book_purchase__title=title,
                                                 fk_book_purchase__isbn=isbn, fk_book_purchase__subject_id=subject,
                                                 scrap_date__gte=fromdate, scrap_date__lte=todate)
    elif fromdate and isbn and title and author:
        books_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__title=title, fk_book_purchase__author=author)
    elif todate and fromdate and isbn and author:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                 fk_book_purchase__isbn=isbn, fk_book_purchase__author=author)
    elif todate and fromdate and isbn and title:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                 fk_book_purchase__isbn=isbn, fk_book_purchase__title=title)
    elif todate and fromdate and isbn and subject:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                 fk_book_purchase__isbn=isbn, fk_book_purchase__subject_id=subject)
    elif subject and author and title:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__subject_id=subject, fk_book_purchase__author=author,
                                                 fk_book_purchase__title=title)
    elif isbn and title and author:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title,
                                                 fk_book_purchase__author=author)
    elif fromdate and isbn and author:
        books_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__author=author)
    elif fromdate and isbn and title:
        books_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__title=title)
    elif fromdate and isbn and subject:
        books_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__subject_id=subject)
    elif todate and title and author:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__title=title,
                                                 fk_book_purchase__author=author)
    elif todate and title and subject:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__title=title,
                                                 fk_book_purchase__subject_id=subject)
    elif todate and isbn and author:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__author=author)
    elif todate and isbn and title:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__title=title)
    elif todate and isbn and subject:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__subject_id=subject)
    elif todate and fromdate and author:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                 fk_book_purchase__author=author)
    elif todate and fromdate and subject:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                 fk_book_purchase__subject_id=subject)
    elif todate and fromdate and title:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                 fk_book_purchase__title=title)
    elif todate and fromdate and isbn:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                 fk_book_purchase__isbn=isbn)
    elif author and subject:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__author=author, fk_book_purchase__subject_id=subject)
    elif subject and title:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__subject_id=subject, fk_book_purchase__title=title)
    elif author and title:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__author=author, fk_book_purchase__title=title)
    elif subject and title:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__subject_id=subject, fk_book_purchase__title=title)
    elif title and author:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__title=title, fk_book_purchase__author=author)
    elif title and subject:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__title=title, fk_book_purchase__subject_id=subject)
    elif isbn and author:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__author=author)
    elif isbn and title:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title)
    elif isbn and subject:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__subject_id=subject)
    elif fromdate and author:
        books_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__author=author)
    elif fromdate and subject:
        books_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__subject_id=subject)
    elif fromdate and title:
        books_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__title=title)
    elif fromdate and isbn:
        books_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__isbn=isbn)
    elif todate and author:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__author=author)
    elif todate and subject:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__subject_id=subject)
    elif todate and title:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__title=title)
    elif todate and isbn:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__isbn=isbn)
    elif todate and fromdate:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate)
    elif author:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__author=author)
    elif title:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__title=title)
    elif subject:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__subject_id=subject)
    elif isbn:
        books_obj = BooksScrapped.objects.filter(fk_book_purchase__isbn=isbn)
    elif fromdate:
        books_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate)
    elif todate:
        books_obj = BooksScrapped.objects.filter(scrap_date__lte=todate)
    else:
        books_obj = BooksScrapped.objects.all()

    render_string = render_to_string("scrappedbookfile.html", {"Books_Scrapped_obj": books_obj})
    return HttpResponse(render_string)


@csrf_exempt
def filter_modal_books_scrap(request):
    """
    Filter for books purchase in modal of book scrap
    """
    author = request.POST.get("author")
    title = request.POST.get("title")
    subject = request.POST.get("subject")
    isbn = request.POST.get("isbn")
    fromdate = request.POST.get("fromdate")
    todate = request.POST.get("todate")

    if fromdate:
        fromdate = datetime.datetime.strptime(str(request.POST.get("fromdate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if todate:
        todate = datetime.datetime.strptime(str(request.POST.get("todate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if author and title and isbn and subject and fromdate and todate:
        books_obj = BooksPurchase.objects.filter(author=author, title=title, isbn=isbn, subject_id=subject,
                                                 published_date__gte=fromdate, published_date__lte=todate)
    elif fromdate and isbn and title and author:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, title=title, author=author)
    elif todate and fromdate and isbn and author:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn,
                                                 author=author)
    elif todate and fromdate and isbn and title:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn,
                                                 title=title)
    elif todate and fromdate and isbn and subject:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn,
                                                 subject_id=subject)
    elif isbn and title and author:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, title=title, author=author)
    elif fromdate and isbn and author:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, author=author)
    elif fromdate and isbn and title:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, title=title)
    elif fromdate and isbn and subject:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, subject_id=subject)
    elif todate and title and author:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, title=title, author=author)
    elif todate and title and subject:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, title=title, subject_id=subject)
    elif todate and isbn and author:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn, author=author)
    elif todate and isbn and title:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn, title=title)
    elif todate and isbn and subject:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn, subject_id=subject)
    elif todate and fromdate and author:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate,
                                                 author=author)
    elif todate and fromdate and subject:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate,
                                                 subject_id=subject)
    elif todate and fromdate and title:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, title=title)
    elif todate and fromdate and isbn:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn)
    elif author and subject:
        books_obj = BooksPurchase.objects.filter(author=author, subject_id=subject)
    elif subject and title:
        books_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
    elif author and title:
        books_obj = BooksPurchase.objects.filter(author=author, title=title)
    elif subject and title:
        books_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
    elif title and author:
        books_obj = BooksPurchase.objects.filter(title=title, author=author)
    elif title and subject:
        books_obj = BooksPurchase.objects.filter(title=title, subject_id=subject)
    elif isbn and author:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, author=author)
    elif isbn and title:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, title=title)
    elif isbn and subject:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, subject_id=subject)
    elif fromdate and author:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, author=author)
    elif fromdate and subject:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, subject_id=subject)
    elif fromdate and title:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, title=title)
    elif fromdate and isbn:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn)
    elif todate and author:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, author=author)
    elif todate and subject:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, subject_id=subject)
    elif todate and title:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, title=title)
    elif todate and isbn:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn)
    elif todate and fromdate:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate)
    elif author:
        books_obj = BooksPurchase.objects.filter(author=author)
    elif title:
        books_obj = BooksPurchase.objects.filter(title=title)
    elif subject:
        books_obj = BooksPurchase.objects.filter(subject_id=subject)
    elif isbn:
        books_obj = BooksPurchase.objects.filter(isbn=isbn)
    elif fromdate:
        books_obj = BooksPurchase.objects.filter(published_date__gte=fromdate)
    elif todate:
        books_obj = BooksPurchase.objects.filter(published_date__lte=todate)
    else:
        books_obj = BooksPurchase.objects.all()

    render_string = render_to_string("scrappeddialogbookfile.html", {"bookss_obj": books_obj})
    return HttpResponse(render_string)


@csrf_exempt
def books_scrap_modal_filter_change_title(request):
    """
    Filtering title by on clicking author
    """
    author = request.POST.get("author")
    if author:
        title_list = list(BooksPurchase.objects.filter(author=author).values_list('id', 'title'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


@csrf_exempt
def books_scrap_modal_filter_change_title_author(request):
    """
    Filtering author and title by on clicking subject
    """
    subject = request.POST.get("subject")
    if subject:
        title_list = list(BooksPurchase.objects.filter(subject_id=subject).values_list('id', 'title', 'author'))
    else:
        pass
    return HttpResponse(json.dumps(title_list))


def available_books_report(request):
    """
    Page for report of available books in the library
    """
    session = request.session.get('user_id')
    user_info_obj = UserInfo.objects.get(id=session)
    user_operations_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
    books_purchase_obj = BooksPurchase.objects.all().order_by('purchase_date')
    books_subject_obj = Subject.objects.all()
    return render(request, "availablebooksreport.html",
                  {"user_operations_obj": user_operations_obj, "user_info_obj": user_info_obj,
                   "books_subject_obj": books_subject_obj,
                   "books_purchase_obj": books_purchase_obj})


def issued_books_report(request):
    """
    Page for report of issued books in the library
    """
    session = request.session.get('user_id')
    user_info_obj = UserInfo.objects.get(id=session)
    user_operations_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
    books_obj = BooksPurchase.objects.all()
    books_data_obj = BooksIssueData.objects.all().order_by('issue_date')
    books_subject_obj = Subject.objects.all()
    return render(request, "issuedbooksreport.html",
                  {"user_operations_obj": user_operations_obj, "books_data_obj": books_data_obj,
                   "books_subject_obj": books_subject_obj,
                   "user_info_obj": user_info_obj, "books_obj": books_obj})


def returned_books_report(request):
    """
    Page for report of returned books in the library
    """
    session = request.session.get('user_id')
    user_info_obj = UserInfo.objects.get(id=session)
    user_operations_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
    books_obj = BooksPurchase.objects.all()
    books_subject_obj = Subject.objects.all()
    books_returned_obj = BooksReturned.objects.all().order_by('return_date')
    return render(request, "returnedbooksreport.html",
                  {"user_operations_obj": user_operations_obj, "books_returned_obj": books_returned_obj,
                   "books_subject_obj": books_subject_obj,
                   "user_info_obj": user_info_obj, "books_obj": books_obj})


def scrapped_books_report(request):
    """
    Page for report of scrapped books in the library
    """
    session = request.session.get('user_id')
    user_info_obj = UserInfo.objects.get(id=session)
    user_operations_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
    books_purchase_obj = BooksPurchase.objects.all().order_by('published_date')
    books_subject_obj = Subject.objects.all()
    books_scrapped_obj = BooksScrapped.objects.all().order_by('scrap_date')
    return render(request, "scrappedbooksreport.html",
                  {"user_operations_obj": user_operations_obj, "user_info_obj": user_info_obj,
                   "books_scrapped_obj": books_scrapped_obj,
                   "books_subject_obj": books_subject_obj, "books_purchase_obj": books_purchase_obj})


@csrf_exempt
def filter_available_books_report(request):
    """
    Filter for available book report
    """
    author = request.POST.get("author")
    title = request.POST.get("title")
    subject = request.POST.get("subject")
    isbn = request.POST.get("isbn")
    fromdate = request.POST.get("fromdate")
    todate = request.POST.get("todate")

    if fromdate:
        fromdate = datetime.datetime.strptime(str(request.POST.get("fromdate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if todate:
        todate = datetime.datetime.strptime(str(request.POST.get("todate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if author and title and isbn and subject and fromdate and todate:
        books_obj = BooksPurchase.objects.filter(author=author, title=title, isbn=isbn, subject_id=subject,
                                                 purchase_date__gte=fromdate, purchase_date__lte=todate)
    elif fromdate and isbn and title and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, title=title, author=author)
    elif todate and fromdate and isbn and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn,
                                                 author=author)
    elif todate and fromdate and isbn and title:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn,
                                                 title=title)
    elif todate and fromdate and isbn and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn,
                                                 subject_id=subject)
    elif subject and author and title:
        books_obj = BooksPurchase.objects.filter(subject_id=subject, author=author, title=title)
    elif isbn and title and author:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, title=title, author=author)
    elif fromdate and isbn and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, author=author)
    elif fromdate and isbn and title:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, title=title)
    elif fromdate and isbn and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, subject_id=subject)
    elif todate and title and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, title=title, author=author)
    elif todate and title and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, title=title, subject_id=subject)
    elif todate and isbn and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn, author=author)
    elif todate and isbn and title:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn, title=title)
    elif todate and isbn and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn, subject_id=subject)
    elif todate and fromdate and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, author=author)
    elif todate and fromdate and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate,
                                                 subject=subject)
    elif todate and fromdate and title:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, title=title)
    elif todate and fromdate and isbn:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn)
    elif author and subject:
        books_obj = BooksPurchase.objects.filter(author=author, subject_id=subject)
    elif subject and title:
        books_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
    elif author and title:
        books_obj = BooksPurchase.objects.filter(author=author, title=title)
    elif subject and title:
        books_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
    elif title and author:
        books_obj = BooksPurchase.objects.filter(title=title, author=author)
    elif title and subject:
        books_obj = BooksPurchase.objects.filter(title=title, subject_id=subject)
    elif isbn and author:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, author=author)
    elif isbn and title:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, title=title)
    elif isbn and subject:
        books_obj = BooksPurchase.objects.filter(isbn=isbn, subject_id=subject)
    elif fromdate and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, author=author)
    elif fromdate and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, subject_id=subject)
    elif fromdate and title:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, title=title)
    elif fromdate and isbn:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn)
    elif todate and author:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, author=author)
    elif todate and subject:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, subject_id=subject)
    elif todate and title:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, title=title)
    elif todate and isbn:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn)
    elif todate and fromdate:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate)
    elif author:
        books_obj = BooksPurchase.objects.filter(author=author)
    elif title:
        books_obj = BooksPurchase.objects.filter(title=title)
    elif subject:
        books_obj = BooksPurchase.objects.filter(subject_id=subject)
    elif isbn:
        books_obj = BooksPurchase.objects.filter(isbn=isbn)
    elif fromdate:
        books_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate)
    elif todate:
        books_obj = BooksPurchase.objects.filter(purchase_date__lte=todate)
    else:
        books_obj = BooksPurchase.objects.all()

    render_string = render_to_string("availablebookreportrender.html", {"books_obj": books_obj})
    return HttpResponse(render_string)


@csrf_exempt
def filter_issued_books_report(request):
    """
    Filter for issued books report
    """
    author = request.POST.get("author")
    title = request.POST.get("title")
    isbn = request.POST.get("isbn")
    subject = request.POST.get("subject")
    fromdate = request.POST.get("fromdate")
    todate = request.POST.get("todate")

    if fromdate:
        fromdate = datetime.datetime.strptime(str(request.POST.get("fromdate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if todate:
        todate = datetime.datetime.strptime(str(request.POST.get("todate")), '%d-%m-%Y').strftime('%Y-%m-%d')
    if author and title and isbn and subject and fromdate and todate:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__author=author, fk_book_purchase__title=title,
                                                  fk_book_purchase__isbn=isbn, fk_book_purchase__subject=subject,
                                                  issue_date__gte=fromdate, issue_date__lte=todate)
    elif fromdate and isbn and title and author:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__title=title, fk_book_purchase__author=author)
    elif todate and fromdate and isbn and author:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__author=author)
    elif todate and fromdate and isbn and title:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__title=title)
    elif todate and fromdate and isbn and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__subject=subject)
    elif subject and title and author:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__subject=subject, fk_book_purchase__title=title,
                                                  fk_book_purchase__author=author).order_by('issue_date')
    elif isbn and title and author:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title,
                                                  fk_book_purchase__author=author)
    elif fromdate and isbn and author:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__author=author)
    elif fromdate and isbn and title:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__title=title).order_by('issue_date')
    elif fromdate and isbn and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__subject=subject).order_by('issue_date')
    elif todate and title and author:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title,
                                                  fk_book_purchase__author=author).order_by('issue_date')
    elif todate and title and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title,
                                                  fk_book_purchase__subject=subject).order_by('issue_date')
    elif todate and isbn and author:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__author=author).order_by('issue_date')
    elif todate and isbn and title:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__title=title).order_by('issue_date')
    elif todate and isbn and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__subject=subject).order_by('issue_date')
    elif todate and fromdate and author:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__author=author).order_by('issue_date')
    elif todate and fromdate and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__subject=subject).order_by('issue_date')
    elif todate and fromdate and title:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__title=title).order_by('issue_date')
    elif todate and fromdate and isbn:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                  fk_book_purchase__isbn=isbn).order_by('issue_date')
    elif author and subject:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__author=author,
                                                  fk_book_purchase__subject=subject).order_by('issue_date')
    elif title and author:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__title=title,
                                                  fk_book_purchase__author=author).order_by(
            'issue_date')
    elif title and subject:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__title=title,
                                                  fk_book_purchase__subject=subject).order_by('issue_date')
    elif isbn and author:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__author=author).order_by(
            'issue_date')
    elif isbn and title:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title).order_by(
            'issue_date')
    elif isbn and subject:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn,
                                                  fk_book_purchase__subject=subject).order_by(
            'issue_date')
    elif fromdate and author:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__author=author).order_by(
            'issue_date')
    elif fromdate and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__subject=subject).order_by(
            'issue_date')
    elif fromdate and title:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__title=title).order_by(
            'issue_date')
    elif fromdate and isbn:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn).order_by(
            'issue_date')
    elif todate and author:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__author=author).order_by(
            'issue_date')
    elif todate and subject:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__subject=subject).order_by(
            'issue_date')
    elif todate and title:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title).order_by(
            'issue_date')
    elif todate and isbn:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn).order_by(
            'issue_date')
    elif todate and fromdate:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate).order_by(
            'issue_date')
    elif author:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__author=author).order_by('issue_date')
    elif title:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__title=title).order_by('issue_date')
    elif subject:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__subject=subject).order_by('issue_date')
    elif isbn:
        books_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn).order_by('issue_date')
    elif fromdate:
        books_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate).order_by('issue_date')
    elif todate:
        books_obj = BooksIssueData.objects.filter(issue_date__lte=todate).order_by('issue_date')
    else:
        books_obj = BooksIssueData.objects.all()

    render_string = render_to_string("issuedbookreportrender.html", {"books_data_obj": books_obj})
    return HttpResponse(render_string)
