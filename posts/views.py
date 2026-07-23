from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.contrib import messages
from django.utils import timezone
from django.db import IntegrityError, models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Report
from .forms import PostForm, ReportForm


class PostListView(View):
    """List all active posts - public view"""
    template_name = 'posts/post_list.html'

    def get(self, request):
        # Start with all active posts
        posts = Post.objects.filter(is_active=True).select_related('user')
        
        # Get filter parameters
        search_query = request.GET.get('q', '').strip()
        category = request.GET.get('category', '').strip()
        location = request.GET.get('location', '').strip()
        
        # Apply search filter (title, description, location)
        if search_query:
            posts = posts.filter(
                models.Q(title__icontains=search_query) |
                models.Q(description__icontains=search_query) |
                models.Q(location__icontains=search_query)
            )
        
        # Apply category filter
        if category:
            posts = posts.filter(category=category)
        
        # Apply location filter
        if location:
            posts = posts.filter(location__icontains=location)
        
        # Check if filters are active
        has_filters = bool(search_query or category or location)
        
        # Pagination - 15 posts per page
        paginator = Paginator(posts, 15)
        page_number = request.GET.get('page', 1)
        
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page
            page_obj = paginator.get_page(1)
        except EmptyPage:
            # If page is out of range, deliver last page
            page_obj = paginator.get_page(paginator.num_pages)
        
        return render(request, self.template_name, {
            'posts': page_obj,
            'page_obj': page_obj,
            'search_query': search_query,
            'selected_category': category,
            'selected_location': location,
            'has_filters': has_filters,
        })


class PostCreateView(LoginRequiredMixin, View):
    """Create a new post - requires login"""
    template_name = 'posts/post_create.html'
    login_url = 'accounts:login'

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your post has been created successfully!')
            return redirect('posts:post_detail', pk=post.pk)
        return render(request, self.template_name, {'form': form})


class PostDetailView(View):
    """View post details - public view"""
    template_name = 'posts/post_detail.html'

    # Safety tips by category
    SAFETY_TIPS = {
        'ROOMMATE': 'Never transfer money before visiting the property.',
        'FLAT_PG': 'Visit the property before making any payment.',
        'BUY_SELL': 'Meet in a public place before exchanging money.',
        'INTERNSHIP': 'Never pay money for a job opportunity.',
        'EVENT': 'Verify the organizer before attending.',
    }

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk, is_active=True)
        is_owner = request.user.is_authenticated and post.user == request.user
        
        # Determine what phone info to send based on authentication
        if request.user.is_authenticated:
            # Authenticated users see full phone number
            phone_display = post.phone
            show_full_contact = True
        else:
            # Anonymous users see masked phone number
            phone_display = self.mask_phone(post.phone)
            show_full_contact = False
        
        # Check if user has already reported this post
        user_reported = False
        if request.user.is_authenticated:
            user_reported = Report.objects.filter(post=post, user=request.user).exists()
        
        # Get safety tip for this category
        safety_tip = self.SAFETY_TIPS.get(post.category, '')
        
        return render(request, self.template_name, {
            'post': post,
            'is_owner': is_owner,
            'phone_display': phone_display,
            'show_full_contact': show_full_contact,
            'user_reported': user_reported,
            'safety_tip': safety_tip,
        })
    
    def mask_phone(self, phone_number):
        """
        Masks a phone number, showing only the last 2 digits.
        Example: "9876543221" becomes "********21"
        """
        if not phone_number:
            return ""
        
        phone_str = str(phone_number)
        
        # Show only last 2 digits
        if len(phone_str) > 2:
            masked = '*' * (len(phone_str) - 2) + phone_str[-2:]
        elif len(phone_str) == 2:
            masked = '**'
        else:
            masked = '*' * len(phone_str)
        
        return masked


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, View):
    """Edit post - only owner can edit"""
    template_name = 'posts/post_edit.html'
    login_url = 'accounts:login'

    def test_func(self):
        """Check if user is the owner of the post"""
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return post.user == self.request.user

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(request, self.template_name, {'form': form, 'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated successfully!')
            return redirect('posts:post_detail', pk=post.pk)
        return render(request, self.template_name, {'form': form, 'post': post})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    """Delete post - only owner can delete"""
    template_name = 'posts/post_delete_confirm.html'
    login_url = 'accounts:login'

    def test_func(self):
        """Check if user is the owner of the post"""
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return post.user == self.request.user

    def get(self, request, pk):
        """Show confirmation page"""
        post = get_object_or_404(Post, pk=pk)
        return render(request, self.template_name, {'post': post})

    def post(self, request, pk):
        """Delete the post"""
        post = get_object_or_404(Post, pk=pk)
        post.is_active = False
        post.save()
        messages.success(request, 'Your post has been deleted successfully!')
        return redirect('posts:my_posts')


class MyPostsView(LoginRequiredMixin, View):
    """View user's own posts"""
    template_name = 'posts/my_posts.html'
    login_url = 'accounts:login'

    def get(self, request):
        posts = Post.objects.filter(user=request.user, is_active=True)
        
        # Pagination - 15 posts per page
        paginator = Paginator(posts, 15)
        page_number = request.GET.get('page', 1)
        
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.get_page(1)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)
        
        return render(request, self.template_name, {
            'posts': page_obj,
            'page_obj': page_obj,
        })



class ReportPostView(LoginRequiredMixin, View):
    """Report a post - requires login"""
    template_name = 'posts/report_post.html'
    login_url = 'accounts:login'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk, is_active=True)
        
        # Check if user already reported this post
        already_reported = Report.objects.filter(post=post, user=request.user).exists()
        
        if already_reported:
            messages.info(request, 'You have already reported this post.')
            return redirect('posts:post_detail', pk=pk)
        
        form = ReportForm()
        return render(request, self.template_name, {'form': form, 'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk, is_active=True)
        form = ReportForm(request.POST)
        
        if form.is_valid():
            try:
                report = form.save(commit=False)
                report.post = post
                report.user = request.user
                report.save()
                messages.success(request, 'Thank you for your report. We will review it shortly.')
                return redirect('posts:post_detail', pk=pk)
            except IntegrityError:
                # User already reported this post
                messages.info(request, 'You have already reported this post.')
                return redirect('posts:post_detail', pk=pk)
        
        return render(request, self.template_name, {'form': form, 'post': post})
