# Generated by Django 3.1.7 on 2021-04-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210417_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=1, max_length=150, verbose_name='price in USD'),
        ),
    ]
