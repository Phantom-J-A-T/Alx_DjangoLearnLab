from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here.
@login_required
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'blog/profile.html', {'user': request.user})
    else:
        return redirect('login')
    
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def home(request):
    return render(request, 'blog/base.html')

def post_detail(request, post_id):
    # Temporary dummy post data
    post = {
        'id': post_id,
        'title': f'Post {post_id}',
        'content': f'This is the detail page for post {post_id}.'
    }
    return render(request, 'blog/post_detail.html', {'post': post})

def posts(request):
    # Dummy data
    posts_list = [
        {'id': 1, 'title': 'First Post'},
        {'id': 2, 'title': 'Another Post'},
        {'id': 3, 'title': 'Last Post'},
    ]
    return render(request, 'blog/posts.html', {'posts': posts_list})