from django.db import models

# USER - a User can have many notes, images, and cards
class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=25)
    profile_pic = models.CharField(max_length=500)
    # Will I need something here to hold the cards that a user creates?
    # This method will return each User's first name when viewing a User object in the python shell in terminal:
    def __str__(self):
        return self.first_name

# NOTE - each Note can belong to only one User
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_text = models.CharField(max_length=400)

    def __str__(self):
        return self.note_text

# IMAGE - each Image can belong to only one User
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img_src = models.CharField(max_length=500)

    def __str__(self):
        return self.img_src

# CARD - each Card can belong to only one User, unless I'm able to implement the public gallery with the option to "save".
class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=True)
    card_text = models.CharField(max_length=400)
    card_img = models.CharField(max_length=500)
    # Change this to models.BooleanField?:
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title
