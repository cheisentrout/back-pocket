from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all().order_by('id')
    serializer_class = CardSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all().order_by('id')
    serializer_class = CardSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

#######################################
# BELOW VIEWS ARE NOT CURRENTLY IN USE:

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
