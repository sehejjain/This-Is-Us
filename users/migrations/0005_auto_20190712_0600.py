# Generated by Django 2.2.2 on 2019-07-12 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190712_0500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orgprofile',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='img',
            new_name='image',
        ),
    ]
