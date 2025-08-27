from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, get_user_model
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserProfileSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import CustomUserSerializer


User = get_user_model()

# Register View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserRegisterSerializer(user).data,
            "token": token.key,
            "message": "User registered successfully!"
        }, status=status.HTTP_201_CREATED)


# Login View
class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserProfileSerializer(user).data,
            "token": token.key,
            "message": "Login successful!"
        }, status=status.HTTP_200_OK)


# Profile View
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def follow(self, request, pk=None):
        """Allow the authenticated user to follow another user"""
        target_user = get_object_or_404(CustomUser, pk=pk)

        if target_user == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(target_user)
        return Response({"detail": f"You are now following {target_user.username}."}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def unfollow(self, request, pk=None):
        """Allow the authenticated user to unfollow another user"""
        target_user = get_object_or_404(CustomUser, pk=pk)

        if target_user == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(target_user)
        return Response({"detail": f"You have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"], permission_classes=[permissions.IsAuthenticated])
    def followers(self, request, pk=None):
        """Get list of a user's followers"""
        target_user = get_object_or_404(CustomUser, pk=pk)
        serializer = CustomUserSerializer(target_user.followers.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"], permission_classes=[permissions.IsAuthenticated])
    def following(self, request, pk=None):
        """Get list of users this person is following"""
        target_user = get_object_or_404(CustomUser, pk=pk)
        serializer = CustomUserSerializer(target_user.following.all(), many=True)
        return Response(serializer.data)