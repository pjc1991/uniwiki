from rest_framework import serializers

from wiki.models import Universe, WikiDocument


class WikiDocsSerializer(serializers.HyperlinkedModelSerializer):
    universe = serializers.HyperlinkedRelatedField(view_name='wiki:universe-detail', read_only=True)
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    related_documents = serializers.HyperlinkedRelatedField(view_name='wiki:wikidocs-detail', read_only=True,
                                                            many=True)
    document_type = serializers.CharField(source='get_document_type_display')

    # version should be read-only
    # is_published should be read-only
    class Meta:
        model = WikiDocument
        fields = ['id', 'name', 'description', 'universe', 'owner', 'related_documents', 'document_type', 'version',
                  'created_at', 'modified_at', 'is_published', 'is_deleted']


class WikiDocsCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WikiDocument
        fields = ['id', 'name', 'description', 'universe', 'owner', 'related_documents', 'document_type', 'version',
                  'created_at', 'modified_at', 'is_published', 'is_deleted']

    def create(self, validated_data):
        universe = Universe.objects.get(id=self.context['request'].data['universe'])
        if not universe.allowed_users.filter(id=self.context['request'].user.id).exists():
            raise Exception("You are not allowed to create a document in this universe")
        return WikiDocument.objects.create(**validated_data)


class UniverseSerializer(serializers.HyperlinkedModelSerializer):
    wiki_docs = WikiDocsSerializer(many=True, read_only=True)

    class Meta:
        model = Universe
        fields = ['id', 'name', 'description', 'wiki_docs']
