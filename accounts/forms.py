from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
import re


class UserRegistrationForm(UserCreationForm):
    """Custom user registration form with additional fields"""
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name',
            'class': 'form-input'
        }),
        label='Name'
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-input'
        }),
        label='Email'
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Choose a username',
            'class': 'form-input'
        }),
        label='Username'
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Create a password',
            'class': 'form-input'
        }),
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm your password',
            'class': 'form-input'
        }),
        label='Confirm Password'
    )

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        """Validate that email is unique"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email

    def clean_username(self):
        """Validate that username is unique"""
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username


class UserLoginForm(AuthenticationForm):
    """Custom login form that accepts username or email"""
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username or Email',
            'class': 'form-input'
        }),
        label='Username or Email'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'form-input'
        }),
        label='Password'
    )



class ProfileEditForm(forms.ModelForm):
    """Form for editing user profile"""
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your full name',
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-colors'
        }),
        label='Full Name'
    )
    
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio', 'phone']
        widgets = {
            'profile_photo': forms.FileInput(attrs={
                'class': 'hidden',
                'accept': 'image/*'
            }),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Write a short bio about yourself...',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-colors resize-none',
                'rows': 3,
                'maxlength': 120
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+1234567890',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-colors'
            })
        }
        labels = {
            'profile_photo': 'Profile Photo',
            'bio': 'Bio',
            'phone': 'Phone Number'
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['first_name'].initial = self.user.first_name
    
    def clean_phone(self):
        """Validate phone number format"""
        phone = self.cleaned_data.get('phone')
        if phone:
            # Remove spaces and special characters
            phone_cleaned = re.sub(r'[^0-9+]', '', phone)
            # Check if it's a valid phone number (10-15 digits, optional +)
            if not re.match(r'^\+?[0-9]{10,15}$', phone_cleaned):
                raise forms.ValidationError('Please enter a valid phone number (10-15 digits).')
            return phone_cleaned
        return phone
    
    def clean_bio(self):
        """Validate bio length"""
        bio = self.cleaned_data.get('bio')
        if bio and len(bio) > 120:
            raise forms.ValidationError('Bio cannot exceed 120 characters.')
        return bio
    
    def clean_profile_photo(self):
        """Validate profile photo size"""
        photo = self.cleaned_data.get('profile_photo')
        if photo:
            # Check if it's a new upload (has size attribute)
            if hasattr(photo, 'size'):
                # Limit to 5MB
                if photo.size > 5 * 1024 * 1024:
                    raise forms.ValidationError('Profile photo size cannot exceed 5MB.')
        return photo
    
    def save(self, commit=True):
        """Save profile and update user's first_name"""
        profile = super().save(commit=False)
        if self.user:
            self.user.first_name = self.cleaned_data.get('first_name')
            if commit:
                self.user.save()
        if commit:
            profile.save()
        return profile
