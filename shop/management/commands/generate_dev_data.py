"""Generate dev data."""

from django.core.management.base import BaseCommand

from shop.models import Footwear, Hat, Style
from shop.tests import BrandFactory, FootwearFactory, HatFactory, StyleFactory


class Command(BaseCommand):
    """Generate dev data."""

    def handle(self, *args, **options):  # noqa: D102
        """Generate dev data."""
        fab_frida = BrandFactory(
            name='Fabulous Frida',
            description="Fabulous Frida is a fashion forward futurist with a focus on fetching "
                        "fezs, fedoras and fascinators.",
        )
        decadent_fran = BrandFactory(
            name='Decadent Fran',
            description="Shoes, boots and hats to evoke the fall of Rome. Gilt, fur and rare "
                        "leathers abound."
        )
        fancy_dan = BrandFactory(
            name='Fancy Dan',
            description="A range of flamboyant shoes and boots for every occasion.",
        )
        janky_stan = BrandFactory(
            name='Janky Stan',
            description="Quality footwear at low low prices.",
        )

        for name, _ in Style.STYLES:
            StyleFactory(name=name)

        HatFactory(brand=fab_frida, style=StyleFactory(name=Style.FEDORA))
        HatFactory(brand=fab_frida, style=StyleFactory(name=Style.FEZ))
        HatFactory(brand=decadent_fran, style=StyleFactory(name=Style.TOP_HAT))
        HatFactory(brand=decadent_fran, style=StyleFactory(name=Style.FEZ))
        HatFactory(brand=decadent_fran, style=StyleFactory(name=Style.PANAMA))

        FootwearFactory(brand=decadent_fran, style=StyleFactory(name=Style.BALMORAL))
        FootwearFactory(brand=fancy_dan, style=StyleFactory(name=Style.BALMORAL))
        FootwearFactory(brand=fancy_dan, style=StyleFactory(name=Style.MONK))
        FootwearFactory(brand=fancy_dan, style=StyleFactory(name=Style.OXFORD))
        FootwearFactory(brand=janky_stan, style=StyleFactory(name=Style.DERBY))
        FootwearFactory(brand=janky_stan, style=StyleFactory(name=Style.BROGUE))
