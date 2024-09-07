from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.

# views.py
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def books(request):
    # This view can be used for additional functionality if needed
    return render(request, 'bookshelf/books.html')


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request, pk):
    # Your view logic here
    return render(request, 'edit_template.html')

@permission_required('bookshelf.can_create', raise_exception=True)
def create_view(request):
    # Your view logic here
    return render(request, 'create_template.html')


from django.shortcuts import render
from .models import Book

def search_books(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# views.py

from django.shortcuts import render
from .forms import ExampleForm

def book_list(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ExampleForm()
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
