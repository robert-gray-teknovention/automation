# Generated by Django 4.2.9 on 2024-02-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='args',
            field=models.JSONField(null=True),
        ),
    ]