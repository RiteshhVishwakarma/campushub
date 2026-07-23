from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Post(models.Model):
    """Post model for campus community posts"""
    
    class CategoryChoices(models.TextChoices):
        ROOMMATE = 'ROOMMATE', 'Roommate'
        FLAT_PG = 'FLAT_PG', 'Flat / PG'
        EVENT = 'EVENT', 'Event'
        INTERNSHIP = 'INTERNSHIP', 'Internship'
        BUY_SELL = 'BUY_SELL', 'Buy & Sell'
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='User'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Title'
    )
    description = models.TextField(
        verbose_name='Description'
    )
    category = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
        verbose_name='Category'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Price'
    )
    location = models.CharField(
        max_length=200,
        verbose_name='Location'
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Contact Phone'
    )
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True,
        verbose_name='Image'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is Active'
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.get_category_display()}"
    
    def get_expiry_date(self):
        """Get the date when this post will expire (30 days after creation)"""
        return self.created_at + timedelta(days=30)
    
    def is_expired(self):
        """Check if the post has expired (more than 30 days old)"""
        return timezone.now() > self.get_expiry_date()
    
    def days_until_expiry(self):
        """Get the number of days until the post expires"""
        time_diff = self.get_expiry_date() - timezone.now()
        days = time_diff.days
        return max(0, days)  # Return 0 if already expired
    
    def get_expiry_display(self):
        """Get a human-readable expiry message"""
        days = self.days_until_expiry()
        if days == 0:
            return "Expires today"
        elif days == 1:
            return "Expires in 1 day"
        else:
            return f"Expires in {days} days"


class Report(models.Model):
    """Report model for flagging inappropriate posts"""
    
    class ReasonChoices(models.TextChoices):
        SPAM = 'SPAM', 'Spam'
        FAKE = 'FAKE', 'Fake Information'
        WRONG_CATEGORY = 'WRONG_CATEGORY', 'Wrong Category'
        SCAM = 'SCAM', 'Scam'
        OTHER = 'OTHER', 'Other'
    
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='reports',
        verbose_name='Post'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reports',
        verbose_name='Reported By'
    )
    reason = models.CharField(
        max_length=20,
        choices=ReasonChoices.choices,
        verbose_name='Reason'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Reported At'
    )

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
        ordering = ['-created_at']
        # Ensure a user can only report a post once
        unique_together = ['post', 'user']

    def __str__(self):
        return f"Report by {self.user.username} on {self.post.title}"
