from django.urls import path
from . import views

urlpatterns = [
    path('pocket/users', views.UserList.as_view(), name='user_list'),
    path('pocket/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('pocket/notes', views.NoteList.as_view(), name='note_list'),
    path('pocket/notes/<int:pk>', views.NoteDetail.as_view(), name='note_detail'),
    path('pocket/images', views.ImageList.as_view(), name='image_list'),
    path('pocket/images/<int:pk>', views.ImageDetail.as_view(), name='image_detail'),
    path('pocket/cards', views.CardList.as_view(), name='card_list'),
    path('pocket/cards/<int:pk>', views.CardDetail.as_view(), name='card_detail')
]
