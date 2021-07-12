from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_post),
    path('post/create/', views.create_post),
    path('post/create/submit/', views.create_post_submit),
    path('post/update/<int:post_id>', views.update_post),
    path('post/update/submit/', views.update_post_submit),
]
