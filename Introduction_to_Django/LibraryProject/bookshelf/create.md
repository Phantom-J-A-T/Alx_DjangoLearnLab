For Importing the Modelinto the Shell
>>> from bookshelf.models import Book

Creating the Book Objects
>>> book = Book.objects.create(title = "First Book", author = "Phantom", published_date = 20250709)
>>> book = Book.objects.create(title = "Second Book", author = "Phantom", published_date = 20250709)
>>> book = Book.objects.create(title = "Third Book", author = "Phantom", published_date = 20250710)

Creating a Specified Book
>>> Book.objects.create(title = "1984", author = "George Orwell", published_date = 1949)
Output
<Book: Book object (4)>
