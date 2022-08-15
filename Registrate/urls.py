from django.urls import path
from .views import login, create_nombre, delete_dato, editar_dato
urlpatterns =  [
    path('', login),
    path('new_nombre/', create_nombre, name='create_nombre'),
    path('delete_dato/<int:Nombre_id>/', delete_dato, name='delete_dato'),
    path('editar_dato/<int:Nombre_id>/', editar_dato, name='editar_dato')
]