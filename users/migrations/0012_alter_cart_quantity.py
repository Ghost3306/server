# Generated by Django 5.0 on 2024-02-03 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_cart_useruid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.CharField(max_length=255),
        ),
    ]
