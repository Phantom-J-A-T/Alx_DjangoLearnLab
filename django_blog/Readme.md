Django Authentication System – Detailed Documentation
1. Overview
Django’s authentication system is built to handle:

User identification (username, password, etc.)

User verification (checking credentials)

Session management (tracking who is logged in)

Permissions & authorization (what a user can access)

Your project combines Django’s built-in login/logout with custom registration and profile management.

2. Core Components
A. Login
Purpose: Allow a user to authenticate using their credentials and start a session.

Implementation:
We use Django’s LoginView from django.contrib.auth.views.

Flow:

User visits /login.

Django shows accounts/login.html.

User submits credentials → Django authenticates using AUTHENTICATION_BACKENDS (default: database).

If valid → Django creates a session and sets a session cookie in the browser.

Redirect to LOGIN_REDIRECT_URL or next parameter.

Code Reference:

python
Copy
Edit
path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
B. Logout
Purpose: End a user’s session and clear authentication-related cookies.

Implementation:
Using Django’s LogoutView.

Flow:

User clicks logout link (/logout).

Django deletes session data from the database.

Redirects to LOGOUT_REDIRECT_URL or shows a template.

Code Reference:

python
Copy
Edit
path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
C. Registration
Purpose: Allow a new user to create an account.

Implementation:
Custom view using an extended UserCreationForm with an additional email field.

Flow:

User visits /register.

Django shows accounts/register.html with CustomUserCreationForm.

On submission → form validates (username unique, password strength, email format).

If valid → user is saved to the database.

Redirect to /login.

Code Reference:

python
Copy
Edit
path('register/', views.register, name='register'),
D. Profile Management
Purpose: Show user-specific data and allow editing of profile details.

Implementation:
Custom view protected with @login_required.

Flow:

User logs in and visits /profile.

Django checks if the user is authenticated (session check).

If not authenticated → redirect to /login?next=/profile.

If authenticated → render accounts/profile.html.

Code Reference:

python
Copy
Edit
path('profile/', views.profile, name='profile'),
3. Settings Impact
In settings.py:

python
Copy
Edit
LOGIN_REDIRECT_URL = 'profile'  # Where to go after login
LOGOUT_REDIRECT_URL = 'login'   # Where to go after logout
LOGIN_URL = 'login'             # Where to send unauthenticated users
4. How Users Interact with the System
Step	User Action	System Response
1	Visit /register	Registration form is shown
2	Submit valid data	User is created and redirected to /login
3	Visit /login	Login form is shown
4	Submit valid credentials	Session is started, redirected to /profile
5	Visit /profile while logged in	Profile details are displayed
6	Click “Logout”	Session is cleared, redirected to /login

5. Testing Instructions
A. Test Registration
Go to /register.

Fill in:

Username: testuser

Email: test@example.com

Password: TestPass123!

Submit form.

Expected:

Redirect to /login.

User appears in the Django admin (/admin/auth/user/).

B. Test Login
Go to /login.

Enter:

Username: testuser

Password: TestPass123!

Submit form.

Expected:

Redirect to /profile.

Browser stores a session cookie.

C. Test Profile Access
Go to /profile while logged in.

Expected: Profile page loads.

Logout.

Try /profile again.

Expected: Redirect to /login?next=/profile.

D. Test Logout
While logged in, visit /logout.

Expected:

Session is cleared.

Redirect or show “You have been logged out” message.

Try /profile.

Expected: Redirect to /login.

E. Security Checks
Try logging in with the wrong password → Should show “Invalid username or password.”

Try registering with an existing username → Should show error “A user with that username already exists.”

Try registering without an email → Should show error “This field is required.”