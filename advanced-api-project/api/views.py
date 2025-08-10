from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.
 # Implememting Generic views for the Book model   
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

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
