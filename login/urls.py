from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('edit_user/',views.edit_user,name='edit_user'),
    path('change_password/',views.password_change,name='change_password'),
    path('add_profile_pic/',views.add_profile_pic,name='add_profile_pic'),
    path('change_profile_pic/',views.change_profile_pic,name='change_profile_pic')
]
