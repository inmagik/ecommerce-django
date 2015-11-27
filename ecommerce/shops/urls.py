from django.conf.urls import url, include
from rest_framework_nested import routers
from .views import ShopViewSet, ProductViewSet, ShopProductViewSet

router = routers.SimpleRouter()
router.register(r'shops', ShopViewSet)
router.register(r'products', ProductViewSet)

shops_router = routers.NestedSimpleRouter(router, r'shops', lookup='shop')
shops_router.register(r'products', ShopProductViewSet, base_name='shop-products')
# 'base_name' is optional. Needed only if the same viewset is registered more than once
# Official DRF docs on this option: http://www.django-rest-framework.org/api-guide/routers/

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(shops_router.urls)),
]