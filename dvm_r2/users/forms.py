from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

FORM_CLASS = 'w-full py-3 px-6 rounded-xl text-slate-700'

class LoginForm(AuthenticationForm):
      username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': FORM_CLASS
    }))
      password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': FORM_CLASS
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


class UserUpdateForm(forms.ModelForm):
     email = forms.EmailField()
     class Meta:
          model = User
          fields = ['username','email']
     username = forms.CharField(widget=forms.TextInput(attrs={'class': FORM_CLASS}))
     email = forms.CharField(widget=forms.TextInput(attrs={'class': FORM_CLASS}))
          
      


class ProfileAddMoneyForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['wallet_balance']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wallet_balance'].widget.attrs.update({'class': FORM_CLASS})