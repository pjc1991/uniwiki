from django.contrib.auth.models import User, Group
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='common:group-detail')
    users = serializers.HyperlinkedRelatedField(many=True, view_name='common:user-detail', read_only=True)

    class Meta:
        model = Group
        fields = ['name', 'url', 'users']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='common:user-detail')
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'groups', 'url']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        # create a new user
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
