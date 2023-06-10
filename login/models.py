from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_all_profile')
    profile_pic = models.ImageField(
        upload_to='profile_pic')

    def __str__(self):
        return self.user.username
