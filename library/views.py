from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
import pandas as pd
import traceback


def error_handler_500(request):
    return render(request, "500.html")


def error_save(error):
    time = str(datetime.datetime.now())
    with open("error_log.txt", "a") as myfile:
        myfile.write(time + "\n")
        myfile.write(error + "\n\n")
    print(error)
    return error


def book_purchase(request):
    """
    Page for book purchase

    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        book_purchase_obj = BooksPurchase.objects.all().order_by('purchase_date')
        book_subject_obj = Subject.objects.all()
        return render(request, "book_purchase.html",
                      {"user_info_obj": user_info_obj, "user_operation_obj": user_operation_obj,
                       "book_subject_obj": book_subject_obj,
                       "book_purchase_obj": book_purchase_obj})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_title(request):
    """
    Filtering title by on clicking author

    :param request:
    :return:
    """
    try:
        author = request.POST.get("author")
        if author:
            title_list = list(BooksPurchase.objects.filter(author=author).values_list('id', 'title'))
        else:
            pass
        return HttpResponse(json.dumps(title_list))
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_author_title(request):
    """
    Filtering author and title by on clicking subject

    :param request:
    :return:
    """
    try:
        subject = request.POST.get("subject")
        if subject:
            title_list = list(BooksPurchase.objects.filter(subject_id=subject).values_list('id', 'title', 'author'))
        else:
            pass
        return HttpResponse(json.dumps(title_list))
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def add_book_purchase(request):
    """
    Adding new books in the library

    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        title = request.POST.get("title")
        author = request.POST.get("author")
        publisher = request.POST.get("publisher")
        published_date = datetime.datetime.strptime(str(request.POST.get("published_date")), '%d-%m-%Y').strftime(
            '%Y-%m-%d')
        isbn = request.POST.get("isbn")
        price = request.POST.get("price")
        no_of_copies = request.POST.get("no_of_copies")
        purchase_date = datetime.datetime.strptime(str(request.POST.get("purchase_date")), '%d-%m-%Y').strftime(
            '%Y-%m-%d')
        subject = request.POST.get("subject")
        if request.method == 'POST':
            add_books = BooksPurchase(fk_user_info_id=session, title=title,
                                      author=author, publisher=publisher,
                                      published_date=published_date, isbn=isbn, price=price, no_of_copies=no_of_copies,
                                      purchase_date=purchase_date, subject_id=subject)
            add_books.save()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def delete_book_purchase(request):
    """
    Deleting any books from books purchase

    :param request:
    :return:
    """
    try:
        id = request.POST.get("id")
        book_obj = BooksPurchase.objects.get(id=id)
        book_obj.delete()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def edit_book_purchase(request):
    """
    Editing any details from books purchase

    :param request:
    :return:
    """
    try:
        list = []
        dict = {}
        id = request.POST.get("id")
        book_obj = BooksPurchase.objects.get(id=id)
        dict['id'] = book_obj.id
        dict['title'] = book_obj.title
        dict['author'] = book_obj.author
        dict['publisher'] = book_obj.publisher
        dict['published_date'] = datetime.datetime.strptime(str(book_obj.published_date), '%Y-%m-%d').strftime(
            '%d-%m-%Y')
        dict['isbn'] = book_obj.isbn
        dict['price'] = book_obj.price
        dict['subject'] = book_obj.subject_id
        dict['no_of_copies'] = book_obj.no_of_copies
        dict['purchase_date'] = datetime.datetime.strptime(str(book_obj.purchase_date), '%Y-%m-%d').strftime('%d-%m-%Y')
        list.append(dict)
        return JsonResponse({"list": list})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def update_book_purchase(request):
    """
    Update any details from books purchase

    :param request:
    :return:
    """
    try:
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
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_book_purchase(request):
    """
    Filter for books purchase

    :param request:
    :return:
    """
    try:
        author = request.POST.get("author")
        title = request.POST.get("title")
        subject = request.POST.get("subject")
        isbn = request.POST.get("isbn")
        fromdate = request.POST.get("from_date")
        todate = request.POST.get("to_date")
        if fromdate:
            fromdate = datetime.datetime.strptime(str(request.POST.get("from_date")), '%d-%m-%Y').strftime('%Y-%m-%d')
        if todate:
            todate = datetime.datetime.strptime(str(request.POST.get("to_date")), '%d-%m-%Y').strftime('%Y-%m-%d')
        if author and title and isbn and subject and fromdate and todate:
            book_obj = BooksPurchase.objects.filter(author=author, title=title, isbn=isbn, subject_id=subject,
                                                    purchase_date__gte=fromdate, purchase_date__lte=todate)
        elif fromdate and isbn and title and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, title=title, author=author)
        elif todate and fromdate and isbn and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn,
                                                    author=author)
        elif todate and fromdate and isbn and title:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn,
                                                    title=title)
        elif todate and fromdate and isbn and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn,
                                                    subject_id=subject)
        elif subject and author and title:
            book_obj = BooksPurchase.objects.filter(subject_id=subject, author=author, title=title)
        elif isbn and title and author:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, title=title, author=author)
        elif fromdate and isbn and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, author=author)
        elif fromdate and isbn and title:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, title=title)
        elif fromdate and isbn and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, subject_id=subject)
        elif todate and title and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, title=title, author=author)
        elif todate and title and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, title=title, subject_id=subject)
        elif todate and isbn and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn, author=author)
        elif todate and isbn and title:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn, title=title)
        elif todate and isbn and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn, subject_id=subject)
        elif todate and fromdate and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate,
                                                    author=author)
        elif todate and fromdate and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate,
                                                    subject=subject)
        elif todate and fromdate and title:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, title=title)
        elif todate and fromdate and isbn:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn)
        elif author and subject:
            book_obj = BooksPurchase.objects.filter(author=author, subject_id=subject)
        elif subject and title:
            book_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
        elif author and title:
            book_obj = BooksPurchase.objects.filter(author=author, title=title)
        elif subject and title:
            book_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
        elif title and author:
            book_obj = BooksPurchase.objects.filter(title=title, author=author)
        elif title and subject:
            book_obj = BooksPurchase.objects.filter(title=title, subject_id=subject)
        elif isbn and author:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, author=author)
        elif isbn and title:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, title=title)
        elif isbn and subject:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, subject_id=subject)
        elif fromdate and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, author=author)
        elif fromdate and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, subject_id=subject)
        elif fromdate and title:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, title=title)
        elif fromdate and isbn:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn)
        elif todate and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, author=author)
        elif todate and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, subject_id=subject)
        elif todate and title:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, title=title)
        elif todate and isbn:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn)
        elif todate and fromdate:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate)
        elif author:
            book_obj = BooksPurchase.objects.filter(author=author)
        elif title:
            book_obj = BooksPurchase.objects.filter(title=title)
        elif subject:
            book_obj = BooksPurchase.objects.filter(subject_id=subject)
        elif isbn:
            book_obj = BooksPurchase.objects.filter(isbn=isbn)
        elif fromdate:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate)
        elif todate:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate)
        else:
            book_obj = BooksPurchase.objects.all()
        render_string = render_to_string("render_filter_book_purchase.html", {"books_obj": book_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def book_issue(request):
    """
    Page for book issue

    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        books_purchase_obj = BooksPurchase.objects.all().order_by('published_date')
        books_issue_obj = BooksIssue.objects.all().order_by('issue_date')
        books_issue_data_obj = BooksIssueData.objects.all().order_by('issue_date')
        books_subject_obj = Subject.objects.all()
        course_obj = Course.objects.all()
        semester_obj = Semester.objects.all()
        section_obj = Section.objects.all()
        return render(request, "book_issue.html",
                      {"user_operation_obj": user_operation_obj, "books_data_obj": books_issue_data_obj,
                       "books_subject_obj": books_subject_obj,
                       "user_info_obj": user_info_obj, "books_issue_obj": books_issue_obj,
                       "books_purchase_obj": books_purchase_obj, "course_obj": course_obj,
                       "semesters_obj": semester_obj, "sections_obj": section_obj})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def delete_issue_book(request):
    """
    Delete issued books while issuing any new books to any student

    :param request:
    :return:
    """
    try:
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
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def issue_filter_student_name(request):
    """
    Filtering student name according to course

    :param request:
    :return:
    """

    try:
        course = request.POST.get("edit_course")
        semester = request.POST.get("edit_semester")
        section = request.POST.get("edit_section")
        if course:
            student_list = list(
                AcademicInfo.objects.filter(fk_course_id=course, fk_semesters_id=semester,
                                            fk_sections_id=section).values_list('fk_user_info',
                                                                                'fk_user_info__first_name',
                                                                                'fk_user_info__last_name'))
        else:
            pass
        return HttpResponse(json.dumps(student_list))
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def append_search_purchase_book_details(request):
    """
    Append book purchase details in the field

    :param request:
    :return:
    """
    try:
        list = []
        dict = {}
        id = request.POST.get("id")
        book_obj = BooksPurchase.objects.get(id=id)
        dict['id'] = book_obj.id
        dict['title'] = book_obj.title
        dict['author'] = book_obj.author
        dict['publisher'] = book_obj.publisher
        dict['subject'] = book_obj.subject.subjects
        dict['isbn'] = book_obj.isbn
        list.append(dict)
        return JsonResponse({"list": list})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def add_issue_book(request):
    """
    Adding issue books to database

    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        edit_title = request.POST.get("title")
        book_purchase_id = request.POST.get("book_purchase_id")
        course = request.POST.get("course")
        semester = request.POST.get("semester")
        section = request.POST.get("section")
        student_name = request.POST.get("student_name")
        date_of_issue = datetime.datetime.strptime(str(request.POST.get("date_of_issue")), '%d-%m-%Y').strftime(
            '%Y-%m-%d')
        due_date = pd.to_datetime(date_of_issue) + pd.Timedelta(days=15)
        book_obj = BooksIssue.objects.filter(fk_user_info_id=student_name)
        if request.method == 'POST':
            if book_obj.count() < 6:
                if not BooksIssue.objects.filter(fk_user_info_id=student_name,
                                                 fk_book_purchase__title=edit_title).exists():
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
                    books_no_copies = BooksPurchase.objects.get(title=edit_title).no_of_copies
                    actual_copies = books_no_copies - scrap_copies_no
                    issue_no_copies = BooksIssue.objects.filter(fk_book_purchase__title=edit_title).count()
                    remaining_copies = actual_copies - issue_no_copies
                    book_obj = BooksIssue.objects.filter(fk_user_info_id=student_name)
                    book_issue_copies_obj = BooksIssue.objects.filter(fk_user_info_id=student_name).count()
                    render_string = render_to_string("render_add_issue_book.html",
                                                     {"user_operations_obj": user_operation_obj,
                                                      "book_issue_copies_obj": book_issue_copies_obj,
                                                      "books_obj": book_obj,
                                                      "books_no_copies": actual_copies,
                                                      "issue_no_copies": issue_no_copies,
                                                      "remaining_copies": remaining_copies})
                    return HttpResponse(render_string)
                else:
                    return HttpResponse("same_books_not_exits")
            else:
                return HttpResponse("fail")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def show_particular_student_book(request):
    """
    Showing particular issued books of student in table while issuing books

    :param request:
    :return:
    """
    try:
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
        book_obj = BooksIssue.objects.filter(fk_user_info_id=student_name)
        book_issue_copies_obj = BooksIssue.objects.filter(fk_user_info_id=student_name).count()
        render_string = render_to_string("render_add_issue_book.html",
                                         {"book_issue_copies_obj": book_issue_copies_obj, "books_obj": book_obj,
                                          "books_no_copies": actual_copies, "issue_no_copies": issue_no_copies,
                                          "remaining_copies": remaining_copies})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def delete_issued_book(request):
    """
    Delete issued books (i.e BooksIssueData) from Table

    :param request:
    :return:
    """
    try:
        id = request.POST.get("id")
        book_obj = BooksIssueData.objects.get(id=id)
        book_obj.delete()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def library_copies_count(request):
    """
    For showing the counts of total copies,issued copies,remaining copies of particular book in the library

    :param request:
    :return:
    """
    try:
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
            {"books_no_copies": actual_copies, "issue_no_copies": issue_no_copies,
             "remaining_copies": remaining_copies})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_modal_book_issue(request):
    """
    Filter modal table of book issue

    :param request:
    :return:
    """
    try:
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
            book_obj = BooksPurchase.objects.filter(author=author, title=title, isbn=isbn, subject_id=subject,
                                                    published_date__gte=fromdate, published_date__lte=todate)
        elif fromdate and isbn and title and author:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, title=title, author=author)
        elif todate and fromdate and isbn and author:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn,
                                                    author=author)
        elif todate and fromdate and isbn and title:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn,
                                                    title=title)
        elif todate and fromdate and isbn and subject:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn,
                                                    subject_id=subject)
        elif subject and title and author:
            book_obj = BooksPurchase.objects.filter(subject_id=subject, title=title, author=author)
        elif isbn and title and author:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, title=title, author=author)
        elif fromdate and isbn and author:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, author=author)
        elif fromdate and isbn and title:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, title=title)
        elif fromdate and isbn and subject:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, subject_id=subject)
        elif todate and title and author:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, title=title, author=author)
        elif todate and title and subject:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, title=title, subject_id=subject)
        elif todate and isbn and author:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn, author=author)
        elif todate and isbn and title:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn, title=title)
        elif todate and isbn and subject:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn, subject_id=subject)
        elif todate and fromdate and author:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate,
                                                    author=author)
        elif todate and fromdate and subject:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate,
                                                    subject_id=subject)
        elif todate and fromdate and title:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate,
                                                    title=title)
        elif todate and fromdate and isbn:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn)
        elif author and subject:
            book_obj = BooksPurchase.objects.filter(author=author, subject_id=subject)
        elif subject and title:
            book_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
        elif author and title:
            book_obj = BooksPurchase.objects.filter(author=author, title=title)
        elif subject and title:
            book_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
        elif title and author:
            book_obj = BooksPurchase.objects.filter(title=title, author=author)
        elif title and subject:
            book_obj = BooksPurchase.objects.filter(title=title, subject_id=subject)
        elif isbn and author:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, author=author)
        elif isbn and title:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, title=title)
        elif isbn and subject:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, subject_id=subject)
        elif fromdate and author:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, author=author)
        elif fromdate and subject:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, subject_id=subject)
        elif fromdate and title:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, title=title)
        elif fromdate and isbn:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn)
        elif todate and author:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, author=author)
        elif todate and subject:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, subject_id=subject)
        elif todate and title:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, title=title)
        elif todate and isbn:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn)
        elif todate and fromdate:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate)
        elif author:
            book_obj = BooksPurchase.objects.filter(author=author)
        elif title:
            book_obj = BooksPurchase.objects.filter(title=title)
        elif subject:
            book_obj = BooksPurchase.objects.filter(subject_id=subject)
        elif isbn:
            book_obj = BooksPurchase.objects.filter(isbn=isbn)
        elif fromdate:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate)
        elif todate:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate)
        else:
            book_obj = BooksPurchase.objects.all()
        render_string = render_to_string("render_filter_modal_book_issue.html", {"bookss_obj": book_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_book_issue(request):
    """
    Filter book issue table

    :param request:
    :return:
    """
    try:
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
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__author=author, fk_book_purchase__title=title,
                                                     fk_book_purchase__isbn=isbn, fk_book_purchase__subject=subject,
                                                     issue_date__gte=fromdate, issue_date__lte=todate)
        elif fromdate and isbn and title and author:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__title=title, fk_book_purchase__author=author)
        elif todate and fromdate and isbn and author:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__author=author)
        elif todate and fromdate and isbn and title:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__title=title)
        elif todate and fromdate and isbn and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__subject=subject)
        elif subject and title and author:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__subject=subject, fk_book_purchase__title=title,
                                                     fk_book_purchase__author=author).order_by('issue_date')
        elif isbn and title and author:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title,
                                                     fk_book_purchase__author=author)
        elif fromdate and isbn and author:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__author=author)
        elif fromdate and isbn and title:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__title=title).order_by('issue_date')
        elif fromdate and isbn and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__subject=subject).order_by('issue_date')
        elif todate and title and author:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title,
                                                     fk_book_purchase__author=author).order_by('issue_date')
        elif todate and title and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title,
                                                     fk_book_purchase__subject=subject).order_by('issue_date')
        elif todate and isbn and author:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__author=author).order_by('issue_date')
        elif todate and isbn and title:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__title=title).order_by('issue_date')
        elif todate and isbn and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__subject=subject).order_by('issue_date')
        elif todate and fromdate and author:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__author=author).order_by('issue_date')
        elif todate and fromdate and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__subject=subject).order_by('issue_date')
        elif todate and fromdate and title:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__title=title).order_by('issue_date')
        elif todate and fromdate and isbn:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__isbn=isbn).order_by('issue_date')
        elif author and subject:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__author=author,
                                                     fk_book_purchase__subject=subject).order_by('issue_date')
        elif title and author:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__title=title,
                                                     fk_book_purchase__author=author).order_by(
                'issue_date')
        elif title and subject:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__title=title,
                                                     fk_book_purchase__subject=subject).order_by('issue_date')
        elif isbn and author:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__author=author).order_by(
                'issue_date')
        elif isbn and title:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__title=title).order_by(
                'issue_date')
        elif isbn and subject:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__subject=subject).order_by(
                'issue_date')
        elif fromdate and author:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate,
                                                     fk_book_purchase__author=author).order_by(
                'issue_date')
        elif fromdate and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate,
                                                     fk_book_purchase__subject=subject).order_by(
                'issue_date')
        elif fromdate and title:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__title=title).order_by(
                'issue_date')
        elif fromdate and isbn:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn).order_by(
                'issue_date')
        elif todate and author:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__author=author).order_by(
                'issue_date')
        elif todate and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate,
                                                     fk_book_purchase__subject=subject).order_by(
                'issue_date')
        elif todate and title:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title).order_by(
                'issue_date')
        elif todate and isbn:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn).order_by(
                'issue_date')
        elif todate and fromdate:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate).order_by(
                'issue_date')
        elif author:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__author=author).order_by('issue_date')
        elif title:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__title=title).order_by('issue_date')
        elif subject:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__subject=subject).order_by('issue_date')
        elif isbn:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn).order_by('issue_date')
        elif fromdate:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate).order_by('issue_date')
        elif todate:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate).order_by('issue_date')
        else:
            book_obj = BooksIssueData.objects.all()
        render_string = render_to_string("render_filter_book_issue.html", {"books_data_obj": book_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def book_return(request):
    """
    Page for book return

    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        books_purchase_obj = BooksPurchase.objects.all()
        books_issue_obj = BooksIssue.objects.all().order_by('issue_date')
        books_subject_obj = Subject.objects.all()
        course_obj = Course.objects.all()
        semesters_obj = Semester.objects.all()
        sections_obj = Section.objects.all()
        books_returned_obj = BooksReturned.objects.all().order_by('return_date')
        return render(request, "book_return.html",
                      {"user_operations_obj": user_operation_obj, "books_returned_obj": books_returned_obj,
                       "books_subject_obj": books_subject_obj,
                       "user_info_obj": user_info_obj, "books_issue_obj": books_issue_obj,
                       "books_purchase_obj": books_purchase_obj,
                       "course_obj": course_obj, "semesters_obj": semesters_obj, "sections_obj": sections_obj})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def append_search_book_issue_details(request):
    """
    Append book issue details in the field

    :param request:
    :return:
    """
    try:
        list = []
        dict = {}
        id = request.POST.get("id")
        book_obj = BooksIssue.objects.get(id=id)
        dict['id'] = book_obj.id
        dict['fk_purchase_id'] = book_obj.fk_book_purchase_id
        dict['title'] = book_obj.fk_book_purchase.title
        dict['author'] = book_obj.fk_book_purchase.author
        dict['publisher'] = book_obj.fk_book_purchase.publisher
        dict['subject'] = book_obj.fk_book_purchase.subject.subjects
        dict['isbn'] = book_obj.fk_book_purchase.isbn
        dict['course'] = book_obj.fk_course.course
        dict['semester'] = book_obj.fk_semester.semester
        dict['section'] = book_obj.fk_section.sections
        dict['issuedate'] = datetime.datetime.strptime(str(book_obj.issue_date), '%Y-%m-%d').strftime('%d-%m-%Y')
        dict['duedate'] = datetime.datetime.strptime(str(book_obj.due_date), '%Y-%m-%d').strftime('%d-%m-%Y')
        dict['studentname'] = book_obj.fk_user_info.first_name + ' ' + book_obj.fk_user_info.last_name
        dict['studentname_id'] = book_obj.fk_user_info_id
        list.append(dict)
        return JsonResponse({"list": list})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def add_return_book(request):
    """
    Adding return books to database

    :param request:
    :return:
    """
    try:
        student_name_id = request.POST.get("student_name_id")
        book_issue_id = request.POST.get("book_issue_id")
        fk_purchase_id = request.POST.get("fk_purchase_id")
        return_date = datetime.datetime.strptime(str(request.POST.get("return_date")), '%d-%m-%Y').strftime('%Y-%m-%d')

        if request.method == 'POST':
            book_issue_data_obj = BooksIssueData.objects.get(fk_user_info_id=student_name_id,
                                                             fk_book_purchase_id=fk_purchase_id,
                                                             book_issue_fk=book_issue_id)
            data_add_books = BooksReturned(fk_user_info_id=student_name_id,
                                           fk_books_issue_data_id=book_issue_data_obj.id,
                                           return_date=return_date)
            data_add_books.save()
            delete_book_obj = BooksIssue.objects.get(id=book_issue_id)
            delete_book_obj.delete()
            books_issue_obj = BooksIssue.objects.filter(fk_user_info_id=student_name_id)
            render_string = render_to_string("render_add_return_book.html", {"books_obj": books_issue_obj})
            return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_book_return(request):
    """
    Filter book return table

    :param request:
    :return:
    """
    try:
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
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__author=author,
                                                    fk_books_issue_data__fk_book_purchase__title=title,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__subject=subject,
                                                    return_date__gte=fromdate, return_date__lte=todate)
        elif fromdate and isbn and title and author:
            book_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__title=title,
                                                    fk_books_issue_data__fk_book_purchase__author=author)
        elif todate and fromdate and isbn and author:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__author=author)
        elif todate and fromdate and isbn and title:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__title=title)
        elif todate and fromdate and isbn and subject:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__subject=subject)
        elif subject and title and author:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__subject=subject,
                                                    fk_books_issue_data__fk_book_purchase__title=title,
                                                    fk_books_issue_data__fk_book_purchase__author=author).order_by(
                'return_date')
        elif isbn and title and author:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__title=title,
                                                    fk_books_issue_data__fk_book_purchase__author=author)
        elif fromdate and isbn and author:
            book_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__author=author)
        elif fromdate and isbn and title:
            book_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__title=title).order_by(
                'return_date')
        elif fromdate and isbn and subject:
            book_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
                'return_date')
        elif todate and title and author:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                    fk_books_issue_data__fk_book_purchase__title=title,
                                                    fk_books_issue_data__fk_book_purchase__author=author).order_by(
                'return_date')
        elif todate and title and subject:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                    fk_books_issue_data__fk_book_purchase__title=title,
                                                    fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
                'return_date')
        elif todate and isbn and author:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__author=author).order_by(
                'return_date')
        elif todate and isbn and title:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__title=title).order_by(
                'return_date')
        elif todate and isbn and subject:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
                'return_date')
        elif todate and fromdate and author:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__author=author).order_by(
                'return_date')
        elif todate and fromdate and subject:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
                'return_date')
        elif todate and fromdate and title:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__title=title).order_by(
                'return_date')
        elif todate and fromdate and isbn:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn).order_by(
                'return_date')
        elif author and subject:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__author=author,
                                                    fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
                'return_date')
        elif title and author:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__title=title,
                                                    fk_books_issue_data__fk_book_purchase__author=author).order_by(
                'return_date')
        elif title and subject:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__title=title,
                                                    fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
                'return_date')
        elif isbn and author:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__author=author).order_by(
                'return_date')
        elif isbn and title:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__title=title).order_by(
                'return_date')
        elif isbn and subject:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__isbn=isbn,
                                                    fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
                'return_date')
        elif fromdate and author:
            book_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__author=author).order_by(
                'return_date')
        elif fromdate and subject:
            book_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
                'return_date')
        elif fromdate and title:
            book_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__title=title).order_by(
                'return_date')
        elif fromdate and isbn:
            book_obj = BooksReturned.objects.filter(return_date__gte=fromdate,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn).order_by(
                'return_date')
        elif todate and author:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                    fk_books_issue_data__fk_book_purchase__author=author).order_by(
                'return_date')
        elif todate and subject:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                    fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
                'return_date')
        elif todate and title:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                    fk_books_issue_data__fk_book_purchase__title=title).order_by(
                'return_date')
        elif todate and isbn:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate,
                                                    fk_books_issue_data__fk_book_purchase__isbn=isbn).order_by(
                'return_date')
        elif todate and fromdate:
            book_obj = BooksReturned.objects.filter(return_date__lte=todate, return_date__gte=fromdate).order_by(
                'return_date')
        elif author:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__author=author).order_by(
                'return_date')
        elif title:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__title=title).order_by(
                'return_date')
        elif subject:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__subject=subject).order_by(
                'return_date')
        elif isbn:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__fk_book_purchase__isbn=isbn).order_by(
                'return_date')
        elif fromdate:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__return_date__gte=fromdate).order_by(
                'return_date')
        elif todate:
            book_obj = BooksReturned.objects.filter(fk_books_issue_data__return_date__lte=todate).order_by(
                'return_date')
        else:
            book_obj = BooksReturned.objects.all()
        render_string = render_to_string("render_filter_book_return.html", {"books_data_obj": book_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_modal_book_return(request):
    """
    Filter book issue modal table

    :param request:
    :return:
    """
    try:
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
            book_obj = BooksIssue.objects.filter(fk_book_purchase__author=author, fk_book_purchase__title=title,
                                                 fk_book_purchase__isbn=isbn, fk_book_purchase__subject=subject,
                                                 issue_date__gte=fromdate, issue_date__lte=todate)
        elif fromdate and isbn and title and author:
            book_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__title=title, fk_book_purchase__author=author)
        elif todate and fromdate and isbn and author:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                 fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__author=author)
        elif todate and fromdate and isbn and title:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                 fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__title=title)
        elif todate and fromdate and isbn and subject:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                 fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__subject=subject)
        elif subject and title and author:
            book_obj = BooksIssue.objects.filter(fk_book_purchase__subject=subject, fk_book_purchase__title=title,
                                                 fk_book_purchase__author=author).order_by('issue_date')
        elif isbn and title and author:
            book_obj = BooksIssue.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title,
                                                 fk_book_purchase__author=author)
        elif fromdate and isbn and author:
            book_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__author=author)
        elif fromdate and isbn and title:
            book_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__title=title).order_by('issue_date')
        elif fromdate and isbn and subject:
            book_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__subject=subject).order_by('issue_date')
        elif todate and title and author:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title,
                                                 fk_book_purchase__author=author).order_by('issue_date')
        elif todate and title and subject:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title,
                                                 fk_book_purchase__subject=subject).order_by('issue_date')
        elif todate and isbn and author:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__author=author).order_by('issue_date')
        elif todate and isbn and title:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__title=title).order_by('issue_date')
        elif todate and isbn and subject:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__subject=subject).order_by('issue_date')
        elif todate and fromdate and author:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                 fk_book_purchase__author=author).order_by('issue_date')
        elif todate and fromdate and subject:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                 fk_book_purchase__subject=subject).order_by('issue_date')
        elif todate and fromdate and title:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                 fk_book_purchase__title=title).order_by('issue_date')
        elif todate and fromdate and isbn:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                 fk_book_purchase__isbn=isbn).order_by('issue_date')
        elif author and subject:
            book_obj = BooksIssue.objects.filter(fk_book_purchase__author=author,
                                                 fk_book_purchase__subject=subject).order_by(
                'issue_date')
        elif title and author:
            book_obj = BooksIssue.objects.filter(fk_book_purchase__title=title,
                                                 fk_book_purchase__author=author).order_by(
                'issue_date')
        elif title and subject:
            book_obj = BooksIssue.objects.filter(fk_book_purchase__title=title,
                                                 fk_book_purchase__subject=subject).order_by(
                'issue_date')
        elif isbn and author:
            book_obj = BooksIssue.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__author=author).order_by(
                'issue_date')
        elif isbn and title:
            book_obj = BooksIssue.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title).order_by(
                'issue_date')
        elif isbn and subject:
            book_obj = BooksIssue.objects.filter(fk_book_purchase__isbn=isbn,
                                                 fk_book_purchase__subject=subject).order_by(
                'issue_date')
        elif fromdate and author:
            book_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__author=author).order_by(
                'issue_date')
        elif fromdate and subject:
            book_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__subject=subject).order_by(
                'issue_date')
        elif fromdate and title:
            book_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__title=title).order_by(
                'issue_date')
        elif fromdate and isbn:
            book_obj = BooksIssue.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn).order_by(
                'issue_date')
        elif todate and author:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__author=author).order_by(
                'issue_date')
        elif todate and subject:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__subject=subject).order_by(
                'issue_date')
        elif todate and title:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title).order_by(
                'issue_date')
        elif todate and isbn:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn).order_by(
                'issue_date')
        elif todate and fromdate:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate).order_by(
                'issue_date')
        elif author:
            book_obj = BooksIssue.objects.filter(fk_book_purchase__author=author).order_by('issue_date')
        elif title:
            book_obj = BooksIssue.objects.filter(fk_book_purchase__title=title).order_by('issue_date')
        elif subject:
            book_obj = BooksIssue.objects.filter(fk_book_purchase__subject=subject).order_by('issue_date')
        elif isbn:
            book_obj = BooksIssue.objects.filter(fk_book_purchase__isbn=isbn).order_by('issue_date')
        elif fromdate:
            book_obj = BooksIssue.objects.filter(issue_date__gte=fromdate).order_by('issue_date')
        elif todate:
            book_obj = BooksIssue.objects.filter(issue_date__lte=todate).order_by('issue_date')
        else:
            book_obj = BooksIssue.objects.all()
        render_string = render_to_string("render_filter_modal_book_return.html", {"books_obj": book_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def book_scrap(request):
    """
    Page for books scrap

    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        books_purchase_obj = BooksPurchase.objects.all().order_by('published_date')
        books_subject_obj = Subject.objects.all()
        books_scrapped_obj = BooksScrapped.objects.all().order_by('scrap_date')
        return render(request, "book_scrap.html",
                      {"user_operations_obj": user_operation_obj, "user_info_obj": user_info_obj,
                       "books_scrapped_obj": books_scrapped_obj,
                       "books_subject_obj": books_subject_obj,
                       "books_purchase_obj": books_purchase_obj})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def edit_book_scrap(request):
    """
    Append book purchase details in the field

    :param request:
    :return:
    """
    try:
        list = []
        dict = {}
        id = request.POST.get("id")
        book_obj = BooksPurchase.objects.get(id=id)
        dict['id'] = book_obj.id
        dict['title'] = book_obj.title
        dict['author'] = book_obj.author
        dict['publisher'] = book_obj.publisher
        dict['subject'] = book_obj.subject.subjects
        dict['isbn'] = book_obj.isbn
        list.append(dict)
        return JsonResponse({"list": list})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def add_scrap_book(request):
    """
    Adding BooksScrapped details to database

    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        book_purchase_id = request.POST.get("book_purchase_id")
        scrap_copies = request.POST.get("scrap_copies")
        reason_for_scrap = request.POST.get("reason_for_scrap")
        scrap_date = datetime.datetime.strptime(str(request.POST.get("scrap_date")), '%d-%m-%Y').strftime('%Y-%m-%d')
        if request.method == 'POST':
            add_books = BooksScrapped(fk_user_info_id=session, fk_book_purchase_id=book_purchase_id,
                                      scrap_date=scrap_date,
                                      reason_for_scrap=reason_for_scrap, scrap_copies=scrap_copies)
            add_books.save()
        return HttpResponse("success")
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_book_scrap(request):
    """
    Filter for books scrap

    :param request:
    :return:
    """
    try:
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
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__author=author, fk_book_purchase__title=title,
                                                    fk_book_purchase__isbn=isbn, fk_book_purchase__subject_id=subject,
                                                    scrap_date__gte=fromdate, scrap_date__lte=todate)
        elif fromdate and isbn and title and author:
            book_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                    fk_book_purchase__title=title, fk_book_purchase__author=author)
        elif todate and fromdate and isbn and author:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                    fk_book_purchase__isbn=isbn, fk_book_purchase__author=author)
        elif todate and fromdate and isbn and title:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                    fk_book_purchase__isbn=isbn, fk_book_purchase__title=title)
        elif todate and fromdate and isbn and subject:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                    fk_book_purchase__isbn=isbn, fk_book_purchase__subject_id=subject)
        elif subject and author and title:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__subject_id=subject,
                                                    fk_book_purchase__author=author,
                                                    fk_book_purchase__title=title)
        elif isbn and title and author:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title,
                                                    fk_book_purchase__author=author)
        elif fromdate and isbn and author:
            book_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                    fk_book_purchase__author=author)
        elif fromdate and isbn and title:
            book_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                    fk_book_purchase__title=title)
        elif fromdate and isbn and subject:
            book_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                    fk_book_purchase__subject_id=subject)
        elif todate and title and author:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__title=title,
                                                    fk_book_purchase__author=author)
        elif todate and title and subject:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__title=title,
                                                    fk_book_purchase__subject_id=subject)
        elif todate and isbn and author:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                    fk_book_purchase__author=author)
        elif todate and isbn and title:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                    fk_book_purchase__title=title)
        elif todate and isbn and subject:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                    fk_book_purchase__subject_id=subject)
        elif todate and fromdate and author:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                    fk_book_purchase__author=author)
        elif todate and fromdate and subject:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                    fk_book_purchase__subject_id=subject)
        elif todate and fromdate and title:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                    fk_book_purchase__title=title)
        elif todate and fromdate and isbn:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate,
                                                    fk_book_purchase__isbn=isbn)
        elif author and subject:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__author=author,
                                                    fk_book_purchase__subject_id=subject)
        elif subject and title:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__subject_id=subject, fk_book_purchase__title=title)
        elif author and title:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__author=author, fk_book_purchase__title=title)
        elif subject and title:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__subject_id=subject, fk_book_purchase__title=title)
        elif title and author:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__title=title, fk_book_purchase__author=author)
        elif title and subject:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__title=title, fk_book_purchase__subject_id=subject)
        elif isbn and author:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__author=author)
        elif isbn and title:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title)
        elif isbn and subject:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__subject_id=subject)
        elif fromdate and author:
            book_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__author=author)
        elif fromdate and subject:
            book_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__subject_id=subject)
        elif fromdate and title:
            book_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__title=title)
        elif fromdate and isbn:
            book_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate, fk_book_purchase__isbn=isbn)
        elif todate and author:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__author=author)
        elif todate and subject:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__subject_id=subject)
        elif todate and title:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__title=title)
        elif todate and isbn:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, fk_book_purchase__isbn=isbn)
        elif todate and fromdate:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate, scrap_date__gte=fromdate)
        elif author:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__author=author)
        elif title:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__title=title)
        elif subject:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__subject_id=subject)
        elif isbn:
            book_obj = BooksScrapped.objects.filter(fk_book_purchase__isbn=isbn)
        elif fromdate:
            book_obj = BooksScrapped.objects.filter(scrap_date__gte=fromdate)
        elif todate:
            book_obj = BooksScrapped.objects.filter(scrap_date__lte=todate)
        else:
            book_obj = BooksScrapped.objects.all()
        render_string = render_to_string("render_filter_book_scrap.html", {"Books_Scrapped_obj": book_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_modal_book_scrap(request):
    """
    Filter for books purchase in modal of book scrap

    :param request:
    :return:
    """
    try:
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
            book_obj = BooksPurchase.objects.filter(author=author, title=title, isbn=isbn, subject_id=subject,
                                                    published_date__gte=fromdate, published_date__lte=todate)
        elif fromdate and isbn and title and author:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, title=title, author=author)
        elif todate and fromdate and isbn and author:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn,
                                                    author=author)
        elif todate and fromdate and isbn and title:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn,
                                                    title=title)
        elif todate and fromdate and isbn and subject:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn,
                                                    subject_id=subject)
        elif isbn and title and author:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, title=title, author=author)
        elif fromdate and isbn and author:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, author=author)
        elif fromdate and isbn and title:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, title=title)
        elif fromdate and isbn and subject:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn, subject_id=subject)
        elif todate and title and author:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, title=title, author=author)
        elif todate and title and subject:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, title=title, subject_id=subject)
        elif todate and isbn and author:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn, author=author)
        elif todate and isbn and title:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn, title=title)
        elif todate and isbn and subject:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn, subject_id=subject)
        elif todate and fromdate and author:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate,
                                                    author=author)
        elif todate and fromdate and subject:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate,
                                                    subject_id=subject)
        elif todate and fromdate and title:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate,
                                                    title=title)
        elif todate and fromdate and isbn:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate, isbn=isbn)
        elif author and subject:
            book_obj = BooksPurchase.objects.filter(author=author, subject_id=subject)
        elif subject and title:
            book_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
        elif author and title:
            book_obj = BooksPurchase.objects.filter(author=author, title=title)
        elif subject and title:
            book_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
        elif title and author:
            book_obj = BooksPurchase.objects.filter(title=title, author=author)
        elif title and subject:
            book_obj = BooksPurchase.objects.filter(title=title, subject_id=subject)
        elif isbn and author:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, author=author)
        elif isbn and title:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, title=title)
        elif isbn and subject:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, subject_id=subject)
        elif fromdate and author:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, author=author)
        elif fromdate and subject:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, subject_id=subject)
        elif fromdate and title:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, title=title)
        elif fromdate and isbn:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate, isbn=isbn)
        elif todate and author:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, author=author)
        elif todate and subject:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, subject_id=subject)
        elif todate and title:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, title=title)
        elif todate and isbn:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, isbn=isbn)
        elif todate and fromdate:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate, published_date__gte=fromdate)
        elif author:
            book_obj = BooksPurchase.objects.filter(author=author)
        elif title:
            book_obj = BooksPurchase.objects.filter(title=title)
        elif subject:
            book_obj = BooksPurchase.objects.filter(subject_id=subject)
        elif isbn:
            book_obj = BooksPurchase.objects.filter(isbn=isbn)
        elif fromdate:
            book_obj = BooksPurchase.objects.filter(published_date__gte=fromdate)
        elif todate:
            book_obj = BooksPurchase.objects.filter(published_date__lte=todate)
        else:
            book_obj = BooksPurchase.objects.all()
        render_string = render_to_string("render_filter_modal_book_scrap.html", {"bookss_obj": book_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def available_book_report(request):
    """
    Page for report of available books in the library

    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        books_purchase_obj = BooksPurchase.objects.all().order_by('purchase_date')
        books_subject_obj = Subject.objects.all()
        return render(request, "available_book_report.html",
                      {"user_operations_obj": user_operation_obj, "user_info_obj": user_info_obj,
                       "books_subject_obj": books_subject_obj,
                       "books_purchase_obj": books_purchase_obj})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def issued_book_report(request):
    """
    Page for report of issued books in the library

    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        book_obj = BooksPurchase.objects.all()
        books_data_obj = BooksIssueData.objects.all().order_by('issue_date')
        books_subject_obj = Subject.objects.all()
        return render(request, "issued_book_report.html",
                      {"user_operations_obj": user_operation_obj, "books_data_obj": books_data_obj,
                       "books_subject_obj": books_subject_obj,
                       "user_info_obj": user_info_obj, "books_obj": book_obj})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def returned_book_report(request):
    """
    Page for report of returned books in the library

    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        book_obj = BooksPurchase.objects.all()
        books_subject_obj = Subject.objects.all()
        books_returned_obj = BooksReturned.objects.all().order_by('return_date')
        return render(request, "returned_book_report.html",
                      {"user_operations_obj": user_operation_obj, "books_returned_obj": books_returned_obj,
                       "books_subject_obj": books_subject_obj,
                       "user_info_obj": user_info_obj, "books_obj": book_obj})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


def scrapped_book_report(request):
    """
    Page for report of scrapped books in the library

    :param request:
    :return:
    """
    try:
        session = request.session.get('user_id')
        user_info_obj = UserInfo.objects.get(id=session)
        user_operation_obj = UserOperation.objects.filter(fk_user_role_id=user_info_obj.fk_user_role.id)
        books_purchase_obj = BooksPurchase.objects.all().order_by('published_date')
        books_subject_obj = Subject.objects.all()
        books_scrapped_obj = BooksScrapped.objects.all().order_by('scrap_date')
        return render(request, "scrapped_book_report.html",
                      {"user_operations_obj": user_operation_obj, "user_info_obj": user_info_obj,
                       "books_scrapped_obj": books_scrapped_obj,
                       "books_subject_obj": books_subject_obj, "books_purchase_obj": books_purchase_obj})
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_available_book_report(request):
    """
    Filter for available book report

    :param request:
    :return:
    """
    try:
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
            book_obj = BooksPurchase.objects.filter(author=author, title=title, isbn=isbn, subject_id=subject,
                                                    purchase_date__gte=fromdate, purchase_date__lte=todate)
        elif fromdate and isbn and title and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, title=title, author=author)
        elif todate and fromdate and isbn and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn,
                                                    author=author)
        elif todate and fromdate and isbn and title:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn,
                                                    title=title)
        elif todate and fromdate and isbn and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn,
                                                    subject_id=subject)
        elif subject and author and title:
            book_obj = BooksPurchase.objects.filter(subject_id=subject, author=author, title=title)
        elif isbn and title and author:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, title=title, author=author)
        elif fromdate and isbn and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, author=author)
        elif fromdate and isbn and title:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, title=title)
        elif fromdate and isbn and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn, subject_id=subject)
        elif todate and title and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, title=title, author=author)
        elif todate and title and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, title=title, subject_id=subject)
        elif todate and isbn and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn, author=author)
        elif todate and isbn and title:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn, title=title)
        elif todate and isbn and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn, subject_id=subject)
        elif todate and fromdate and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate,
                                                    author=author)
        elif todate and fromdate and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate,
                                                    subject=subject)
        elif todate and fromdate and title:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, title=title)
        elif todate and fromdate and isbn:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate, isbn=isbn)
        elif author and subject:
            book_obj = BooksPurchase.objects.filter(author=author, subject_id=subject)
        elif subject and title:
            book_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
        elif author and title:
            book_obj = BooksPurchase.objects.filter(author=author, title=title)
        elif subject and title:
            book_obj = BooksPurchase.objects.filter(subject_id=subject, title=title)
        elif title and author:
            book_obj = BooksPurchase.objects.filter(title=title, author=author)
        elif title and subject:
            book_obj = BooksPurchase.objects.filter(title=title, subject_id=subject)
        elif isbn and author:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, author=author)
        elif isbn and title:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, title=title)
        elif isbn and subject:
            book_obj = BooksPurchase.objects.filter(isbn=isbn, subject_id=subject)
        elif fromdate and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, author=author)
        elif fromdate and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, subject_id=subject)
        elif fromdate and title:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, title=title)
        elif fromdate and isbn:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate, isbn=isbn)
        elif todate and author:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, author=author)
        elif todate and subject:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, subject_id=subject)
        elif todate and title:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, title=title)
        elif todate and isbn:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, isbn=isbn)
        elif todate and fromdate:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate, purchase_date__gte=fromdate)
        elif author:
            book_obj = BooksPurchase.objects.filter(author=author)
        elif title:
            book_obj = BooksPurchase.objects.filter(title=title)
        elif subject:
            book_obj = BooksPurchase.objects.filter(subject_id=subject)
        elif isbn:
            book_obj = BooksPurchase.objects.filter(isbn=isbn)
        elif fromdate:
            book_obj = BooksPurchase.objects.filter(purchase_date__gte=fromdate)
        elif todate:
            book_obj = BooksPurchase.objects.filter(purchase_date__lte=todate)
        else:
            book_obj = BooksPurchase.objects.all()
        render_string = render_to_string("render_filter_available_book_report.html", {"books_obj": book_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')


@csrf_exempt
def filter_issued_book_report(request):
    """
    Filter for issued books report

    :param request:
    :return:
    """
    try:
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
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__author=author, fk_book_purchase__title=title,
                                                     fk_book_purchase__isbn=isbn, fk_book_purchase__subject=subject,
                                                     issue_date__gte=fromdate, issue_date__lte=todate)
        elif fromdate and isbn and title and author:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__title=title, fk_book_purchase__author=author)
        elif todate and fromdate and isbn and author:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__author=author)
        elif todate and fromdate and isbn and title:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__title=title)
        elif todate and fromdate and isbn and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__subject=subject)
        elif subject and title and author:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__subject=subject, fk_book_purchase__title=title,
                                                     fk_book_purchase__author=author).order_by('issue_date')
        elif isbn and title and author:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn, fk_book_purchase__title=title,
                                                     fk_book_purchase__author=author)
        elif fromdate and isbn and author:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__author=author)
        elif fromdate and isbn and title:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__title=title).order_by('issue_date')
        elif fromdate and isbn and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__subject=subject).order_by('issue_date')
        elif todate and title and author:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title,
                                                     fk_book_purchase__author=author).order_by('issue_date')
        elif todate and title and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title,
                                                     fk_book_purchase__subject=subject).order_by('issue_date')
        elif todate and isbn and author:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__author=author).order_by('issue_date')
        elif todate and isbn and title:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__title=title).order_by('issue_date')
        elif todate and isbn and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__subject=subject).order_by('issue_date')
        elif todate and fromdate and author:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__author=author).order_by('issue_date')
        elif todate and fromdate and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__subject=subject).order_by('issue_date')
        elif todate and fromdate and title:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__title=title).order_by('issue_date')
        elif todate and fromdate and isbn:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate,
                                                     fk_book_purchase__isbn=isbn).order_by('issue_date')
        elif author and subject:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__author=author,
                                                     fk_book_purchase__subject=subject).order_by('issue_date')
        elif title and author:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__title=title,
                                                     fk_book_purchase__author=author).order_by(
                'issue_date')
        elif title and subject:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__title=title,
                                                     fk_book_purchase__subject=subject).order_by('issue_date')
        elif isbn and author:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__author=author).order_by(
                'issue_date')
        elif isbn and title:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__title=title).order_by(
                'issue_date')
        elif isbn and subject:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn,
                                                     fk_book_purchase__subject=subject).order_by(
                'issue_date')
        elif fromdate and author:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate,
                                                     fk_book_purchase__author=author).order_by(
                'issue_date')
        elif fromdate and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate,
                                                     fk_book_purchase__subject=subject).order_by(
                'issue_date')
        elif fromdate and title:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__title=title).order_by(
                'issue_date')
        elif fromdate and isbn:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate, fk_book_purchase__isbn=isbn).order_by(
                'issue_date')
        elif todate and author:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__author=author).order_by(
                'issue_date')
        elif todate and subject:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate,
                                                     fk_book_purchase__subject=subject).order_by(
                'issue_date')
        elif todate and title:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__title=title).order_by(
                'issue_date')
        elif todate and isbn:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, fk_book_purchase__isbn=isbn).order_by(
                'issue_date')
        elif todate and fromdate:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate, issue_date__gte=fromdate).order_by(
                'issue_date')
        elif author:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__author=author).order_by('issue_date')
        elif title:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__title=title).order_by('issue_date')
        elif subject:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__subject=subject).order_by('issue_date')
        elif isbn:
            book_obj = BooksIssueData.objects.filter(fk_book_purchase__isbn=isbn).order_by('issue_date')
        elif fromdate:
            book_obj = BooksIssueData.objects.filter(issue_date__gte=fromdate).order_by('issue_date')
        elif todate:
            book_obj = BooksIssueData.objects.filter(issue_date__lte=todate).order_by('issue_date')
        else:
            book_obj = BooksIssueData.objects.all()
        render_string = render_to_string("render_filter_issued_book_report.html", {"books_data_obj": book_obj})
        return HttpResponse(render_string)
    except:
        error_save(str(traceback.format_exc()))
        return redirect('error_handler_500')
