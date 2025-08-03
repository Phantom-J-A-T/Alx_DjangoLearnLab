from django.shortcuts import render
from .models import Book
from rest_framework import generics
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated to access this viewset

    def perform_create(self, serializer):
        # Custom logic before saving a new book instance
        serializer.save()

class AdminViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for the Book model,
    accessible only to admin users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]  # Ensure the user is authenticated to access this viewset

    def perform_create(self, serializer):
        # Custom logic before saving a new book instance
        serializer.save()