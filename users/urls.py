from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("<str:username>/", views.Profile.as_view(), name="detail"), 
]


