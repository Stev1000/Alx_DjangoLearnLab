from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Custom user creation form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Profile update form
class ProfileUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)
    bio = forms.CharField(max_length=500, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']
