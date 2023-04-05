from django.db import models


class Product(models.Model):
    title = models.CharField('Назва', max_length=50)
    description = models.TextField('Опис')
    price = models.IntegerField('Ціна')

    def __str__(self):
        return self.title

    class Meta:
         verbose_name = 'Product'
         verbose_name_plural = 'Products'


class ProductImages(models.Model):
    image = models.ImageField(upload_to="img/products", blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
