# Generated by Django 4.2.9 on 2024-02-08 04:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0006_command_asyncro_scheduledcommand'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledcommand',
            name='run_once',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='scheduledcommand',
            name='job_id',
            field=models.CharField(default=uuid.UUID('692d9f9e-94b2-4f33-89b2-845ba2e397f2'), max_length=20),
        ),
    ]