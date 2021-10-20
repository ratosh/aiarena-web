# Generated by Django 3.0.14 on 2021-09-25 11:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20210922_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitionparticipation',
            name='division_num',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
