from django.urls import path
from .views import list_books, LibraryDetailView, register, LoginView, LogoutView, add_book, change_book, delete_book, admin_dashboard, librarian_Dashboard, member_dashboard
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns= [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name= 'relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html'), name='logout'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian_dashboard/', librarian_Dashboard, name='librarian_dashboard'),
    path('member_dashboard/', member_dashboard, name='member_dashboard'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:book_id>/edit/', change_book, name='change_book'),
    path('books/<int:book_id>/delete/', delete_book, name='delete_book'),
]