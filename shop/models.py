from django.db import models
from django.utils.translation import ugettext_lazy as _

from djmoney.models.fields import MoneyField
from collectionfield.models import CollectionField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.


class Style(models.Model):

    # footwear
    OXFORD = 'OXF'
    DERBY = 'DRB'
    BROGUE = 'BRG'
    MONK = 'MNK'
    BALMORAL = 'BML'
    # hat
    FEDORA = 'FED'
    TOP_HAT = 'TOP'
    TRILBY = 'TBY'
    PANAMA = 'PNM'
    FEZ = 'FEZ'
    CAP = 'CAP'

    STYLES = (
        (OXFORD, 'Oxford'),
        (DERBY, 'Derby'),
        (BROGUE, 'Brogue'),
        (MONK, 'Monk'),
        (BALMORAL, 'Balmoral'),
        (FEDORA, 'Fedora'),
        (TOP_HAT, 'Top Hat'),
        (TRILBY, 'Trilby'),
        (PANAMA, 'Panama'),
        (FEZ, 'Fez'),
        (CAP, 'Cap'),
    )

    name = models.CharField(max_length=3, unique=True)

    class Meta:
        verbose_name = 'Style'
        verbose_name_plural = 'Styles'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


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
    style = models.ForeignKey(
        Style, verbose_name=_('style'), related_name='hats', blank=True,
        null=True
    )
    brand = models.ManyToManyField(
        Brand, verbose_name=_('brand'), related_name='hats', blank=True
    )
    price = MoneyField(max_digits=6, decimal_places=2, default_currency='GBP')
    colour = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        verbose_name = 'Hat'
        verbose_name_plural = 'Hats'
        ordering = ('price', )

    def __unicode__(self):
        if not self.brand:
            return '{style_of_hat} at {price}'.format(
                style_of_hat=self.style.name,
                price=self.price,
            )
        return '{style_of_hat} by {brand} at {price}'.format(
            style_of_hat=self.style,
            brand=self.brand.name,
            price=self.price,
        )

    def __str__(self):
        return self.__unicode__()


class Footwear(models.Model):
    style = models.ForeignKey(
        Style, verbose_name=_('style'), related_name='footwear', blank=True,
        null=True
    )
    brand = models.ForeignKey(Brand, verbose_name=_('brand'), related_name='footwear')
    price = MoneyField(max_digits=6, decimal_places=2, default_currency='GBP')

    class Meta:
        verbose_name = 'Footwear'
        verbose_name_plural = 'Footwear'
        ordering = ('price', )

    def __unicode__(self):
        return '{style_of_footwear} by {brand} at {price}'.format(
            style_of_footwear=self.style,
            brand=self.brand.name,
            price=self.price,
        )

    def __str__(self):
        return self.__unicode__()


class Item(models.Model):

    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    limit = models.Q(app_label='shop', model='hat') | models.Q(app_label='shop', model='footwear')
    content_type = models.ForeignKey(
        ContentType, related_name='items', on_delete=models.CASCADE,
        limit_choices_to=limit
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Basket(models.Model):
    owner = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    checkout_date = models.DateTimeField()
    items = GenericRelation(Item)

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Basket'

    def __unicode__(self):
        return 'Basket for {first_name}{last_name} total {total_price}'.format(
            first_name=self.owner.first_name,
            last_name=self.owner.last_name,
            total_price=self.total_price
        )

    @property
    def total_price(self):
        return (
            Item.objects.filter(
                basket_id=self.pk
            ).aggregate(Sum('price'))
        )

    @property
    def hats_price(self):
        content_type = ContentType.objects.get_for_model(Hat)
        return (
            Item.objects.filter(
                basket_id=self.pk,
                content_type=content_type
            ).aggregate(Sum('price'))
        )

    @property
    def footwear_price(self):
        content_type = ContentType.objects.get_for_model(Footwear)
        return (
            Item.objects.filter(
                basket_id=self.pk,
                content_type=content_type
            ).aggregate(Sum('price'))
        )


    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(ban__isnull=True)

