from django.contrib import admin

from .models import Shop, ProductClass, ProductField, Product, ProductCategory

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(ProductCategory)


