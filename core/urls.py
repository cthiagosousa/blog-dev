from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_post),
    path('post/create/', views.create_post),
    path('post/create/submit/', views.create_post_submit),
    path('post/update/<int:post_id>', views.update_post),
    path('post/update/submit/', views.update_post_submit),
    path('post/delete/<int:post_id>', views.delete_post),
    
    path('user/admin', views.user_administration),
    path('login/', views.login_user),
    path('login/submit/', views.login_user_submit),
    path('logout/', views.logout),
]
