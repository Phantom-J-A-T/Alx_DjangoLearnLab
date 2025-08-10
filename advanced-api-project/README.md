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

🧪 Testing Strategy
This project uses Django’s built-in test framework, which is based on Python’s unittest module, to ensure API reliability and maintainability.
All tests run against a separate test database to prevent any impact on production or development data.

Testing Approach
Unit Tests → Validate individual components (serializers, models, views).

Integration Tests → Verify that multiple components work together (e.g., API endpoints with DB interactions).

Permission & Access Tests → Ensure authenticated/unauthenticated users have the correct access (read-only for unauthenticated, full access for authenticated users).

Filter, Search, and Ordering Tests → Confirm filtering, search, and sorting functionality works as expected.

Example Test Cases
Book Creation

✅ Authenticated users can create books.

❌ Unauthenticated users cannot create books.

Book Retrieval

Any user (authenticated or not) can retrieve a single book or list of books.

Book Update

Only authenticated users with correct permissions can update books.

Filtering, Search & Ordering

Query parameters correctly filter books by author or publication year.

Search returns correct matches for title and author.

Ordering works for title and publication_year.

How to Run Tests
Run all tests:

bash
Copy
Edit
python manage.py test
Run tests for a specific app:

bash
Copy
Edit
python manage.py test api
Run a specific test case:

bash
Copy
Edit
python manage.py test api.tests.BookAPITestCase
Interpreting Test Results
✅ OK → All tests passed successfully.

❌ FAIL → At least one assertion failed; review the error message and traceback for details.

⚠️ ERROR → An exception occurred during the test; investigate the stack trace for the cause.