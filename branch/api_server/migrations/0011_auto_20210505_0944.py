# Generated by Django 3.1.7 on 2021-05-05 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0010_auto_20210505_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicescall',
            name='actual_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
