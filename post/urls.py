from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
     path('like/<int:post_id>/', views.like, name='like'),
     path('comment/<int:post_id>/', views.comment, name='comment'),
]