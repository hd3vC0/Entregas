# Generated by Django 3.0.6 on 2020-06-01 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200601_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiendacategoria',
            name='banner',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='tiendacategoria',
            name='icono',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
