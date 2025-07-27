from django import forms
from ..relationship_app.models import UserProfile
from .models import Book

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'description']

        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'published_date': 'Date Published',
            'isbn': 'ISBN Number',
            'description': 'Book Description',
        }

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(widget=forms.Textarea, label="Message")