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


class ScalingMixin(models.Model):
    raw_lo = models.FloatField(default=0.0)
    raw_hi = models.FloatField(default=100.0)
    scale_lo = models.FloatField(default=0.0)
    scale_hi = models.FloatField(default=100.0)
    scaling_on = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def get_value(self, raw_value):
        if self.scaling_on:
            raw_range = self.raw_hi - self.raw_lo
            scale_range = self.scale_hi - self.scale_lo
            return scale_range/raw_range * (raw_value - self.raw_lo) + self.scale_lo
        else:
            return raw_value


class LoggingMixin(models.Model):
    logging_on = models.BooleanField(default=False)

    class Meta:
        abstract = True


class AnalogLoggingMixin(LoggingMixin):
    logging_deadband = models.FloatField(default=1.0, null=True)

    class Meta:
        abstract = True


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


class StringDataItem(LoggingMixin, DataItem):
    alarm_string = models.CharField(max_length=100)


class DiscreteDataItem(LoggingMixin, DataItem):
    class AlarmState(models.TextChoices):
        TRUE = 'TRUE', 'true'
        FALSE = 'FALSE', 'false'
        NONE = 'NONE', 'none'


class IntegerDataItem(ScalingMixin, LoggingMixin, DataItem):
    pass


class RealDataItem(ScalingMixin, AnalogLoggingMixin, DataItem):
    decimal_places = models.IntegerField(default=2)


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
    value_raw = models.FloatField(null=True)
    value = models.FloatField(null=True)
