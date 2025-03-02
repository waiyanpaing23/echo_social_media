from django.urls import path
from . import views
from post import views as post_views

app_name = 'core'

urlpatterns = [
    path('', post_views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout_user, name='logout')
]