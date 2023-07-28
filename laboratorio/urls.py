
from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertar_lab, name='insertar_lab'),
    path('mostrar/', views.mostrar_lab, name='mostrar_lab'),
    path('editar/<int:pk>', views.editar_lab, name='editar_lab'),
    path('eliminar/<int:pk>', views.eliminar_lab, name='eliminar_lab'),
    
]
