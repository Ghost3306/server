# Generated by Django 5.0 on 2024-01-30 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_height_products_length_products_width'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('productname', models.CharField(max_length=255)),
                ('productid', models.IntegerField()),
                ('reviewerid', models.CharField(max_length=255)),
                ('reviwername', models.CharField(max_length=255)),
                ('review', models.TextField()),
                ('start', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
