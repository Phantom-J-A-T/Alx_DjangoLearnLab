All Commands used on Shell
from bookshelf.model imporrt Book
>>> Book.objects.create(title = "1984", author = "George Orwell", published_date = 1949)
<Book: Book object (4)>
>>>
KeyboardInterrupt
>>> retrieve_book= Book.objects.get(title = "1984")
>>> print (retrieve_book)
Book object (4)
>>>
KeyboardInterrupt
>>> retrieve_book.title = "Nineteen Eighty-Four"
>>> retrieve_book.save()
>>>
KeyboardInterrupt
>>> print (retrieve_book.title)
Nineteen Eighty-Four
>>>
KeyboardInterrupt
>>> retrieve_book.delete()
(1, {'bookshelf.Book': 1})
>>>
KeyboardInterrupt
>>>
KeyboardInterrupt
>>> print (retrieve_book.title)
Nineteen Eighty-Four
>>>
KeyboardInterrupt
>>> for book in Book.objects.all():
...     print(book.title)
...
Second Book
Third Book
>>> quit()
