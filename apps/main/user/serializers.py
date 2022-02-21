from rest_framework import serializers
from django.db import transaction
from .models import *


class BfrDoorSerializer(serializers.ModelSerializer):
    users_indoor_list = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = BfrDoor
        fields = (
            'code', 'name', 'users_indoor_list'
        )


class BfrUserInfoSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    acl = BfrDoorSerializer(read_only=True, many=True)

    class Meta:
        model = BfrUser
        fields = (
            'id', BfrUser.USERNAME_FIELD, 'full_name', 'telephone', 'email'
            'acl', 'last_indoor', 'indoor_time', 'last_outdoor', 'outdoor_time'
        )
        # read_only_fields = (
        #     'id', BfrUser.USERNAME_FIELD, 'full_name', 'telephone', 'email'
        #     'acl', 'last_indoor', 'indoor_time', 'last_outdoor', 'outdoor_time'
        # )


class BfrUserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    acl = BfrDoorSerializer(read_only=True, many=True)

    class Meta:
        model = BfrUser
        fields = (
            'id', BfrUser.USERNAME_FIELD, 'email', 'name', 'surname', 'otchestvo', 'telephone',
            'full_name', 'password', 'acl', 'is_staff', 'is_superuser', 'is_admin', 'is_active',
            'last_indoor', 'indoor_time', 'last_outdoor', 'outdoor_time'
        )
        read_only_fields = ('is_superuser', 'last_indoor', 'indoor_time', 'last_outdoor', 'outdoor_time')
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    @transaction.atomic
    def update(self, instance, validated_data):
        password = None
        if 'password' in validated_data:
            password = validated_data.pop('password')
        user = super(BfrUserSerializer, self).update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def create(self, validated_data):
        if 'password' not in validated_data:
            raise Exception('Не задан пароль пользователя!')
        password = validated_data.pop('password')
        username = validated_data.pop('username')
        user = BfrUser.objects.create_user(username, password=password, **validated_data)
        return user
