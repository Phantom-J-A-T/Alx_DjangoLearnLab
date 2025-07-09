For Updating Details of the  Book Model
After selecting what I wanted to change and changing it I used the .save() to update it to the model

retrieved_book.title = "First Book Updated"
>>> retrieved_book.save()
No Output unless requested

retrieve_book.title = "Nineteen Eighty-Four"
>>> retrieve_book.save()
Output
>>> print (retrieve_book.title)
Nineteen Eighty-Four
