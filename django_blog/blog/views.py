from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Post

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


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/posts/'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)