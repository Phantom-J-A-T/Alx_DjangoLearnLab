from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import  Book
from .models import Library

def list_books(request):
    books = Book.objects.all()
    response = "Books List"
    for book in books:
        response += f"* {book.title} by {book.author.name} - Published on {book.published_date}."
    return render(request, 'relationship_app/list_books.html', {'books': books, 'response': response})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context