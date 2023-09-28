from django.db import models
from django.contrib.auth.models import User

class UserVerification(models.Model):
    username = models.CharField(max_length=255)
    unique_code = models.CharField(max_length=64)   # Assuming a maximum length of 64 characters for the hash

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/')