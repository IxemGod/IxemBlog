from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<str:slug>", views.single_article, name="single_article"),
    path("add/", views.add_article, name="add_article"),
]
