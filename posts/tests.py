import io
import shutil
import tempfile

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from PIL import Image

from .models import Post

TEMP_MEDIA = tempfile.mkdtemp()


def photo(name='p.png'):
    buf = io.BytesIO()
    Image.new('RGB', (4, 4), 'red').save(buf, 'PNG')
    return SimpleUploadedFile(name, buf.getvalue(), content_type='image/png')


@override_settings(
    MEDIA_ROOT=TEMP_MEDIA,
    STORAGES={
        'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'},
        'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'},
    },
)
class PostPhotosTests(TestCase):
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA, ignore_errors=True)

    def setUp(self):
        self.user = User.objects.create_user('alice', password='pw12345!')
        self.client.force_login(self.user)

    def data(self, **extra):
        base = {
            'category': 'BUY_SELL', 'title': 'Laptop', 'description': 'Good laptop',
            'price': '1000', 'location': 'Kharadi', 'phone': '9876543210',
        }
        base.update(extra)
        return base

    def create(self, n):
        files = [photo(f'p{i}.png') for i in range(n)]
        return self.client.post(reverse('posts:post_create'), self.data(images=files))

    def test_create_requires_at_least_one_photo(self):
        resp = self.create(0)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Add at least 1 photo.')
        self.assertFalse(Post.objects.exists())

    def test_create_rejects_more_than_five(self):
        resp = self.create(6)
        self.assertContains(resp, 'up to 5 photos')
        self.assertFalse(Post.objects.exists())

    def test_create_with_three_photos(self):
        resp = self.create(3)
        post = Post.objects.get()
        self.assertRedirects(resp, reverse('posts:post_detail', args=[post.pk]))
        self.assertTrue(post.image)
        self.assertEqual(post.extra_images.count(), 2)
        self.assertEqual(len(post.gallery()), 3)

        detail = self.client.get(reverse('posts:post_detail', args=[post.pk]))
        self.assertContains(detail, 'class="pd-slide"', count=3)
        self.assertContains(detail, '1/3')

    def test_edit_remove_cover_promotes_next_photo(self):
        self.create(2)
        post = Post.objects.get()
        second = post.extra_images.get().image.name
        resp = self.client.post(
            reverse('posts:post_edit', args=[post.pk]),
            self.data(remove_images=['cover'], images=[photo('new.png')]),
        )
        self.assertEqual(resp.status_code, 302)
        post.refresh_from_db()
        self.assertEqual(post.image.name, second)
        self.assertEqual(len(post.gallery()), 2)

    def test_edit_cannot_remove_every_photo(self):
        self.create(1)
        post = Post.objects.get()
        resp = self.client.post(
            reverse('posts:post_edit', args=[post.pk]), self.data(remove_images=['cover'])
        )
        self.assertContains(resp, 'Add at least 1 photo.')
        post.refresh_from_db()
        self.assertTrue(post.image)

    def test_edit_cannot_exceed_five(self):
        self.create(4)
        post = Post.objects.get()
        resp = self.client.post(
            reverse('posts:post_edit', args=[post.pk]),
            self.data(images=[photo('a.png'), photo('b.png')]),
        )
        self.assertContains(resp, 'up to 5 photos')
        self.assertEqual(len(post.gallery()), 4)
