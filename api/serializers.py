from rest_framework import serializers
from .models import Client, Artist, Work
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer, validated_data=user_data)
        client = Client.objects.create(user=user, **validated_data)
        return client


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer()

    class Meta:
        model = Artist
        fields = ['id', 'name', 'works']

    def create(self, validated_data):
        works_data = validated_data.pop('works')
        artist = Artist.objects.create(**validated_data)
        work = Work.objects.create(**works_data)

        artist.works.add(work)
        return artist
