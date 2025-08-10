from .models import Author, Book
from rest_framework import serializers
from datetime import date

# Serializers for Author  with Fields for the name and email
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

# Serializers for Book with Fields for the title, author, and publication year
class BookSerializer(serializers.ModelSerializer):
    # Nested serializer for author to include author details in book serialization
    author = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year']
        read_only_fields = ['author']  # Make author read-only to prevent modification through this serializer
    # Validation for publication year to ensure it is not in the future
    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
