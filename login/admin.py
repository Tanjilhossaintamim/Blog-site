from django.contrib import admin
from .models import UserProfile

# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    '''Admin View for UserProfile'''

    list_display = ['user', 'profile_pic']
    list_per_page = 10
