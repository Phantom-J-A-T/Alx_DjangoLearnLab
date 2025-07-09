For Retrieving the Data Stored in the Book Model
I used the .get command followed by the parameters either ID, title, author name etc
 retrieved_book = Book.objects.get(title= "First Book")
>>> print(retrieved_book)
Output
Book object (1)
>>> print(retrieved_book.author)
Output
Phantom

>>> retrieve_book= Book.objects.get(title = "1984")
Output
>>> print (retrieve_book)
Book object (4)
