from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from common.serializers import UserSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # only allow users to see their own user object

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


