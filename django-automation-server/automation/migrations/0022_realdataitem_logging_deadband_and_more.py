# Generated by Django 4.2.6 on 2023-11-28 06:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0021_alter_device_device_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='realdataitem',
            name='logging_deadband',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='realdataitem',
            name='logging_on',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.UUIDField(default=uuid.UUID('9f6925e2-1328-4fd2-90d1-bda86e3e7fda'), unique=True),
        ),
    ]
