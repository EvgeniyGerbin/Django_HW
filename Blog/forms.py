from django import forms
from Blog.models import Post, CommentPost


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = '__all__'