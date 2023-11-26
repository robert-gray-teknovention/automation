from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from .views import (
    UserViewSet,
    )

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

]
