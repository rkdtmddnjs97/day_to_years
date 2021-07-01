from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nickname', 'location', 'phone_num', 'profile_img']
        
class CustomUserChangeForm(UserChangeForm) :
    class Meta :
        model = User
        fields = ['nickname', 'location', 'phone_num']

class ProfileChangeForm(UserChangeForm) :
    class Meta :
        model = User
        fields = ['comment', 'profile_img']
