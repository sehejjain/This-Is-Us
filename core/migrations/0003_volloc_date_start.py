# Generated by Django 2.2.2 on 2019-07-06 12:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190706_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='volloc',
            name='date_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
