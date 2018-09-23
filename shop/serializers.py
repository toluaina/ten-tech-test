from rest_framework import serializers

from shop.models import Brand, Footwear, Hat, Style, Basket, Item


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    """Brand serializer."""

    class Meta:
        model = Brand
        fields = '__all__'


class FootwearSerializer(serializers.HyperlinkedModelSerializer):
    """Footwear serializer."""

    brand = BrandSerializer(read_only=True, required=False)

    class Meta:
        model = Footwear
        exclude = ('style', )


class HatSerializer(serializers.HyperlinkedModelSerializer):
    """Hat serializer."""

    brand_name = serializers.SerializerMethodField()

    style = serializers.CharField(write_only=True, required=True)
    brand = BrandSerializer(write_only=True, required=True)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, write_only=True, required=True
    )
    colour = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Hat
        fields = '__all__'

    def get_brand_name(self, obj):
        if obj.brand is not None:
            return obj.brand.name


class StyleSerializer(serializers.HyperlinkedModelSerializer):
    """Style serializer."""

    class Meta:
        model = Style
        fields = '__all__'


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    """Item serializer."""
    object_type = serializers.CharField(
        read_only=True, source='content_type.model'
    )

    class Meta:
        model = Item
        fields = '__all__'


class BasketSerializer(serializers.HyperlinkedModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Basket
        fields = ('items',)
