from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # Only one field needed
    following = models.ManyToManyField(
        'self',
        symmetrical=False,   # following ≠ followers
        related_name='followers',  
        blank=True
    )

    def __str__(self):
        return self.username
