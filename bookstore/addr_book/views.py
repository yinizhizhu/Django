#import datetime
from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse
from addr_book.models import Book, Author
import django
# Create your views here.

def version(request):
    return HttpResponse("<p>Django Version=" + str(django.VERSION))

def aboutme(requst):
    return render_to_response("AboutMe.html")

def contactme(requst):
    return render_to_response("ContactMe.html")

def total(_list):
    """to count the number of the list"""
    counter = 0
    for temp in _list:
        counter = counter + 1
    return counter

def deletebook(request):
    """delete the uniqe book"""
    Book.objects.filter(isbn=request.GET["isbn"]).delete()
    book_list = Book.objects.all()
    if total(book_list) > 0:
        c = Context({"books_list": book_list,})
        return render_to_response("lookthrough.html", c)
    return render_to_response("lookthrough.html")

def lookthrough(request):
    """to look through all the Info"""
    book_list = Book.objects.all()
    if total(book_list) > 0:
        c = Context({"books_list": book_list,})
        return render_to_response("lookthrough.html", c)
    return render_to_response("lookthrough.html")

def searchauthor(request):
    """search author with name"""
    if request.POST:
        book_list = Book.objects.all()
        c = Context({"books_list": book_list,})
        return render_to_response("searchauthor.html", c)
    return render_to_response("searchauthor.html")

def clickontitle(request):
    """get the Info while user clicks on the title of book"""
    book_list = Book.objects.filter(title=request.GET["title"])
    tempc = Context({"books_list": book_list,})
    return render_to_response("info_title.html", tempc)

def updateinfo(request):
    """update the Info of the book and the author"""
    book_list = Book.objects.filter(title=request.GET["title"])
    tempc = Context({"books_list": book_list,})
    if request.POST:
        post = request.POST
        for book in book_list:
            if book.author.authorid == post['authorid']:
                book.author.authorid = post["authorid"]
                book.author.name = post["name"]
                book.author.age = post["age"]
                book.author.country = post["country"]
                book.author.save()
            else:
                new_author = newauthor(post)
                new_author.save()
                book.author = new_author
            book.publisher = post["publisher"]
            book.publishdate = post["publishdate"]
            book.price = post["price"]
            book.save()

        c = Context({"books_list": book_list,})
        return render_to_response("info_title.html", c)
    return render_to_response("update.html", tempc)

def newbook(post):
    """to get the room for book to store"""
    new_book = Book(
        isbn = post["isbn"],
        title = post["title"],
        publisher = post["publisher"],
        publishdate = post["publishdate"],
        price = post["price"])
    return new_book

def newauthor(post):
    """"to get the room for book to store"""
    new_author = Author(
        authorid = post["authorid"],
        name = post["name"],
        age = post["age"],
        country = post["country"])
    return new_author

def addbook(request):
    """to add the book into the DB"""
    if request.POST:
        post = request.POST
        if total(Book.objects.filter(isbn=post["isbn"])) > 0:
            if total(Author.objects.filter(authorid=post["authorid"])) > 0:
                author = Author.objects.get(authorid=post["authorid"])
                author.name=post["name"]
                author.age=post["age"]
                author.country=post["country"]
                author.save()
            else:
                author = newauthor(post)
                author.save()
            book = Book.objects.get(isbn=post["isbn"])
            book.title=post["title"]
            book.author = author
            book.publisher=post["publisher"]
            book.publishdate=post["publishdate"]
            book.price=post["price"]
            book.save()
        else:
            if total(Author.objects.filter(authorid=post["authorid"])) > 0:
                author = Author.objects.get(authorid=post["authorid"])
                author.name=post["name"]
                author.age=post["age"]
                author.country=post["country"]
                author.save()
            else:
                author = newauthor(post)
                author.save()
            book = newbook(post)
            book.author = author
            book.save()
    return render_to_response("addbook.html")
