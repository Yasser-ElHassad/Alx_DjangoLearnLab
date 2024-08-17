from . import models


# Filtering books by author
books_by_author = models.Book.objects.filter(author='John Doe')

# Retrieving all books
all_books = models.Book.objects.all()

# Ordering books by published date
all_books = models.Librarian.objects.all()

