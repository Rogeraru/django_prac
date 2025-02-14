from django.urls import path
from . import views

#define a list of url petterns
urlpatterns = [
    path('', views.index)
]