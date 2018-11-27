from django.urls import path
from .views import Home


app_name = 'youtube_links'


urlpatterns = [
    path('', Home.as_view(), name = 'home'),
]