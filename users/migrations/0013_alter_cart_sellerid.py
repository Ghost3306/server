# Generated by Django 5.0 on 2024-02-03 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='sellerid',
            field=models.CharField(max_length=255),
        ),
    ]