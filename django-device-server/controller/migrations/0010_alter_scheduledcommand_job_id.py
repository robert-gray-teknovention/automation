# Generated by Django 4.2.9 on 2024-02-15 04:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0009_alter_scheduledcommand_function_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledcommand',
            name='job_id',
            field=models.CharField(default=uuid.UUID('4be2649d-7e60-4422-b96f-a82a2d328752'), max_length=40),
        ),
    ]
