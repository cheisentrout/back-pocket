from django.contrib import admin
from .models import AppUser
from .models import Note
from .models import Image
from .models import Card

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Note)
admin.site.register(Image)
admin.site.register(Card)
