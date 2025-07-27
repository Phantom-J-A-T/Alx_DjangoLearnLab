from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
from .models import Book
from .forms import UserProfileForm
from .forms import BookForm
from .forms import ExampleForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    response = HttpResponse("Welcome to Library Project!")
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self'"
    return response

@permission_required('relationship_app.can_create_userprofile', raise_exception=True)
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm()
    return render(request, 'relationship_app/profile_form.html', {'form': form})

@permission_required('relationship_app.can_edit_userprofile', raise_exception=True)
def edit_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'relationship_app/profile_form.html', {'form': form})

@permission_required('relationship_app.can_delete_userprofile', raise_exception=True)
def delete_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'relationship_app/profile_confirm_delete.html', {'profile': profile})


@permission_required('relationship_app.can_view_userprofile', raise_exception=True)
def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'relationship_app/profile_list.html', {'profiles': profiles})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/form_example.html', {'form': form, 'title': 'Add Book'})

def example_view(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        # Do something with the form data
        pass
    return render(request, 'bookshelf/example_form.html', {'form': form})