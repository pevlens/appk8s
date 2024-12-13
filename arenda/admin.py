from django.contrib import admin

# Register your models here.

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Post, CategoryFeature

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent', 'created_at')
    list_filter = ('parent',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'category', 'created_at', 'latitude', 'longitude')
    list_filter = ('category',)
    search_fields = ('title', 'content')

@admin.register(CategoryFeature)
class CategoryFeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'value')