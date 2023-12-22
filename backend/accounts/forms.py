from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile

# Create your forms here 
class UserRegisterForm(UserCreationForm):
    class Meta():
        model = CustomUser
        fields = ['email', 'full_names', 'password1', 'password2', ]

class MechanicRegisterForm(UserCreationForm):
    class Meta():
        model = CustomUser
        fields = ['email', 'full_names', 'password1', 'password2', ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_no', 'about', 'location', ]
