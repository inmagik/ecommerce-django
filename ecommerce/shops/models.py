from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField
from jsonfield import JSONField
import collections


class Shop(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s" % self.name


class ProductClass(models.Model):
    name = models.CharField(max_length=255)
    shop = models.ForeignKey(Shop)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.shop.name)


class ProductField(models.Model):
    name = models.CharField(max_length=255)
    product_class = models.ForeignKey(ProductClass)

    def __unicode__(self):
        return "%s" % self.name


class Product(models.Model):
    shop = models.ForeignKey(Shop)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=lambda instance: instance.name,
        unique_with=['shop__pk'], slugify=lambda value: value.replace(' ','-'))
    product_class = models.ForeignKey(ProductClass, null=True, blank=True)
    product_code = models.CharField(max_length=255, null=True, blank=True)
    
    base_price = models.FloatField()
    properties = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict})

    def __unicode__(self):
        return "%s - %s" % (self.name, self.shop.name)



