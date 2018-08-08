from django.contrib import admin

from . import models


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    """Brand admin."""

    list_display = ('name', )


@admin.register(models.Hat)
class HatAdmin(admin.ModelAdmin):
    """Brand admin."""

    list_display = ('style', 'price', )


@admin.register(models.Footwear)
class FootwearAdmin(admin.ModelAdmin):
    """Brand admin."""

    list_display = ('style', 'price', )
