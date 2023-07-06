from django.contrib.auth.models import User
from rest_framework import serializers

from wiki.models import Universe, WikiDocument


class WikiDocsSerializer(serializers.HyperlinkedModelSerializer):
    universe = serializers.HyperlinkedRelatedField(view_name='wiki:universe-detail', queryset=Universe.objects.all())
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())
    related_documents = serializers.HyperlinkedRelatedField(view_name='wiki:wikidocs-detail',
                                                            queryset=WikiDocument.objects.all(), many=True)
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
