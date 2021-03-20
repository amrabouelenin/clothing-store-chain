# Generated by Django 3.1.7 on 2021-03-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.PositiveIntegerField(help_text='Please enter the branch id', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=256, verbose_name='Branch Name')),
                ('location', models.CharField(max_length=256, verbose_name='location')),
                ('branch_ip', models.CharField(help_text='Allowed Ip Address of the branch', max_length=120, verbose_name='Branch server ip')),
            ],
        ),
    ]
