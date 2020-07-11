from django.urls import path,re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry.html", views.entry),
    path("favourite",views.user_favourite_add),
    path("index.html",views.index),
    path("about",views.about),
    path("message",views.message),
    path("testwriter",views.test_writer),
    path("text",views.index),
    path("text_list",views.text_list),
]
