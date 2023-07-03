from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .views import UniverseViewSet, WikiDocsViewSet

router = routers.DefaultRouter()
router.register(r'universe', UniverseViewSet)
router.register(r'wikidoc', WikiDocsViewSet)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'universe': reverse('universe-list', request=request, format=format),
        'wikidoc': reverse('wikidoc-list', request=request, format=format),
    })


urlpatterns = [
    path('', include(router.urls)),
    path('', api_root, name='wiki-api-root'),
]
