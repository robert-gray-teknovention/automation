# Generated by Django 4.2.6 on 2023-11-16 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MqttServer',
            new_name='MqttBroker',
        ),
    ]