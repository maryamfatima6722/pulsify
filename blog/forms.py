from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'category', 'author_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the description', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the author name'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment', 'rows': 3}),
        }
