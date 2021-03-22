# Generated by Django 3.1.7 on 2021-03-20 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0002_dailyrevenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRevenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.PositiveIntegerField(default=1616242898, verbose_name='Datetime Unix')),
                ('revenu', models.FloatField(max_length=150, verbose_name='Revenus in Dollar$')),
                ('loses', models.FloatField(max_length=150, verbose_name='Amount of losses in Dollar$')),
                ('Branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_server.branch')),
            ],
        ),
        migrations.DeleteModel(
            name='DailyRevenu',
        ),
    ]