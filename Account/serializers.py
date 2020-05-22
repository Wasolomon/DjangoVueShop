from rest_framework import serializers

from .models import User, Right, Role, Menu, Category


class UserSerializers(serializers.HyperlinkedModelSerializer):
    # roleName = serializers.CharField(source='role_name.roleName')

    class Meta:
        model = User
        fields = ('url', 'password', 'id', 'username', 'mg_state', 'type', 'role_name', 'email', 'mobile')
        depth = 3


class RightSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Right
        fields = ('id', 'url', 'authName', 'level', 'path', 'pid', 'children')
        depth = 3

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['children']:
            data['children'] = ''
        return data


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'url', 'roleName', 'roleDesc', 'children')
        depth = 3


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'authName', 'path', 'children')
        depth = 3


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        depth = 3


class CategoryLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('level', 'name', 'id', 'deleted')
