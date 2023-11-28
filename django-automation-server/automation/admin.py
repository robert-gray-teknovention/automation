from django.contrib import admin
from .models import (
    MqttBroker,
    RestServer,
    Device,
    DeviceType,
    RealDataItem,
    Topic,
    )


@admin.register(MqttBroker)
class MqttServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'server_type')


@admin.register(RestServer)
class RestServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'server_type')


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'device_id')


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(RealDataItem)
class RealDataItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'data_type', 'device', 'topic')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'server')
