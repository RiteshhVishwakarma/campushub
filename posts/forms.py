from django import forms
from .models import Post, PostImage, Report

MAX_PHOTOS = 5
MAX_PHOTO_MB = 5


class MultipleImageInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.ImageField):
    """Accepts several image files from one <input multiple>."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', MultipleImageInput(attrs={'accept': 'image/*'}))
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_clean(d, initial) for d in data if d]
        return [single_clean(data, initial)] if data else []


class PostForm(forms.ModelForm):
    """Form for creating and editing posts (1 to 5 photos)."""

    images = MultipleImageField(required=False, label='Photos')

    class Meta:
        model = Post
        fields = ['category', 'title', 'description', 'price', 'location', 'phone']
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
        }
        labels = {
            'category': 'Category',
            'title': 'Title',
            'description': 'Description',
            'price': 'Price (Optional)',
            'location': 'Location',
            'phone': 'Contact Phone',
        }

    def _existing_keys(self):
        """Keys for the photos this post already has: 'cover' and extra-photo ids."""
        if not self.instance.pk:
            return []
        keys = ['cover'] if self.instance.image else []
        keys += [str(pk) for pk in self.instance.extra_images.values_list('pk', flat=True)]
        return keys

    def clean_images(self):
        files = self.cleaned_data.get('images') or []
        for f in files:
            if f.size > MAX_PHOTO_MB * 1024 * 1024:
                raise forms.ValidationError(f'"{f.name}" is larger than {MAX_PHOTO_MB} MB.')
        return files

    def clean(self):
        cleaned = super().clean()
        existing = self._existing_keys()
        removed = set(self.data.getlist('remove_images')) & set(existing) if hasattr(self.data, 'getlist') else set()
        self.kept_keys = [k for k in existing if k not in removed]
        total = len(self.kept_keys) + len(cleaned.get('images') or [])
        if 'images' not in self.errors:
            if total < 1:
                self.add_error('images', 'Add at least 1 photo.')
            elif total > MAX_PHOTOS:
                self.add_error('images', f'You can add up to {MAX_PHOTOS} photos ({total} selected).')
        return cleaned

    def save(self, commit=True):
        """Save the post, then rebuild its photo list: kept photos first, new ones after."""
        post = super().save(commit=False)
        if not commit:
            return post
        extras = {str(e.pk): e for e in post.extra_images.all()} if post.pk else {}
        photos = [post.image.name if k == 'cover' else extras[k].image.name for k in self.kept_keys]
        photos += self.cleaned_data.get('images') or []

        post.image = photos[0]
        post.save()
        post.extra_images.all().delete()
        for i, photo in enumerate(photos[1:]):
            PostImage.objects.create(post=post, image=photo, order=i)
        return post


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
