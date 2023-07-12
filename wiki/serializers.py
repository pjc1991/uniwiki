from django.contrib.auth.models import User
from rest_framework import serializers

from wiki.models import Universe, WikiDocument


class WikiDocsSerializer(serializers.ModelSerializer):
    universe_name = serializers.CharField(source='universe.name', read_only=True)
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = WikiDocument
        fields = [
            'id',
            'name',
            'description',
            'universe_name',
            'owner',
            'version',
            'related_documents',
            'document_type',
            'created_at',
            'modified_at',
            'is_published',
            'is_deleted',
        ]


class UniverseSerializer(serializers.ModelSerializer):
    wiki_document = WikiDocsSerializer(many=True, read_only=True)

    class Meta:
        model = Universe
        fields = [
            'id',
            'name',
            'description',
            'created_at',
            'modified_at',
            'owner',
            'allowed_users',
            'wiki_document',
        ]
