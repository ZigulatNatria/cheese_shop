from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category, Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'text', 'price', 'amount', 'productCategory', 'units', 'published')
    list_display_links = ('get_image', 'name', 'text', 'price', 'amount', 'productCategory', 'units', 'published')
    search_fields = ('name', 'text', 'published')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="130" height="100"')

    get_image.short_description = 'Изображение'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

# Register your models here.
admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductCategory)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Comment)