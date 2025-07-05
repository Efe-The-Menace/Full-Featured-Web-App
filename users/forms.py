from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class profile_form(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['Bio', 'location', 'image', 'X', 'linkedin', 'github']
        
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        exclude = ['user']
    

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']