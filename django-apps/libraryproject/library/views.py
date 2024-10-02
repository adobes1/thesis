from django.shortcuts import render, redirect
from library.models import Book
from library.forms import BookForm


def list_books_view(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'list_books.html', {'books': books})


def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
