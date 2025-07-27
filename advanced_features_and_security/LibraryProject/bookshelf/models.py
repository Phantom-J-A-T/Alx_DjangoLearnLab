from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.core.validators import FileExtensionValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.IntegerField()

class CustomUser(AbstractUser):
   date_of_birth = models.DateField(null=True, blank=True)
   profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True, 
                                     validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
   
   class Meta:
       permissions = [
            ("can_view_userprofile", "Can view user profile"),
            ("can_create_userprofile", "Can create user profile"),
            ("can_edit_userprofile", "Can edit user profile"),
            ("can_delete_userprofile", "Can delete user profile"),
       ]
   

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Use an email address to register. Make sure it is valid.')
        user = self.model(username=username, **extra_fields)
        email = self.normalize_email(email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be a staff.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)