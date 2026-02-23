from django.shortcuts import render, get_object_or_404
from .models import Book

def splash(request):
    return render(request, 'splash.html')


def book_list(request):
    books = Book.objects.all()

    query = request.GET.get('q')
    if query:
        books = books.filter(title__icontains=query)

    category = request.GET.get('category')
    if category:
        books = books.filter(category=category)

    return render(request, 'base.html', {'books': books})



def kirish(request):
    return render(request, "kirish.html")


def home(request):
    books = Book.objects.all()
    return render(request, "home.html", {'books': books})


def sahifam(request):
    return render(request, "sahifam.html")



def nav(request):
    return render(request, "nav.html")


def mutolaa(request):
    return render(request, "mutolaa.html")



def market(request):
    return render(request, "market.html")



def davra(request):
    return render(request, "davra.html")


def kitob_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'kitob.html', {'book': book})

def pdf_view(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'pdf.html', {'book': book})



