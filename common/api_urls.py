from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from common import views

router = routers.DefaultRouter()

app_name = 'common'


@api_view(['GET'])
def api_root(request, fmt=None):
    return Response({
    })


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('', api_root, name='common-api-root'),
]
