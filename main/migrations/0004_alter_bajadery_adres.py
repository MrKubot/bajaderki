# Generated by Django 4.0.4 on 2022-05-09 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_bajadery_adres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bajadery',
            name='adres',
            field=models.URLField(blank=True, default='-'),
        ),
    ]
