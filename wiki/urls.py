from django.urls import path, include
from rest_framework import routers
from .views import UniverseViewSet, WikiDocsViewSet

router = routers.DefaultRouter()
router.register(r'universes', UniverseViewSet)
router.register(r'wikidocs', WikiDocsViewSet)
