# Generated by Django 3.0.8 on 2020-10-18 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0118_auto_20201012_0339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='patreon_level',
            new_name='supporter_level',
        ),
    ]
