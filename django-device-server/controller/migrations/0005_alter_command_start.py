# Generated by Django 4.2.9 on 2024-02-05 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0004_command_end_command_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='start',
            field=models.DateTimeField(null=True),
        ),
    ]