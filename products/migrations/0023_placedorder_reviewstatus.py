# Generated by Django 5.0 on 2024-02-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_remove_review_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='placedorder',
            name='reviewstatus',
            field=models.CharField(default='notdone', max_length=15),
        ),
    ]
