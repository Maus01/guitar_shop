from .models import Category, Brand, Product, Order

from django.contrib import admin
from django.contrib.sessions.models import Session

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',),}
    
@admin.register(Brand)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',),}
    
@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    
admin.site.register(Session)
admin.site.register(Order)


