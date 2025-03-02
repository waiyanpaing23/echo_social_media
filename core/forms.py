from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={
        'placeholder' : 'Username',
        'class' : 'w-[100%] bg-transparent border border-zinc-500 focus:outline-zinc-700 rounded-md p-3 mb-5'
    }))
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={
        'placeholder' : 'Password',
        'class' : 'w-[100%] bg-transparent border border-zinc-500 focus:outline-zinc-700 rounded-md p-3 mb-5'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder' : 'Username',
        'class' : 'w-[100%] bg-transparent border border-zinc-500 focus:outline-zinc-700 rounded-md p-3 mt-5'
    }))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={
        'placeholder' : 'Email',
        'class' : 'w-[100%] bg-transparent border border-zinc-500 focus:outline-zinc-700 rounded-md p-3 mt-5'
    }))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder' : 'Password',
        'class' : 'w-[100%] bg-transparent border border-zinc-500 focus:outline-zinc-700 rounded-md p-3 mt-5'
    }))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm Password',
        'class' : 'w-[100%] bg-transparent border border-zinc-500 focus:outline-zinc-700 rounded-md p-3 mt-5'
    }))

class EditUserForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email']

    username = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={
        'placeholder' : 'Username',
        'class' : 'w-full border border-gray-300 rounded-md p-2 mb-4',
    }))
    email = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={
        'placeholder' : 'Email',
        'class' : 'w-full border border-gray-300 rounded-md p-2 mb-4'
    }))

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_img', 'bio', 'location']

    profile_img = forms.ImageField(label='', required=False, widget=forms.FileInput(attrs={
        'class' : 'border border-gray-300 rounded-md p-2 mb-4',
        'onchange' : 'loadFile(event)'
    }))
    bio = forms.CharField(label='', required=False, widget=forms.Textarea(attrs={
        'placeholder' : 'Write a Bio',
        'class' : 'w-full border border-gray-300 rounded-md p-2 mb-4',
        'rows' : 2
    }))
    location = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={
        'placeholder' : 'Location',
        'class' : 'w-full border border-gray-300 rounded-md p-2 mb-4'
    }))
