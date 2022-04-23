from django.urls import path
from .views import PlayMusic


urlpatterns = [
        path('background/',
             PlayMusic.as_view(),
             name='get_url'),
        ]
