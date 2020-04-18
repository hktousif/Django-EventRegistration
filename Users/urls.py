from .views import *
from django.urls import path
urlpatterns = [
    path('/', signup_view, name='signup'),
    path('/logout', logout_view, name="logout"),
    path('/profile', profile_view, name="profile"),
    path('/login', login_view, name="login"),
]