from rest_framework.viewsets import ModelViewSet

from rest_framework.filters import OrderingFilter
from shop.models import Brand, Footwear, Hat, FootwearStyle
from shop.serializers import (
    BrandSerializer,
    FootwearSerializer,
    HatListSerializer,
    HatRetrieveSerializer,
    HatSerializer,
    FootwearStyleSerializer,
)


class BrandViewSet(ModelViewSet):
    """Brand views everything included."""

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class FootwearViewSet(ModelViewSet):
    """Footwear views everything included."""

    queryset = Footwear.objects.all().order_by('price')
    serializer_class = FootwearSerializer


class HatViewSet(ModelViewSet):
    """Hat views everything included."""

    queryset = Hat.objects.all().order_by('price')

    def get_serializer_class(self):
        """Use NewEventTIMSerializer to create and update."""
        if self.action == 'list':
            return HatListSerializer
        elif self.action == 'retrieve':
            return HatRetrieveSerializer
        return HatSerializer


class FootwearStyleViewSet(ModelViewSet):
    queryset = FootwearStyle.objects.all()
    serializer_class = FootwearStyleSerializer
