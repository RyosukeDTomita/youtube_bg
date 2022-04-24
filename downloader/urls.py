from django.urls import path
from .views import MusicDl#, play_music


urlpatterns = [
        path('dl/',
             MusicDl.as_view(),
             name='get_url'),
        #path('play/',
        #     play_music,
        #     name='play'),
]
