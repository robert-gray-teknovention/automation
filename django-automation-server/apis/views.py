from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import (
    UserSerializer,
    RealDataItemSerializer,
    DataItemSerializer,
    GetRealDataItemSerializer,
    GetRealDataEntrySerializer,
    RealDataEntrySerializer,
    GetTopicSerializer,
    TopicSerializer,
    DeviceSerializer,
    GetDeviceSerializer,
    GetDeviceTypeSerializer,
    ServerSerializer,
    GetServerSerializer,
    RestServerSerializer,
    GetRestServerSerializer,
    MqttBrokerSerializer,
    GetMqttBrokerSerializer,
    )
from automation.models import (
    DataItem,
    RealDataItem,
    RealDataEntry,
    Topic,
    MqttBroker,
    RestServer,
    Device,
    DeviceType,
    Server,
    )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DataItemViewSet(viewsets.ModelViewSet):
    queryset = DataItem.objects.all()
    serializer_class = DataItemSerializer


class RealDataItemViewSet(viewsets.ModelViewSet):
    queryset = RealDataItem.objects.all()
    serializer_class = GetRealDataItemSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetRealDataItemSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return RealDataItemSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class RealDataEntryViewSet(viewsets.ModelViewSet):
    queryset = RealDataEntry.objects.all()
    serializer_class = GetRealDataEntrySerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetRealDataEntrySerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return RealDataEntrySerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetTopicSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return TopicSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = GetDeviceSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetDeviceSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return DeviceSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class DeviceTypeViewSet(viewsets.ModelViewSet):
    queryset = DeviceType.objects.all()
    serializer_class = GetDeviceTypeSerializer


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = GetServerSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetServerSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return ServerSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class RestServerViewSet(viewsets.ModelViewSet):
    queryset = RestServer.objects.all()
    serializer_class = GetRestServerSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetRestServerSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return RestServerSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class MqttBrokerViewSet(viewsets.ModelViewSet):
    queryset = MqttBroker.objects.all()
    serializer_class = GetMqttBrokerSerializer

    def get_serializer_class(self):
        # Use SerializerForGET for GET requests
        if self.request.method == 'GET':
            return GetMqttBrokerSerializer
        # Use SerializerForPOST for POST requests
        elif self.request.method == 'POST' or self.request.method == 'PUT':
            return MqttBrokerSerializer
        # Use the default serializer for other HTTP methods
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        # Override get_serializer to pass the request context to the serializer
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
