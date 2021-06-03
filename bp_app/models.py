from django.db import models

# Create your models here.

# User
class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=25)
    profile_pic = models.CharField(max_length=500)
    # This method will return each User's first name when viewing a User object in the python shell in terminal:
    def __str__(self):
        return self.first_name

# Note
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_text = models.CharField(max_length=400)

    def __str__(self):
        return self.note_text

# Image
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img_src = models.CharField(max_length=500)

    def __str__(self):
        return self.img_src

# Card
class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    card_img = models.CharField(max_length=500)
    card_text = models.CharField(max_length=400)
    # Change this to models.BooleanField?:
    public = models.CharField(max_length=20)

    def __str__(self):
        return self.title
