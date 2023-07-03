from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from common import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'group', views.GroupViewSet)

app_name = 'common'


@api_view(['GET'])
def api_root(request, fmt=None):
    return Response({
        'user': reverse('user-list', request=request, format=fmt),
    })


urlpatterns = [
    path('', include(router.urls)),
    path('', api_root, name='common-api-root'),
]
