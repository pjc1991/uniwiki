from django.urls import path, include
from rest_framework import routers
from .views import UniverseViewSet, WikiDocsViewSet

router = routers.SimpleRouter()
router.register(r'wiki/universes', UniverseViewSet)
router.register(r'wiki/wikidocs', WikiDocsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
