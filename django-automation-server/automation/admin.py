from django.contrib import admin
from .models import MqttBroker


@admin.register(MqttBroker)
class MqttServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'host')
