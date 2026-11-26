from django.contrib import admin
from .models import Post, PostImage, Report


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]


admin.site.register(Report)
