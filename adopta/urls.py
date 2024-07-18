from django.urls import path
from .views import index 
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('inscribe/', views.inscribe, name='inscribe'),
    path('sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('adopta/', views.adopta, name='adopta'),
    path('registro/', views.registro, name='registro'),
]