from django.contrib import admin

from .models import Shop, ProductClass, ProductField, Product

admin.site.register(Shop)
admin.site.register(Product)

