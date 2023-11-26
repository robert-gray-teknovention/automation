from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField()


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


class Device(models.Model):
    name = models.CharField(max_length=50)
    device_id = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class DeviceType(models.Model):
    name = models.CharField(max_length=50)
    devices = models.ManyToManyField(Device)

    def __str__(self):
        return self.name


class DataGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DataItem(models.Model):
    name = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, null=True, on_delete=models.NULL)
    data_group = models.ManyToManyField(DataGroup)
    data_type =
    def __str__(self):
        return self.name


class DataEntry(models.Model):
    name = models.CharField(max_length=50)
