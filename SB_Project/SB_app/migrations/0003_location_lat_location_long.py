# Generated by Django 5.0.1 on 2024-02-03 16:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SB_app', '0002_remove_city_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='long',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
