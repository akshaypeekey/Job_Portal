from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.userprofile.models import Profile


class SignupForm(UserCreationForm):
    class Meta:
        first_name = forms.CharField(max_length=20)
        last_name = forms.CharField(max_length=20)
        email = forms.EmailField(max_length=20, help_text='Enter a valid email address')

        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'user_type',
            'phone_number',
            'profile_image',
        ]