# CampusHub - Database Models Complete

## ✅ Models Created

### 1. Profile Model (accounts/models.py)

**Location:** `accounts/models.py`

**Fields:**
- `user` - OneToOneField with User model (CASCADE delete)
- `phone` - CharField (max 15 chars, optional)
- `college` - CharField (max 200 chars, optional)
- `profile_photo` - ImageField (upload to 'profiles/', optional)
- `created_at` - DateTimeField (auto_now_add)

**Features:**
- ✅ Proper verbose_name on all fields
- ✅ OneToOne relationship with Django User
- ✅ related_name='profile' for reverse lookup
- ✅ `__str__` method returns "username's Profile"
- ✅ Meta ordering by newest first (-created_at)
- ✅ Registered in admin

**Relationship:**
```python
user.profile  # Access profile from user
profile.user  # Access user from profile
```

---

### 2. Post Model (posts/models.py)

**Location:** `posts/models.py`

**Fields:**
- `user` - ForeignKey to User (CASCADE delete)
- `title` - CharField (max 200 chars)
- `description` - TextField
- `category` - CharField with TextChoices
- `price` - DecimalField (10 digits, 2 decimals, nullable)
- `location` - CharField (max 200 chars)
- `phone` - CharField (max 15 chars)
- `image` - ImageField (upload to 'posts/', optional)
- `created_at` - DateTimeField (auto_now_add)
- `updated_at` - DateTimeField (auto_now)
- `is_active` - BooleanField (default True)

**Category Choices (TextChoices):**
```python
ROOMMATE = 'ROOMMATE', 'Roommate'
FLAT_PG = 'FLAT_PG', 'Flat / PG'
EVENT = 'EVENT', 'Event'
INTERNSHIP = 'INTERNSHIP', 'Internship'
BUY_SELL = 'BUY_SELL', 'Buy & Sell'
```

**Features:**
- ✅ Proper verbose_name on all fields
- ✅ ForeignKey relationship with User
- ✅ related_name='posts' for reverse lookup
- ✅ CategoryChoices using Django TextChoices
- ✅ Nullable price field for posts without pricing
- ✅ `__str__` method returns "title - Category"
- ✅ Meta ordering by newest first (-created_at)
- ✅ Registered in admin

**Relationship:**
```python
user.posts.all()  # Get all posts by user
post.user  # Access user from post
post.get_category_display()  # Get human-readable category
```

---

## 📊 Database Schema

### Profile Table
| Field | Type | Constraints |
|-------|------|-------------|
| id | BigAutoField | Primary Key |
| user_id | BigInteger | Foreign Key (OneToOne), NOT NULL |
| phone | VARCHAR(15) | Nullable |
| college | VARCHAR(200) | Nullable |
| profile_photo | VARCHAR(100) | Nullable |
| created_at | DateTime | NOT NULL |

### Post Table
| Field | Type | Constraints |
|-------|------|-------------|
| id | BigAutoField | Primary Key |
| user_id | BigInteger | Foreign Key, NOT NULL |
| title | VARCHAR(200) | NOT NULL |
| description | TEXT | NOT NULL |
| category | VARCHAR(20) | NOT NULL, Choices |
| price | Decimal(10,2) | Nullable |
| location | VARCHAR(200) | NOT NULL |
| phone | VARCHAR(15) | NOT NULL |
| image | VARCHAR(100) | Nullable |
| created_at | DateTime | NOT NULL |
| updated_at | DateTime | NOT NULL |
| is_active | Boolean | Default TRUE |

---

## 🗄️ Migrations

### Applied Migrations
- ✅ `accounts/migrations/0001_initial.py` - Profile model
- ✅ `posts/migrations/0001_initial.py` - Post model

### Migration Status
```bash
accounts
 [X] 0001_initial

posts
 [X] 0001_initial
```

---

## ✅ Verification

### System Check
```bash
python manage.py check
```
**Result:** System check identified no issues (0 silenced)

### Migrations Status
```bash
python manage.py showmigrations
```
**Result:** All migrations applied successfully

---

## 🎯 Model Usage Examples

### Create a Profile
```python
from django.contrib.auth.models import User
from accounts.models import Profile

user = User.objects.get(username='john')
profile = Profile.objects.create(
    user=user,
    phone='1234567890',
    college='MIT',
    profile_photo='profiles/john.jpg'
)
```

### Create a Post
```python
from posts.models import Post

post = Post.objects.create(
    user=user,
    title='Looking for Roommate',
    description='Need a roommate near campus...',
    category=Post.CategoryChoices.ROOMMATE,
    location='Cambridge, MA',
    phone='1234567890',
    image='posts/room.jpg'
)
```

### Query Posts
```python
# Get all active posts
Post.objects.filter(is_active=True)

# Get posts by category
Post.objects.filter(category=Post.CategoryChoices.ROOMMATE)

# Get posts by user
user.posts.all()

# Get latest posts
Post.objects.all()[:10]  # Already ordered by -created_at
```

---

## 📁 File Changes

### Created/Modified Files
1. ✅ `accounts/models.py` - Profile model
2. ✅ `posts/models.py` - Post model with CategoryChoices
3. ✅ `accounts/admin.py` - Admin registration
4. ✅ `posts/admin.py` - Admin registration
5. ✅ `accounts/migrations/0001_initial.py` - Profile migration
6. ✅ `posts/migrations/0001_initial.py` - Post migration

---

## 🚫 NOT Created (As Per Instructions)

- ❌ Forms
- ❌ Views
- ❌ Templates
- ❌ Admin customizations (only basic registration)
- ❌ Business logic

---

## 🎉 Summary

**Models:** 2 created
**Migrations:** 2 generated and applied
**Database:** Ready for data
**Admin:** Models registered
**System Check:** 0 issues

---

## 🔍 Next Steps (Awaiting Instructions)

The database models are complete and ready for:
1. Form creation
2. View implementation
3. Template updates
4. Admin customization
5. Business logic

**Status:** ✅ Models Complete - Database Ready

---

**Generated:** July 23, 2026
**Django Version:** 6.0.7
**Database:** SQLite3
