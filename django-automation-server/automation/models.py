from django.db import models
import uuid


class Server(models.Model):
    class ServerTypes(models.TextChoices):
        MQTT = 'MQTT', 'mqtt'
        REST = 'REST', 'rest'
    name = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField()
    server_type = models.CharField(choices=ServerTypes.choices, default=ServerTypes.MQTT)

    def __str__(self):
        return self.name


class RestServer(Server):
    class HostProtocols(models.TextChoices):
        HTTP = 'HTTP', 'http'
        HTTPS = 'HTTPS', 'https'
    protocol = models.CharField(choices=HostProtocols.choices, default=HostProtocols.HTTP)
    host = models.CharField(max_length=100)
    port = models.IntegerField(default=80)
    path = models.CharField(max_length=25, default='/apis')
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)


class MqttBroker(Server):
    class HostProtocols(models.TextChoices):
        MQTT = 'MQTT', 'mqtt'
        MQTTS = 'MQTTS', 'mqtts'
        WS = 'WS', 'ws'
        WSS = 'WSS', 'ws'
    protocol = models.CharField(choices=HostProtocols.choices, default=HostProtocols.MQTTS)
    host = models.CharField(max_length=100)
    port = models.IntegerField(default=8883)
    path = models.CharField(max_length=25, default='/mqtt')
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    ssl = models.BooleanField(default=True)


class Topic(models.Model):
    name = models.CharField(max_length=50)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DeviceType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=50)
    device_id = models.UUIDField(unique=True, default=uuid.uuid4())
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class DataGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DataItem(models.Model):
    class Type(models.TextChoices):
        STRING = 'STRING', 'string'
        DISCRETE = 'DISCRETE', 'discrete'
        INT = 'INT', 'integer'
        REAL = 'REAL', 'real'
    name = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    data_group = models.ManyToManyField(DataGroup, blank=True)
    data_type = models.CharField(max_length=10, choices=Type.choices)
    alarm_enable = models.BooleanField(default=False)
    alarm_status = models.BooleanField(default=False)
    device = models.ForeignKey(Device, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class StringDataItem(DataItem):
    alarm_string = models.CharField(max_length=100)


class DiscreteDataItem(DataItem):
    class AlarmState(models.TextChoices):
        TRUE = 'TRUE', 'true'
        FALSE = 'FALSE', 'false'
        NONE = 'NONE', 'none'


class IntegerDataItem(DataItem):
    scaling_on = models.BooleanField()
    lo_scale = models.IntegerField(default=0)
    hi_scale = models.IntegerField(default=100)


class RealDataItem(DataItem):
    scaling_on = models.BooleanField()
    lo_scale = models.FloatField(default=0.0)
    hi_scale = models.FloatField(default=100.0)
    decimal_places = models.IntegerField(default=2)
    logging_on = models.BooleanField(default=False)
    logging_deadband = models.FloatField(default=1.0)


class DataEntry(models.Model):
    data_item = models.ForeignKey(DataItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)


class StringDataEntry(DataEntry):
    value = models.CharField(max_length=1024)


class DiscreteDataEntry(DataEntry):
    value = models.BooleanField(default=False)


class IntegerDataEntry(DataEntry):
    value_raw = models.IntegerField(null=True)
    value = models.IntegerField(null=True)


class RealDataEntry(DataEntry):
    value = models.FloatField()
