"""Member benefit factories."""

import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice
from moneyed import Money
import random

from shop.models import (
    Brand,
    Footwear,
    Hat,
    Style
)


class StyleFactory(DjangoModelFactory):
    """Factory for styles."""

    name = FuzzyChoice(
        (style[0] for style in Style.STYLES)
    )

    class Meta:
        model = Style
        django_get_or_create = ('name',)


class BrandFactory(DjangoModelFactory):
    """Factory for brands."""

    name = factory.Faker('company')

    class Meta:
        model = Brand


class FootwearFactory(DjangoModelFactory):
    """Factory for hats."""

    style = factory.SubFactory(StyleFactory)
    brand = factory.SubFactory(BrandFactory)

    class Meta:
        model = Footwear

    @factory.lazy_attribute
    def price(self):
        """Generate a random price between 0 and 400."""
        return Money(random.randint(0, 400), 'GBP')


class HatFactory(DjangoModelFactory):
    """Factory for hats."""

    style = factory.SubFactory(StyleFactory)
    brand = factory.SubFactory(BrandFactory)

    class Meta:
        model = Hat

    @factory.lazy_attribute
    def price(self):
        """Generate a random price between 0 and 400."""
        return Money(random.randint(0, 400), 'GBP')
