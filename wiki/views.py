# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from wiki.models import Universe, WikiDocument
from .serializers import UniverseSerializer, WikiDocumentSerializer


# Standard Views


# --- API Views ---

class UniverseViewSet(viewsets.ModelViewSet):
    queryset = Universe.objects.all()
    serializer_class = UniverseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Universe.objects.filter(allowed_users=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, allowed_users=[self.request.user])


class WikiDocumentViewSet(viewsets.ModelViewSet):
    queryset = WikiDocument.objects.all()
    serializer_class = WikiDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return WikiDocument.objects.filter(universe__allowed_users=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Latest(APIView):

    def get_queryset(self):
        user = self.request.user
        return WikiDocument.objects.filter(universe__allowed_users=user)

    # return the latest wiki document
    def get(self, request, format=None):
        wiki_document = WikiDocument.objects.latest('modified_at')
        serializer = WikiDocumentSerializer(wiki_document)
        return Response(serializer.data)
