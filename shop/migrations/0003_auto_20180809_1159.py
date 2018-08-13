# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 11:59
from __future__ import unicode_literals

from django.db import migrations


def populate_brands(apps, schema_editor):
    Hat = apps.get_model('shop', 'Hat')

    for hat in Hat.objects.all():
        hat.brands.add(hat.brand)


def rollback_brands(apps, schema_editor):
    Hat = apps.get_model('shop', 'Hat')

    for hat in Hat.objects.all():
        hat.brand = hat.brands.first()  # Arbitrarily pick the first brand here
        hat.save()

def populate_footwear_styles(apps, schema_editor):
    Footwear = apps.get_model('shop', 'Footwear')
    FootwearStyle = apps.get_model('shop', 'FootwearStyle')

    for footwear in Footwear.objects.all():
        FootwearStyle.objects.create(style=footwear.style, footwear=footwear)

def rollback_footwear_styles(apps, schema_editor):
    Footwear = apps.get_model('shop', 'Footwear')
    FootwearStyle = apps.get_model('shop', 'FootwearStyle')

    for footwear in Footwear.objects.all():
        # Arbitrarily pick the first footwear here
        footwear.style = FootwearStyle.objects.filter(footwear__id=footwear.id).first().style
        footwear.save()

class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180809_1132'),
    ]

    operations = [
        migrations.RunPython(populate_brands, rollback_brands),
        migrations.RunPython(populate_footwear_styles, rollback_footwear_styles),
    ]