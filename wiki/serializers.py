from rest_framework import serializers

from common.models import UniUser as User
from wiki.models import Universe, WikiDocument


class WikiDocumentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=serializers.CurrentUserDefault()
    )
    document_type = serializers.ChoiceField(
        choices=WikiDocument.DocumentType.choices, default=WikiDocument.DocumentType.UNKNOWN
    )

    universe = serializers.PrimaryKeyRelatedField(
        queryset=Universe.objects.all(), default=serializers.CurrentUserDefault()
    )

    description = serializers.CharField(
        allow_blank=True, trim_whitespace=False
    )

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

    # override create method
    def create(self, validated_data):
        # if universe is not specified, find the latest universe he is allowed to access
        # if the user don't have any universe, create a new one
        if 'universe' not in self.context['request'].data:
            # find the latest universe he is allowed to access
            universe = Universe.objects.filter(allowed_users=self.context['request'].user).last()
            if universe is None:
                # create a new universe
                universe = Universe.objects.create(name="New Universe", owner=self.context['request'].user)
                universe.allowed_users.add(self.context['request'].user)
            validated_data['universe'] = universe

        # check if user is allowed to create a document in this universe
        if self.context['request'].user not in validated_data['universe'].allowed_users.all():
            raise serializers.ValidationError("You are not allowed to create a document in this universe.")

        # check if there is more than one document with the same name in this universe, if so, delete except the latest one
        if WikiDocument.objects.filter(name=validated_data['name'], universe=validated_data['universe']).count() > 1:
            # find the latest document
            document = WikiDocument.objects.filter(name=validated_data['name'], universe=validated_data['universe']).last()
            # delete other documents
            WikiDocument.objects.filter(name=validated_data['name'], universe=validated_data['universe']).exclude(id=document.id).delete()
            # update the latest document, only update description
            document.description = validated_data['description']
            return document

        # check if there is a document with the same name in this universe
        if WikiDocument.objects.filter(name=validated_data['name'], universe=validated_data['universe']).exists():
            # instead of create a new document, update the existing one, only update description
            document = WikiDocument.objects.get(name=validated_data['name'], universe=validated_data['universe'])
            document.description = validated_data['description']
            document.save()
            return document

        # super create
        return super().create(validated_data)

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
