from django.contrib import admin

# Register your models here.
from .models import Product, GroupProduct

admin.site.register(GroupProduct)
admin.site.register(Product)
