from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='name',
        unique=True)
    description = models.TextField(
        verbose_name='description',
        blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=128,
        verbose_name='product_name')
    image = models.ImageField(
        upload_to='products_images',
        blank=True)
    short_desc = models.CharField(
        max_length=60,
        verbose_name='product preview description',
        blank=True)
    description = models.TextField(
        verbose_name='product description',
        blank=True)
    price = models.DecimalField(
        max_digits=8,
        verbose_name='product price',
        decimal_places=2,
        default=0)
    quantity = models.PositiveIntegerField(
        verbose_name='product quantity',
        default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
