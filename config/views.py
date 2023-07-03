from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, fmt=None):
    return Response({
        'admin': reverse('admin:index', request=request, format=fmt),
        'common': reverse('common-api-root', request=request, format=fmt),
        'wiki': reverse('wiki-api-root', request=request, format=fmt),
        'login': reverse('rest_framework:login', request=request, format=fmt),
        'logout': reverse('rest_framework:logout', request=request, format=fmt),
    })
