# Generated by Django 4.0.4 on 2022-05-09 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bajadery',
            name='lokalizacja',
        ),
        migrations.AlterField(
            model_name='bajadery',
            name='nazwa',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='bajadery',
            name='ocena',
            field=models.FloatField(),
        ),
    ]
