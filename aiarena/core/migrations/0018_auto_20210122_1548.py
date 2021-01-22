# Generated by Django 3.0.8 on 2021-01-22 05:18

from django.db import migrations

from aiarena.core.models import CompetitionParticipation


def deactivate_participants_of_closed_competitions(apps, schema_editor):
    CompetitionParticipation.objects.filter(competition__status='closed').update(active=False)

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210116_0812'),
    ]

    operations = [
        migrations.RunPython(deactivate_participants_of_closed_competitions),
    ]
