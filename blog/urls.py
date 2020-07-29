
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry.html", views.entry),
    path("favourite", views.user_favourite_add),
    path("index.html", views.index),
    path("about", views.about),
    path("message", views.message),
    path("testwriter", views.test_writer),
    path("texttosql",views.new_text_get_text),
    path("text_list", views.text_list),
    path("sign_in",views.sign_in_page),
    path("sign_up",views.sign_up_page)
]
