from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
     path('post/', views.create_post, name='create_post'),
     path('like/<int:post_id>/', views.like, name='like'),
     path('comment/<int:post_id>/', views.comment, name='comment'),
]