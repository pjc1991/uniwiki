from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
]
