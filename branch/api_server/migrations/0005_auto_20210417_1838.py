# Generated by Django 3.1.7 on 2021-04-17 16:38

from django.db import migrations
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0004_auto_20210417_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicescall',
            name='actual_date',
            field=unixtimestampfield.fields.UnixTimeStampField(),
        ),
        migrations.AlterField(
            model_name='servicescall',
            name='expected_date',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True),
        ),
    ]
