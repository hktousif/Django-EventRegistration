from .views import *
from django.urls import path
urlpatterns = [
    path('/', signup_view),
    path('/logout', logout_view),
    path('/profile', profile_view),
    path('/login', login_view),
]