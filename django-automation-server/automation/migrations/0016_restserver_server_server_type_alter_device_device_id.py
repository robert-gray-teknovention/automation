# Generated by Django 4.2.6 on 2023-11-27 06:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0015_alter_dataitem_data_group_alter_device_device_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestServer',
            fields=[
                ('server_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.server')),
                ('protocol', models.CharField(choices=[('HTTP', 'http'), ('HTTPS', 'https')], default='HTTP')),
                ('host', models.CharField(max_length=100)),
                ('port', models.IntegerField(default=80)),
                ('path', models.CharField(default='/mqtt', max_length=25)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            bases=('automation.server',),
        ),
        migrations.AddField(
            model_name='server',
            name='server_type',
            field=models.CharField(choices=[('MQTT', 'mqtt'), ('REST', 'rest')], default='MQTT'),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.UUIDField(default=uuid.UUID('3512e1f4-d3eb-4aa0-8e9f-5dab87935cca'), unique=True),
        ),
    ]
