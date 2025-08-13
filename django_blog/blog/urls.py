from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    
    # Blog post detail view
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    
    # User registration
    path('register/', views.register, name='register'),
    
    # User login
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    
    # User logout
    path('logout/', auth_views.LogoutView.as_view(template_name = 'blog/logout.html'), name='logout'),
]