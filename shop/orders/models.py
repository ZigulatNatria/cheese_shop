from django.db import models
from showcase.models import Product


class City(models.Model):
    name = models.CharField(verbose_name='город', max_length=50)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField(verbose_name='имя', max_length=50)
    last_name = models.CharField(verbose_name='фамилия', max_length=50)
    email = models.EmailField(verbose_name='электронная почта')
    phone = models.BigIntegerField(verbose_name='телефон')
    address = models.CharField(verbose_name='адрес', max_length=250)
    postal_code = models.IntegerField(verbose_name='почтовый индекс', null=True)
    city = models.ForeignKey('City', verbose_name='город', on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(verbose_name='создано', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлено', auto_now=True)
    paid = models.BooleanField(verbose_name='оплата', default=False)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'№ {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_absolute_url(self):
        return f'/orders/order_list/'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='заказ', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='товар', related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=1)

    class Meta:
        verbose_name = 'элемент заказа'
        verbose_name_plural = 'элементы заказа'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id']),
        ]

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
