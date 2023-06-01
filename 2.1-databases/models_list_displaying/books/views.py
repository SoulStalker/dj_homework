from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_objects = Book.objects.values()
    context = {'books': books_objects}
    return render(request, template, context)

