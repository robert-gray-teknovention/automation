# Generated by Django 4.2.9 on 2024-02-05 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0003_command_executed_alter_command_args'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='command',
            name='start',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
