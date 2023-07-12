from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers

from wiki.models import Universe, WikiDocument


class WikiDocsSerializer(serializers.HyperlinkedModelSerializer):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    related_documents = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    document_type = serializers.ChoiceField(choices=WikiDocument.DocumentType.choices)

    # version should be read-only
    # is_published should be read-only
    class Meta:
        model = WikiDocument
        fields = ['id', 'name', 'description', 'universe', 'owner', 'related_documents', 'document_type', 'version',
                  'created_at', 'modified_at', 'is_published', 'is_deleted']


class UniverseSerializer(serializers.ModelSerializer):
    wiki_docs = WikiDocsSerializer(many=True, read_only=True)

    class Meta:
        model = Universe
        # all field
        fields = '__all__'
