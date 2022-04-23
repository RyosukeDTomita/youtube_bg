from django.urls import path
from .views import use_youtube_dl


urlpatterns = [
        path('background/', use_youtube_dl)
        ]
