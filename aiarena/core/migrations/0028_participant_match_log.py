# Generated by Django 2.1.7 on 2019-07-14 01:23

import aiarena.core.models
import aiarena.core.storage
from django.db import migrations
import private_storage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20190710_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='match_log',
            field=private_storage.fields.PrivateFileField(blank=True, null=True, storage=aiarena.core.storage.OverwritePrivateStorage(base_url='/'), upload_to=aiarena.core.models.match_log_upload_to),
        ),
    ]