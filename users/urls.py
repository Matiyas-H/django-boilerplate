from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("edit-profile/", views.EditProfile.as_view(), name="edit_profile"),
    path("<str:username>/", views.Profile.as_view(), name="detail"), 
   
]

