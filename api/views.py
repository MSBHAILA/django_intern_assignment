from rest_framework import generics
from .models import Client, Artist, Work
from rest_framework.filters import SearchFilter
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ClientSerializer, ArtistSerializer, WorkSerializer, UserSerializer


class ClientCreate(generics.CreateAPIView):
    serializer_class = ClientSerializer
    # queryset = Client.objects.all()


class WorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
    queryset = Work.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('work_type',)


class ArtistList(generics.ListCreateAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
