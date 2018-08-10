"""Shop urls."""

from rest_framework_nested import routers

from shop.views import BrandViewSet, FootwearViewSet, HatViewSet, FootwearStyleViewSet


router = routers.SimpleRouter()

router.register(r'brands', BrandViewSet)
router.register(r'footwear', FootwearViewSet)
router.register(r'hats', HatViewSet)
router.register(r'footwear_styles', FootwearStyleViewSet)
