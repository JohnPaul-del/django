from django.db import models
from django.conf import settings
from django.db.models import PositiveIntegerField

import basketapp
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    quantity = PositiveIntegerField(
        verbose_name='quantity',
        default=0,
    )
    add_datetime = models.DateTimeField(
        verbose_name='add_datetime',
        auto_now=True,
    )

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity

    @property
    def total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        _total_amount = sum(list(map(lambda x: x.product_cost, _items)))
        return _total_amount

