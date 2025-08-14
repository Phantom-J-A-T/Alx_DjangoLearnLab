from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    path('posts/', views.posts, name='posts'), 

    path('profile/', views.profile, name='profile'),
    
    # Blog post detail view
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    
    # User registration
    path('register/', views.register, name='register'),
    
    # User login
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    
    # User logout
    path('logout/', auth_views.LogoutView.as_view(template_name = 'blog/logout.html'), name='logout'),

     path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]