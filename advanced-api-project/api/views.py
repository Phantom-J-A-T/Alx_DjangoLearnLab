from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter
from django_filters.rest_framework import DjangoFilterBackend
#from django_filters import rest_framework


# Create your views here.
 # Implememting Generic views for the Book model   
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # allow unauthenticated users to read, but authenticated users to write
    filter_backends = [DjangoFilterBackend]  # Using DjangoFilterBackend to enable filtering
    filterset_class = [BookFilter]  # Adding filter backend to allow filtering of books
    search_fields = ['title', 'author__name']  # Enabling search functionality on title and author name
    ordering_fields = ['title, publication_year']  # Allowing ordering by publication year and title
    ordering = ['publication_year']  # Default ordering by publication year


class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # allow unauthenticated users to read, but authenticated users to write

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # restrict creation to authenticated users

    def perform_create(self, serializer):
        # Giving the authnticated user the ability to create a book and save it
        serializer.save()

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # restrict updates to authenticated users

    def perform_update(self, serializer):
        # Giving the authenticated user the ability to update a book and save it
        serializer.save()

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # restrict deletion to authenticated users

    def perform_destroy(self, instance):
        # Giving the authenticated user the ability to delete a book
        instance.delete()


#filters.OrderingFilter
#filters.SearchFilter