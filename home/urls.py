from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<str:slug>", views.single_article, name="single_article"),
    path("add/", views.add_article, name="add_article"),
    path("blog/name/", views.name, name="name"),
    path("blog/your-name", views.get_name, name="get_name"),
    path("add/validate", views.validate_add_article, name="validate_add_article"),
    path("search", views.search, name="search"),
]
