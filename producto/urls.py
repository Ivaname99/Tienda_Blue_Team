from django.urls import path
from producto import views

urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('productos/', views.listado_productos, name='productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:id>', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>', views.eliminar_producto, name='eliminar_producto'),
    path('contacto', views.mensaje, name='contactar'),
    path('contacto/mensajes', views.recibidos, name="mensajes_recibidos"),
    path('contacto/eliminar/<int:id>', views.eliminarMensaje, name="eliminar_mensaje"),
    path('acercaDe', views.acercaDe, name="acercaDe")
]