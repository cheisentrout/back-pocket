from django.shortcuts import render
from rest_framework import generics

# SERIALIZERS
from .serializers import UserSerializer
from .serializers import NoteSerializer
from .serializers import ImageSerializer
from .serializers import CardSerializer

# MODELS
from .models import User
from .models import Note
from .models import Image
from .models import Card

# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by('id')
    serializer_class = NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all().order_by('id')
    serializer_class = NoteSerializer

class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all().order_by('id')
    serializer_class = ImageSerializer

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all().order_by('id')
    serializer_class = ImageSerializer

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all().order_by('id')
    serializer_class = CardSerializer

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all().order_by('id')
    serializer_class = CardSerializer
