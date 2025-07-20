from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import  Book
from .models import Library
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from .models import Book, Author

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('list_books')
        else:
            return render(request, 'relationship_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'relationship_app/login.html')

def LogoutView(request):
    logout(request)
    return redirect('login')



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


def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'admin'

@login_required
@user_passes_test(is_admin)

def admin_dashboard(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'librarian'

@login_required
@user_passes_test(is_librarian)

def librarian_Dashboard(request):
    return render(request, 'relationship_app/librarian_view.html')

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'member'

@login_required
@user_passes_test(is_member)

def member_dashboard(request):
    return render(request, 'relationship_app/member_view.html')


@permission_required('relationship_app.can_add_book', raise_exception=True)
@login_required
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author_name = request.POST['author']
        published_date = request.POST['published_date']
        
        author = Author.objects.get_or_create(name=author_name)
        Book.objects.create(title=title, author=author, published_date=published_date)
        
        return redirect('list_books')
    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})

@permission_required('relationship_app.can_view_book', raise_exception=True)
@login_required
def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'relationship_app/view_book.html', {'book': book})

@permission_required('relationship_app.can_change_book', raise_exception=True)
@login_required
def change_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        author_name = request.POST['author']
        book.author = Author.objects.get_or_create(name=author_name)[0]
        book.published_date = request.POST['published_date']
        book.save()
        return redirect('list_books')
    authors = Author.objects.all()
    return render(request, 'relationship_app/change_book.html', {'book': book, 'authors': authors})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
@login_required
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})