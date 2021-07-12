from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create-post/', views.create),
    path('create-post/submit/', views.create_submit),
]
