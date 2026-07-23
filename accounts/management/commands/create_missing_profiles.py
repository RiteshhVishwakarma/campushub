from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile


class Command(BaseCommand):
    help = 'Create profiles for users who do not have one'

    def handle(self, *args, **options):
        users_without_profile = []
        
        for user in User.objects.all():
            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                users_without_profile.append(user.username)
        
        if users_without_profile:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Created profiles for {len(users_without_profile)} users: {", ".join(users_without_profile)}'
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('All users already have profiles!')
            )
