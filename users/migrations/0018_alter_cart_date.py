# Generated by Django 5.0 on 2024-02-05 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_cart_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 14, 40, 34, 394667, tzinfo=datetime.timezone.utc)),
        ),
    ]