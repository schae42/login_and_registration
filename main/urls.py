from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_user', views.process_user),
    path('login_user', views.login_user),
    path('welcome', views.welcome),
    path('logout', views.logout),
]