from models import Author, Book, Library, Librarian

# Querying the database to retrieve all authors
author_name = input("Enter the name of the author you want to search for: ")
try:
    author = Author.objects.get(name=author_name)
    print(f"Author found: {author.name}")
    
    # Retrieve all books written by the author
    books = Book.objects.filter(author=author)
    if books.exists():
        print("Books written by this author:")
        for book in books:
            print(f"* {book.title} (Published on: {book.published_date})")
    else:
        print("No books found for this author.")
except Author.DoesNotExist:
    print(f"No author found with the name '{author_name}'.  Try another name, Thank you!")


# Querying the database to retrieve all libraries
library_name = input("Enter the name of the library you want to search for: ")
try:
    library = Library.objects.get(name=library_name)
    print(f"Library found: {library.name}, Location: {library.location}")
    
    # Retrieve all books available in the library
    books_in_library = library.books.all()
    if books_in_library.exists():

        print("Books available in this library:")
        for book in books_in_library:
            print(f"* {book.title} (Published on: {book.published_date})")
    else:
        print("No books found in this library.")
except Library.DoesNotExist:
    print(f"No library found with the name '{library_name}'. Try another name, Thank you!")

try:
    Librarian = Librarian.objects.get(Library= library_name)
    print(f"Librarian found: {Librarian.name} for the library {library.name}")
except Librarian.DoesNotExist:
    print(f"No librarian found in'{library_name}'. Try another name, Thank you!")