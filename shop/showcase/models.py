from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(verbose_name='название', max_length=50)
    text = models.TextField(verbose_name='описание', null=True, blank=True)
    image = models.ImageField(verbose_name='изображение', null=True, width_field=None, height_field=None, upload_to='images/') #TODO убрать null=True полсле сброса базы

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='название', max_length=50)
    text = models.TextField(verbose_name='описание', null=True, blank=True)
    price = models.FloatField(verbose_name='цена', null=True, blank=True)
    amount = models.IntegerField(verbose_name='количество', null=True, blank=True)
    image = models.ImageField(verbose_name='фото', width_field=None, height_field=None, upload_to='images/')
    # productCategory = models.ManyToManyField(Category, through='ProductCategory')
    productCategory = models.ForeignKey('Category', verbose_name='категория продукта', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def take(self):   #TODO переделать алгоритм уменьшения колличества товара по человечески
        self.amount -= 1
        self.save()


class Comment(models.Model):
    comment_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    author_comment = models.CharField(max_length=30, verbose_name='Автор')
    ia_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить на экран?')
    text = models.TextField(verbose_name='Содержание')
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опуюликован')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['created']


# class ProductCategory(models.Model):
#     product_category = models.ForeignKey(Product, on_delete=models.CASCADE)
#     category_product = models.ForeignKey(Category, on_delete=models.CASCADE)


