📚 Books API
A Django REST Framework-based API for managing books.
Provides read-only access to unauthenticated users and full CRUD access to authenticated users.

🚀 Features
📖 List & View Books — Public access.

✏️ Create, Update, Delete — Requires authentication.

✅ Validation — Ensures publication_year is not in the future.

🔒 Permissions — Custom access rules for different endpoints.

📡 API Endpoints
Method	Endpoint	Description	Permission
GET	/books/	Retrieve all books	Public
GET	/books/<id>/	Retrieve a single book by ID	Public
POST	/books/create/	Create a new book	Authenticated
PUT	/books/<id>/update/	Update an existing book	Authenticated
PATCH	/books/<id>/update/	Partially update a book	Authenticated
DELETE	/books/<id>/delete/	Delete a book	Authenticated

🛡️ Validation Rules
publication_year must not be greater than the current year.

Validation is enforced in both Create and Update endpoints.

🔑 Permissions
Public Access → List and detail views.

Authenticated Access → Create, update, and delete.

Powered by DRF’s built-in permission classes:

AllowAny

IsAuthenticated

IsAuthenticatedOrReadOnly