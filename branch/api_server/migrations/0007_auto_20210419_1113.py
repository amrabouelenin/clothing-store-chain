# Generated by Django 3.1.7 on 2021-04-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0006_auto_20210419_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicescall',
            name='loss',
            field=models.IntegerField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicescall',
            name='revenue',
            field=models.IntegerField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]