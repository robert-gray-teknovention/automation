# Generated by Django 4.2.6 on 2023-11-27 05:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0004_alter_device_device_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.UUIDField(default=uuid.UUID('a69bbcac-e11f-48ed-86ac-fedcbe5ddb1e'), unique=True),
        ),
    ]
