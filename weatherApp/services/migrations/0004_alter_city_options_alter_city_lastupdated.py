# Generated by Django 4.0.6 on 2022-07-28 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_city_lastupdated_city_weather'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'citie'},
        ),
        migrations.AlterField(
            model_name='city',
            name='lastUpdated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]