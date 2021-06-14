from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("joinroom/", views.join_room, name="join_room"),
    path("room_url", views.room_url, name="room_url"),
    path("display_room", views.display_room, name="display_room"),
    path("vote_option", views.vote_option, name="vote_option"),
]
