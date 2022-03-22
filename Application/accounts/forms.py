from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    #first_name = forms.TextInput()


    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2']

### It's for updating the user information like username
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

## While it's use for updating the user profile like address, bio, image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'address', 'image']

