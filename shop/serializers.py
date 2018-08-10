from rest_framework import serializers

from shop.models import Brand, Footwear, Hat, FootwearStyle


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    """Brand serializer."""

    class Meta:
        model = Brand
        fields = '__all__'


class FootwearStyleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FootwearStyle
        fields = '__all__'


class FootwearSerializer(serializers.HyperlinkedModelSerializer):
    """Footwear serializer."""

    styles = FootwearStyleSerializer(many=True)
    brand = BrandSerializer()

    class Meta:
        model = Footwear
        fields = '__all__'


class HatSerializer(serializers.HyperlinkedModelSerializer):
    """Hat serializer."""

    class Meta:
        model = Hat
        fields = '__all__'


class HatRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    """Hat serializer for retrival of individual objects."""

    brands = BrandSerializer(many=True)

    class Meta:
        model = Hat
        fields = ('url', 'brands', 'price')


class HatListSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for listing Hat objects."""

    brand_names = serializers.SerializerMethodField()

    class Meta:
        model = Hat
        fields = (
            'url',
            'style',
            'brand_names',
            'price',
            'colour',
        )

    def get_brand_names(self, obj):
        """Resolve to brand names"""
        return [brand.name for brand in obj.brands.all()]
