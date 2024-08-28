from django.urls import path

from . import views



urlpatterns = [
    path('get_public_key', views.get_public_key)
]