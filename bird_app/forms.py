from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post, CustomUser, Comment

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'age', 'name', 'gender',  'email',  'isExpert', 'documents_link')  

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'age', 'name', 'gender',  'email', 'isExpert', 'documents_link')  

class PostForm(ModelForm):
    class Meta:
        model = Post    
        fields = ['title','body','stayAnonymous']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
