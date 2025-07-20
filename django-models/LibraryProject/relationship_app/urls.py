from django.urls import path
from .views import list_books, LibraryDetailView, RegisterView, LoginView, LogoutView

urlpatterns= [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', RegisterView, name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
]