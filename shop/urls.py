"""Shop urls."""

from rest_framework_nested import routers

from shop.views import BrandViewSet, FootwearViewSet, HatViewSet


router = routers.SimpleRouter()

router.register(r'brands', BrandViewSet)
router.register(r'footwear', FootwearViewSet)
router.register(r'hats', HatViewSet)
