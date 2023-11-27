from django.contrib import admin

from .models import Product, Category, Comment

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'price', 'amount', 'image', 'productCategory', 'units')
    list_display_links = ('name', 'text', 'price', 'amount', 'image', 'productCategory', 'units')
    search_fields = ('name', 'text')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')
    list_display_links = ('name', 'text')
    search_fields = ('name', 'text')

# Register your models here.
admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductCategory)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)