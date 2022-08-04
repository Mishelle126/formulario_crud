from django.urls import path
from .views import login, create_nombre
urlpatterns =  [
    path('', login),
    path('new_nombre/', create_nombre, name='create_nombre'),
]