from django.urls import path
from .views import login, create_nombre, delete_dato
urlpatterns =  [
    path('', login),
    path('new_nombre/', create_nombre, name='create_nombre'),
    path('delete_dato/<int:Nombre_id>/', delete_dato, name='delete_dato')
]