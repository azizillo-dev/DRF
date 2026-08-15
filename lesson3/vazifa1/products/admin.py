from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'stock', 'is_active']
    list_filter = ['is_active', 'stock', 'price']
    search_fields = ['title', 'description']
    ordering = ['-created_at']
    