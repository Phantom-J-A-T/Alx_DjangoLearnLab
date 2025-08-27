from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView    

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='user-feed'),
]


# path("follow/<int:pk>/", views.CustomUserViewSet.as_view({"post": "follow"}), name="follow-user"),
#   path("unfollow/<int:pk>/", views.CustomUserViewSet.as_view({"post": "unfollow"}), name="unfollow-user"),