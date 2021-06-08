from rest_framework import serializers
# DJANGO BUILT IN USER OBJECT:
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import AppUser
from .models import Note
from .models import Image
from .models import Card

# turn this into a function I can call when the user is being created?
# Ran this once and it generated tokens for all existing users, bless it's heart:
# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        # Following line makes it so that someone can't send a GET request to the users api and see the hashed password, and that creating a new User object requires a password
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

        # def create(self, validated_data):
        #     user = User.objects.create_user(**validated_data)
        #     Token.objects.create(user=user)
        #     return user

        #Right now I think the Django User object is expecting some other information from this function - either an email field, a different type of password, or something. I'm getting an error.
        def create(self, validated_data):
            print (User)
            user = User(
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            Token.objects.get_or_create(user=user)
            user.save()
            return user

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'profile_pic')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'user', 'note_text')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'user', 'img_src')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'user', 'title', 'card_text', 'card_img', 'public')
