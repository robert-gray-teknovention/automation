# Generated by Django 4.2.9 on 2024-02-15 04:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0010_alter_scheduledcommand_job_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledcommand',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='scheduledcommand',
            name='job_id',
            field=models.CharField(default=uuid.UUID('d30889ba-2c95-47e8-ab9a-3e6f1a1f8802'), max_length=40),
        ),
    ]