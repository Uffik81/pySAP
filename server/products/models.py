from django.db import models

# Create your models here.

class GroupProduct(models.Model):
    name = models.CharField(max_length=64, help_text='Наименоание группы')

class Product(models.Model):
    group = models.ForeignKey('GroupProduct', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=64, help_text='Наименоание товара')
    gtin = models.CharField(max_length=14, help_text='GTIN')
    sku  = models.IntegerField(help_text='Код товара')

    def __str__(self):
        return self.name
