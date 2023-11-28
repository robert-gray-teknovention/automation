from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from .views import (
    UserViewSet,
    DataItemViewSet,
    RealDataItemViewSet,
    RealDataEntryViewSet,
    TopicViewSet,
    DeviceViewSet,
    DeviceTypeViewSet,
    ServerViewSet,
    RestServerViewSet,
    MqttBrokerViewSet
    )

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'data_items', DataItemViewSet)
router.register(r'real_data_items', RealDataItemViewSet)
router.register(r'real_data_entries', RealDataEntryViewSet)
router.register(r'mqtt_brokers', MqttBrokerViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'device_types', DeviceTypeViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'servers', ServerViewSet)
router.register(r'rest_servers', RestServerViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

]
