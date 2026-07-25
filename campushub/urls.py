from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
]

# Note: Media files are now served by Cloudinary in both development and production
# No need for local media serving with django.conf.urls.static
