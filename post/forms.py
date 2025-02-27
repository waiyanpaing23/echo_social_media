from django import forms
from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']

    text = forms.CharField(label='', widget=forms.Textarea(attrs={
        'placeholder' : 'Write your post here...',
        'class' : 'w-full h-32 border border-gray-300 rounded-md p-2 mb-4'
    }))
    image = forms.ImageField(label='', required=False, widget = forms.FileInput(attrs={
        'class' : 'w-full border border-gray-300 rounded-md p-2 mb-4'
    }))

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

    comment_text = forms.CharField(label='', widget=forms.Textarea(attrs={
        'placeholder' : 'Write a comment...',
        'class' : 'w-full border border-gray-300 rounded-md p-2 my-4',
        'rows' : 2
    }))