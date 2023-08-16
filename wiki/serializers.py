from rest_framework import serializers

from common.models import UniUser as User
from wiki.models import Universe, WikiDocument


class WikiDocumentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    universe = serializers.HyperlinkedRelatedField(view_name='wiki:universe-detail', read_only=True)

    class Meta:
        model = WikiDocument
        fields = [
            'id',
            'universe',
            'name',
            'description',
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
    detail = serializers.HyperlinkedIdentityField(view_name='wiki:universe-detail', read_only=True)

    class Meta:
        model = Universe
        fields = [
            'id',
            'name',
            'detail',
            'description',
            'created_at',
            'modified_at',
            'owner',
            'allowed_users',
        ]
