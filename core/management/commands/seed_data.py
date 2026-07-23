"""
Management command to generate realistic development seed data for CampusHub.
"""
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from accounts.models import Profile
from posts.models import Post


class Command(BaseCommand):
    help = 'Generate realistic development seed data for CampusHub'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Delete all generated seed data before creating new data',
        )

    def handle(self, *args, **options):
        # Indian student names
        first_names = [
            'Aarav', 'Vivaan', 'Aditya', 'Vihaan', 'Arjun', 'Sai', 'Arnav', 'Ayaan',
            'Krishna', 'Ishaan', 'Shaurya', 'Atharva', 'Advik', 'Pranav', 'Reyansh',
            'Ananya', 'Diya', 'Aadhya', 'Avni', 'Sara', 'Pari', 'Anvi', 'Anika',
            'Navya', 'Kavya', 'Kiara', 'Saanvi', 'Riya', 'Ishita', 'Prisha'
        ]
        
        last_names = [
            'Sharma', 'Verma', 'Patel', 'Kumar', 'Singh', 'Reddy', 'Desai', 'Joshi',
            'Mehta', 'Gupta', 'Agarwal', 'Rao', 'Nair', 'Iyer', 'Das', 'Pandey',
            'Mishra', 'Kulkarni', 'Chopra', 'Malhotra', 'Kapoor', 'Bhat', 'Pillai',
            'Menon', 'Shah', 'Gandhi', 'More', 'Patil', 'Sawant', 'Thakur'
        ]

        # Pune locations
        pune_locations = [
            'Lohegaon', 'Viman Nagar', 'Kharadi', 'Wagholi', 'Vishrantwadi',
        ]

        # Colleges
        colleges = [
            'Aditya Pune University', 'MIT College', 'PICT Pune', 'VIT Pune',
            'Symbiosis Institute', 'COEP Pune', 'Fergusson College'
        ]

        # Post templates by category
        post_templates = {
            'ROOMMATE': {
                'titles': [
                    'Looking for Roommate in {}',
                    'Roommate Needed for Shared Flat in {}',
                    'Need a Roommate Near {}',
                    'Searching for Flatmate in {}',
                    'Room Available for Student in {}',
                ],
                'descriptions': [
                    'Looking for a responsible roommate to share a 2BHK flat. Fully furnished with all amenities. Preferred working professional or student. Non-smoking preferred.',
                    'Need a roommate for sharing rent and expenses. Spacious room with attached bathroom. Close to metro station and market. Vegetarian preferred.',
                    'Room available immediately. Looking for someone clean and responsible. WiFi and electricity included. Friendly environment.',
                    'Searching for a compatible roommate. The flat has good ventilation and natural light. Peaceful neighborhood with all facilities nearby.',
                    'Looking for a student or working professional as roommate. Rent is negotiable. Close to bus stop and college.',
                ],
                'has_price': True,
                'price_range': (5000, 12000),
            },
            'FLAT_PG': {
                'titles': [
                    '2BHK Flat Available in {}',
                    'PG Accommodation for Students in {}',
                    'Affordable Flat for Rent in {}',
                    '1BHK Flat Available Near {}',
                    'Spacious PG with Food in {}',
                ],
                'descriptions': [
                    'Well-maintained 2BHK flat available for rent. Semi-furnished with modular kitchen. Parking available. Suitable for family or working professionals.',
                    'PG accommodation with all meals included. Separate rooms available. WiFi, laundry, and housekeeping provided. Girls only / Boys only.',
                    'Affordable flat in a prime location. Close to colleges and tech parks. Public transport easily accessible. Ready to move in.',
                    'Spacious 1BHK with balcony. Newly painted and clean. Water 24/7. Maintenance included in rent.',
                    'PG with homely food and comfortable stay. AC rooms available. Study table and almirah provided. Safe and secure environment.',
                ],
                'has_price': True,
                'price_range': (8000, 25000),
            },
            'EVENT': {
                'titles': [
                    'Tech Fest at {} - Register Now',
                    'Cultural Night Event in {}',
                    'Hackathon Competition at {}',
                    'Sports Tournament Near {}',
                    'Workshop on Web Development in {}',
                ],
                'descriptions': [
                    'Join us for an amazing tech fest featuring coding competitions, robotics, and project exhibitions. Free entry for students. Prizes worth 1 lakh!',
                    'Cultural night featuring dance, music, and drama performances. Open to all students. Food stalls and games available. Entry free.',
                    '24-hour hackathon with exciting problem statements. Team of 2-4 members. Great networking opportunity. Refreshments provided.',
                    'Inter-college sports tournament. Multiple events including cricket, football, badminton. Register your team now. Limited slots.',
                    'Free workshop on full-stack web development. Learn Django, React, and deployment. Certificate provided. Limited seats available.',
                ],
                'has_price': False,
            },
            'INTERNSHIP': {
                'titles': [
                    'Software Development Internship at {}',
                    'Marketing Intern Needed in {}',
                    'Web Development Internship in {}',
                    'Content Writing Internship Near {}',
                    'Data Analytics Intern at {}',
                ],
                'descriptions': [
                    'Looking for enthusiastic interns for software development role. Good knowledge of Python/Java required. 3-6 months internship. Stipend provided.',
                    'Marketing internship opportunity with a growing startup. Learn digital marketing, content creation, and campaigns. Work from office. Flexible timings.',
                    'Web development internship for students with knowledge of HTML, CSS, JavaScript. Build real projects. Certificate and stipend provided.',
                    'Content writing internship for creative writers. Write blogs, articles, and social media content. Remote work option available.',
                    'Data analytics internship with hands-on experience in Python, SQL, and visualization tools. Learn from industry experts. PPO available.',
                ],
                'has_price': True,
                'price_range': (5000, 15000),
            },
            'BUY_SELL': {
                'titles': [
                    'Laptop for Sale - {}',
                    'Study Books Available in {}',
                    'Bicycle for Sale in {}',
                    'Gaming Console for Sale Near {}',
                    'Furniture for Sale in {}',
                ],
                'descriptions': [
                    'Dell Inspiron laptop in excellent condition. 8GB RAM, 512GB SSD, Intel i5 processor. Battery backup 4-5 hours. Bill and box available.',
                    'Engineering textbooks for sale. All subjects covered. Minimal highlighting. Half the original price. Good condition.',
                    'Hero bicycle for sale. Well maintained with new tires. Perfect for daily commuting. Gears working smoothly.',
                    'PlayStation 4 with 2 controllers and 5 games. Rarely used. Like new condition. All cables included.',
                    'Study table and chair for sale. Wooden, sturdy build. Suitable for students. Pickup only. Negotiable price.',
                ],
                'has_price': True,
                'price_range': (500, 30000),
            },
        }

        # Clear data if --clear flag is provided
        if options['clear']:
            self.stdout.write(self.style.WARNING('Clearing existing seed data...'))
            
            # Delete seed users (username starts with 'seed_user_')
            seed_users = User.objects.filter(username__startswith='seed_user_')
            seed_count = seed_users.count()
            seed_users.delete()
            
            self.stdout.write(self.style.SUCCESS(f'Deleted {seed_count} seed users and their related data'))

        # Generate 30 users
        self.stdout.write(self.style.SUCCESS('Creating seed users...'))
        users_created = 0
        
        for i in range(1, 31):
            username = f'seed_user_{i}'
            
            # Skip if user already exists
            if User.objects.filter(username=username).exists():
                continue
            
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            email = f'{username}@student.com'
            
            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password='seedpass123',
                first_name=first_name,
                last_name=last_name
            )
            
            # Update profile (auto-created by signal)
            profile = user.profile
            profile.phone = f'+91{random.randint(7000000000, 9999999999)}'
            profile.bio = random.choice([
                'Student passionate about technology',
                'Engineering student and tech enthusiast',
                'Love coding and building things',
                'Final year student looking for opportunities',
                'Part-time developer and full-time learner',
            ])
            profile.college = random.choice(colleges)
            profile.save()
            
            users_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {users_created} users'))

        # Generate 100 active posts
        self.stdout.write(self.style.SUCCESS('Creating seed posts...'))
        posts_created = 0
        
        # Get all seed users
        seed_users = list(User.objects.filter(username__startswith='seed_user_'))
        
        if not seed_users:
            self.stdout.write(self.style.ERROR('No seed users available. Create users first.'))
            return
        
        # Distribute posts across categories
        category_distribution = {
            'ROOMMATE': 25,
            'FLAT_PG': 25,
            'EVENT': 20,
            'INTERNSHIP': 15,
            'BUY_SELL': 15,
        }
        
        for category, count in category_distribution.items():
            template = post_templates[category]
            
            for _ in range(count):
                user = random.choice(seed_users)
                location = random.choice(pune_locations)
                
                # Generate post data
                title = random.choice(template['titles']).format(location)
                description = random.choice(template['descriptions'])
                phone = user.profile.phone
                
                # Set price based on category
                price = None
                if template['has_price']:
                    min_price, max_price = template['price_range']
                    price = random.randint(min_price // 1000, max_price // 1000) * 1000
                
                # Create post with random creation date (within last 20 days)
                days_ago = random.randint(0, 20)
                created_at = timezone.now() - timezone.timedelta(days=days_ago)
                
                post = Post.objects.create(
                    user=user,
                    title=title,
                    description=description,
                    category=category,
                    price=price,
                    location=location,
                    phone=phone,
                    is_active=True,
                )
                
                # Set custom created_at
                post.created_at = created_at
                post.save()
                
                posts_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {posts_created} posts'))
        
        # Summary
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('═' * 50))
        self.stdout.write(self.style.SUCCESS('SEED DATA GENERATION COMPLETE'))
        self.stdout.write(self.style.SUCCESS('═' * 50))
        self.stdout.write(f'Users created: {users_created}')
        self.stdout.write(f'Posts created: {posts_created}')
        self.stdout.write('')
        self.stdout.write('Test credentials:')
        self.stdout.write('  Username: seed_user_1 to seed_user_30')
        self.stdout.write('  Password: seedpass123')
        self.stdout.write('')
        self.stdout.write('To clear seed data: python manage.py seed_data --clear')
        self.stdout.write(self.style.SUCCESS('═' * 50))
