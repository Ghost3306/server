# Generated by Django 5.0 on 2024-01-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
