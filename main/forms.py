from django import forms
from main.models import User

class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))

    class Meta:
        model = User
        fields = ('email','password')