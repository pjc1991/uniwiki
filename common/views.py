from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from common.serializers import UserSerializer, GroupSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    # only allow users to see their own user object

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Group.objects.all()
        else:
            return user.groups.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
