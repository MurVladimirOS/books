from django.shortcuts import render
from .models import AllBooks
from django.core.paginator import Paginator

# Create your views here.

def get_book(request):
    books = [book for book in AllBooks.objects.all()]


    context = {
        'count_books': len(books),
        'books': books,
    }
    return render(request, "app/page.html", context=context)
