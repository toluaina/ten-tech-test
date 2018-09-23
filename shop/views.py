from rest_framework.viewsets import ModelViewSet

from shop.models import Brand, Footwear, Hat
from shop.serializers import BrandSerializer, FootwearSerializer, HatSerializer
from shop import permissions


class BrandViewSet(ModelViewSet):
    """Brand views everything included."""

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (permissions.CanCreateUpdateDestroyBrand,)


class FootwearViewSet(ModelViewSet):
    """Footwear views everything included."""

    queryset = Footwear.objects.all()
    serializer_class = FootwearSerializer
    permission_classes = (permissions.CanCreateUpdateDestroyFootwear,)


class HatViewSet(ModelViewSet):
    """Hat views everything included."""

    queryset = Hat.objects.all()
    serializer_class = HatSerializer
    permission_classes = (permissions.CanCreateUpdateDestroyHat,)
