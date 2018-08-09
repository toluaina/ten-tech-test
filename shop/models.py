from django.db import models
from django.utils.translation import ugettext_lazy as _

from djmoney.models.fields import MoneyField

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class Hat(models.Model):
    FEDORA = 'FED'
    TOP_HAT = 'TOP'
    TRILBY = 'TBY'
    PANAMA = 'PNM'
    FEZ = 'FEZ'
    CAP = 'CAP'
    STYLES = (
        (FEDORA, 'Fedora'),
        (TOP_HAT, 'Top Hat'),
        (TRILBY, 'Trilby'),
        (PANAMA, 'Panama'),
        (FEZ, 'Fez'),
        (CAP, 'Cap')
    )
    style = models.CharField(_('style'), max_length=3, choices=STYLES)
    brands = models.ManyToManyField(Brand, verbose_name=_('brands'), related_name='new_hats')
    price = MoneyField(max_digits=6, decimal_places=2, default_currency='GBP')
    colour = models.TextField(_('colour'), blank=True, default='')

    class Meta:
        verbose_name = 'Hat'
        verbose_name_plural = 'Hats'

    def __unicode__(self):
        return '{style_of_hat} by {brand} at {price}'.format(
            style_of_hat=self.style,
            brand=self.brand.name,
            price=self.price,
        )

    def __str__(self):
        return self.__unicode__()


class Footwear(models.Model):
    brand = models.ForeignKey(Brand, verbose_name=_('brand'), related_name='footwear')
    price = MoneyField(max_digits=6, decimal_places=2, default_currency='GBP')

    class Meta:
        verbose_name = 'Footwear'
        verbose_name_plural = 'Footwear'

    def __unicode__(self):
        return '{style_of_footwear} by {brand} at {price}'.format(
            style_of_footwear=self.style,
            brand=self.brand.name,
            price=self.price,
        )

    def __str__(self):
        return self.__unicode__()


class FootwearStyle(models.Model):
    OXFORD = 'OXF'
    DERBY = 'DRB'
    BROGUE = 'BRG'
    MONK = 'MNK'
    BALMORAL = 'BML'
    STYLES = (
        (OXFORD, 'Oxford'),
        (DERBY, 'Derby'),
        (BROGUE, 'Brogue'),
        (MONK, 'Monk'),
        (BALMORAL, 'Balmoral'),
    )

    footwear = models.ForeignKey(Footwear, verbose_name=_('footwear'), related_name='styles')
    style = models.CharField(_('style'), max_length=3, choices=STYLES)

    def __unicode__(self):
        return '{style_of_footwear}'.format(
            style_of_footwear=self.style,
        )

    def __str__(self):
        return self.__unicode__()
