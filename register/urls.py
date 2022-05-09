from django.urls import path, include
from . import views


urlpatterns = [
    path('unauth', views.unauth, name='unauth'),
    path('login/', views.login, name='login'),
    path('', views.register, name='register'),
]