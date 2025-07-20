from django.urls import path
from .views import list_books, LibraryDetailView, register, LoginView, LogoutView
from django.contrib.auth.views import LoginView, LogoutView
from .admin_view import admin_dashboard
from .librarian_view import librarian_Dashboard 
from .member_view import member_dashboard
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
]