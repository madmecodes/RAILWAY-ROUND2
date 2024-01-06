from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

FORM_CLASS = 'w-full py-3 px-6 rounded-xl text-slate-700'

class LoginForm(AuthenticationForm):
      username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-3 px-6 text-slate-700 rounded-xl'
    }))
      password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-3 px-6 rounded-xl text-slate-700'
    }))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields= ('username','email','password1','password2')
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Username','class': FORM_CLASS}))
    email= forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Your Email', 'class': FORM_CLASS}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Your Password', 'class': FORM_CLASS}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repeat Password', 'class': FORM_CLASS}))
