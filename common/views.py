
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from common.models import UniUser
from common.serializers import UserSerializer


# Create your views here.


# --- API views ---
@permission_classes([IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    queryset = UniUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return UniUser.objects.filter(pk=user.pk)
