from django.contrib import admin

from .models import Category, Product, Size, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'child_category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SubCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent_category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'sub_category', 'name', 'slug', 'price',
                    'availability', 'created']
    list_filter = ['availability', 'created']
    list_editable = ['price', 'availability']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['title']
