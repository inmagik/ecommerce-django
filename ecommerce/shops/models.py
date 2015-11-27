#from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField
from jsonfield import JSONField
import collections


class Shop(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s" % self.name


class ProductCategory(models.Model):
    shop = models.ForeignKey(Shop, related_name="product_categories")
    name = models.CharField(max_length=255)
    order = models.IntegerField(blank=True, default=1)

    def __unicode__(self):
        return u"%s" % self.name    

    class Meta:
        verbose_name_plural = "Product categories"
        ordering = ["order"]


class ProductClass(models.Model):
    name = models.CharField(max_length=255)
    shop = models.ForeignKey(Shop)

    def __unicode__(self):
        return u"%s - %s" % (self.name, self.shop.name)


class ProductField(models.Model):
    name = models.CharField(max_length=255)
    product_class = models.ForeignKey(ProductClass)
    order = models.IntegerField(blank=True, default=1)

    def __unicode__(self):
        return u"%s" % self.name


class Product(models.Model):
    shop = models.ForeignKey(Shop)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name', unique_with=['shop__id'])
    product_category = models.ForeignKey(ProductCategory, null=True, blank=True)
    product_class = models.ForeignKey(ProductClass, null=True, blank=True)
    product_code = models.CharField(max_length=255, null=True, blank=True)
    
    base_price = models.FloatField()
    properties = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict}, null=True, blank=True)
    order = models.IntegerField(blank=True, default=1)

    def __unicode__(self):
        return u"%s - %s" % (self.name, self.shop.name)



