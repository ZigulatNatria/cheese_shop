from django.db import models
from showcase.models import Product


class Order(models.Model):
    first_name = models.CharField(verbose_name='имя', max_length=50)
    last_name = models.CharField(verbose_name='фамилия', max_length=50)
    email = models.EmailField(verbose_name='электронная почта')
    address = models.CharField(verbose_name='адрес', max_length=250)
    postal_code = models.CharField(verbose_name='почтовый индекс', max_length=20)
    city = models.CharField(verbose_name='город', max_length=100)
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

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
