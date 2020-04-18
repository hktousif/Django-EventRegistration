from .views import *
from django.urls import path


urlpatterns = [
    path('', home_view, name="home"),
    path('aboutibmr', about_view, name="aboutibmr"),
    path('events', events_view, name="events"),
    path('gallery', gallery_view, name="gallery"),
    path('support', support_view, name="support"),
    path('register', register_view, name="register"),
    path('protocols', protocols_view, name="protocols"),
]