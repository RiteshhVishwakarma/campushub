from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserLoginForm, ProfileEditForm
from .models import Profile


class RegisterView(View):
    """User registration view"""
    template_name = 'accounts/register.html'
    form_class = UserRegistrationForm

    def get(self, request):
        # Redirect if already logged in
        if request.user.is_authenticated:
            return redirect('core:home')
        
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to CampusHub, {user.first_name}! Your account has been created successfully.')
            
            # Redirect to next parameter or home
            next_url = request.GET.get('next') or request.POST.get('next') or 'core:home'
            return redirect(next_url)
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    """User login view that accepts username or email"""
    template_name = 'accounts/login.html'
    form_class = UserLoginForm

    def get(self, request):
        # Redirect if already logged in
        if request.user.is_authenticated:
            return redirect('core:home')
        
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        
        # Get username/email from form
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')
        
        # Try to authenticate with username first
        user = authenticate(request, username=username_or_email, password=password)
        
        # If authentication fails, try with email
        if user is None:
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            
            # Redirect to next parameter or home
            next_url = request.GET.get('next') or request.POST.get('next') or 'core:home'
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username/email or password. Please try again.')
            form = self.form_class()
            return render(request, self.template_name, {'form': form})


class LogoutView(LoginRequiredMixin, View):
    """User logout view"""
    login_url = 'accounts:login'

    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('core:home')

    def post(self, request):
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('core:home')


class ProfileView(LoginRequiredMixin, View):
    """User profile view"""
    template_name = 'accounts/profile.html'
    login_url = 'accounts:login'

    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        active_posts_count = profile.get_active_posts_count()
        return render(request, self.template_name, {
            'user': request.user,
            'profile': profile,
            'active_posts_count': active_posts_count
        })


class EditProfileView(LoginRequiredMixin, View):
    """Edit profile view"""
    template_name = 'accounts/edit_profile.html'
    login_url = 'accounts:login'
    form_class = ProfileEditForm

    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = self.form_class(instance=profile, user=request.user)
        return render(request, self.template_name, {
            'form': form,
            'profile': profile
        })

    def post(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = self.form_class(
            request.POST, 
            request.FILES, 
            instance=profile, 
            user=request.user
        )
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('accounts:profile')
        
        return render(request, self.template_name, {
            'form': form,
            'profile': profile
        })
