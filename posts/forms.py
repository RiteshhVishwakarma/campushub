from django import forms
from .models import Post, Report


class PostForm(forms.ModelForm):
    """Form for creating and editing posts"""
    
    class Meta:
        model = Post
        fields = ['category', 'title', 'description', 'price', 'location', 'phone', 'image']
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-input',
            }),
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter post title',
                'class': 'form-input',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe your post in detail',
                'class': 'form-input',
                'rows': 5,
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter price (optional)',
                'class': 'form-input',
                'step': '0.01',
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Enter location',
                'class': 'form-input',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Enter contact phone number',
                'class': 'form-input',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-input',
                'accept': 'image/*',
            }),
        }
        labels = {
            'category': 'Category',
            'title': 'Title',
            'description': 'Description',
            'price': 'Price (Optional)',
            'location': 'Location',
            'phone': 'Contact Phone',
            'image': 'Image (Optional)',
        }


class ReportForm(forms.ModelForm):
    """Form for reporting posts"""
    
    class Meta:
        model = Report
        fields = ['reason']
        widgets = {
            'reason': forms.RadioSelect(),
        }
        labels = {
            'reason': 'Why are you reporting this post?',
        }
