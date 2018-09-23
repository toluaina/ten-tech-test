from rest_framework import serializers

from shop.models import Brand, Footwear, Hat


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    """Brand serializer."""

    class Meta:
        model = Brand
        fields = '__all__'


class FootwearSerializer(serializers.HyperlinkedModelSerializer):
    """Footwear serializer."""

    class Meta:
        model = Footwear
        exclude = ('style', )


class HatSerializer(serializers.HyperlinkedModelSerializer):
    """Hat serializer."""

    brand_name = serializers.SerializerMethodField()

    class Meta:
        model = Hat
        fields = '__all__'

    def get_brand_name(self, obj):
        if obj.brand is not None:
            return obj.brand.name
