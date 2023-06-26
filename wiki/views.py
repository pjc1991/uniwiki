# Create your views here.
from rest_framework import viewsets, permissions

from wiki.models import Universe, WikiDocument
from .serializers import UniverseSerializer, WikiDocsSerializer


class UniverseViewSet(viewsets.ModelViewSet):
    # only show the universes that the user has access to
    # many-to-many relationship

    queryset = Universe.objects.all()
    serializer_class = UniverseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Universe.objects.filter(allowed_users=user)


class WikiDocsViewSet(viewsets.ModelViewSet):
    queryset = WikiDocument.objects.all()
    serializer_class = WikiDocsSerializer
    permission_classes = [permissions.IsAuthenticated]
