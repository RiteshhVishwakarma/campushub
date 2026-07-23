from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """User profile model extending Django's User model"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='User'
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        verbose_name='Phone Number'
    )
    bio = models.CharField(
        max_length=120,
        blank=True,
        verbose_name='Bio'
    )
    college = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='College Name'
    )
    profile_photo = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True,
        verbose_name='Profile Photo'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def get_active_posts_count(self):
        """Return count of active posts by this user"""
        return self.user.posts.filter(is_active=True).count()
    
    def get_initials(self):
        """Get user initials for avatar fallback"""
        if self.user.first_name:
            return self.user.first_name[0].upper()
        return self.user.username[0].upper()
