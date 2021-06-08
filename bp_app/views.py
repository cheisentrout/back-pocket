from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# DJANGO BUILT IN USER OBJECT:
from django.contrib.auth.models import User

# SERIALIZERS
from .serializers import UserSerializer
from .serializers import AppUserSerializer
from .serializers import NoteSerializer
from .serializers import ImageSerializer
from .serializers import CardSerializer

# MODELS
from .models import AppUser
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

# USER VIEWS PRIOR TO TRYING DJANGO BUILT IN USER OBJECT - THESE ARE "APPUSER" VIEWS:
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)

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
