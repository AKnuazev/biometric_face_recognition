from rest_framework import serializers
from django.db import transaction
from .models import *


class BfrUserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = BfrUser
        fields = (
            'id', BfrUser.USERNAME_FIELD, 'email', 'name', 'surname', 'otchestvo', 'telephone',
            'full_name', 'password', 'is_staff', 'is_superuser', 'is_admin', 'is_active'
        )
        read_only_fields = ('is_superuser',)
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
        login = validated_data.pop('login')
        user = BfrUserSerializer.objects.create_user(login, password=password, **validated_data)
        return user
