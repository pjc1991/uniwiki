from rest_framework import serializers

from wiki.models import Universe


class UniverseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Universe
        fields = ['id', 'name', 'description']


class WikiDocsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Universe
        fields = ['id', 'name', 'description']
