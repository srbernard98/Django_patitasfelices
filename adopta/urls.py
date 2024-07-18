from django.urls import path
from .views import index 
from . import views
from django.urls import path
from .views import UsuarioListView, UsuarioDetailView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView

urlpatterns = [
    path('', index, name='index'),
    path('inscribe/', views.inscribe, name='inscribe'),
    path('sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('adopta/', views.adopta, name='adopta'),
    path('registro/', views.registro, name='registro'),


    path('usuario_list', UsuarioListView.as_view(), name='usuario_list'),
    path('usuario/<int:pk>/', UsuarioDetailView.as_view(), name='usuario_detail'),
    path('usuario/nuevo/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuario/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuario/<int:pk>/eliminar/', UsuarioDeleteView.as_view(), name='usuario_delete'),
]