"""
Django management command to expire posts older than 30 days.

Usage:
    python manage.py expire_posts
    
This command should be run daily via cron job or task scheduler.
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from posts.models import Post
from datetime import timedelta


class Command(BaseCommand):
    help = 'Mark posts older than 30 days as inactive (expired)'

    def add_arguments(self, parser):
        # Optional: Add dry-run mode
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be expired without actually expiring',
        )

    def handle(self, *args, **options):
        dry_run = options.get('dry_run', False)
        
        # Get the cutoff date (30 days ago)
        expiry_date = timezone.now() - timedelta(days=30)
        
        # Find active posts created before the cutoff date
        expired_posts = Post.objects.filter(
            is_active=True,
            created_at__lt=expiry_date
        )
        
        expired_count = expired_posts.count()
        
        if expired_count == 0:
            self.stdout.write(
                self.style.SUCCESS('No posts to expire.')
            )
            return
        
        if dry_run:
            self.stdout.write(
                self.style.WARNING(f'DRY RUN: Would expire {expired_count} post(s):')
            )
            for post in expired_posts[:10]:  # Show first 10
                days_old = (timezone.now() - post.created_at).days
                self.stdout.write(
                    f'  - [{post.id}] {post.title[:50]} (Created {days_old} days ago)'
                )
            if expired_count > 10:
                self.stdout.write(f'  ... and {expired_count - 10} more')
        else:
            # Mark posts as inactive
            expired_posts.update(is_active=False)
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully expired {expired_count} post(s).')
            )
            
            # Show summary
            self.stdout.write('Summary:')
            self.stdout.write(f'  - Posts expired: {expired_count}')
            self.stdout.write(f'  - Cutoff date: {expiry_date.strftime("%Y-%m-%d %H:%M:%S")}')
            self.stdout.write(f'  - Current time: {timezone.now().strftime("%Y-%m-%d %H:%M:%S")}')
