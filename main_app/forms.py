from django import forms
from main_app.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']