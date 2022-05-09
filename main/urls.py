
from django.urls import path, include
from . import views

urlpatterns = [
    path('dodaj/', views.dodaj, name='dodaj'),
    path('ranking/', views.ranking, name='ranking'),
    path('', views.home, name='home'),

]








