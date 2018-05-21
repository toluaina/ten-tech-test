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
)


class BrandFactory(DjangoModelFactory):
    """Factory for brands."""

    name = factory.Faker('company')

    class Meta:
        model = Brand


class FootwearFactory(DjangoModelFactory):
    """Factory for hats."""

    style = FuzzyChoice(
        (footwear_style[0] for footwear_style in Footwear.STYLES)
    )
    brand = factory.SubFactory(BrandFactory)

    class Meta:
        model = Footwear

    @factory.lazy_attribute
    def price(self):
        """Generate a random price between 0 and 400."""
        return Money(random.randint(0, 400), 'GBP')


class HatFactory(DjangoModelFactory):
    """Factory for hats."""

    style = FuzzyChoice(
        (hat_style[0] for hat_style in Hat.STYLES)
    )
    brand = factory.SubFactory(BrandFactory)

    class Meta:
        model = Hat

    @factory.lazy_attribute
    def price(self):
        """Generate a random price between 0 and 400."""
        return Money(random.randint(0, 400), 'GBP')
