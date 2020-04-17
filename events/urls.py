from .views import *
from django.urls import path


urlpatterns = [
    path('', home_view),
    path('aboutibmr', about_view),
    path('events', events_view),
    path('gallery', gallery_view),
    path('support', support_view),
    path('register', register_view),
    path('protocols', protocols_view),
]