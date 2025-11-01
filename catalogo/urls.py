from django.urls import path
from . import views

urlpatterns=[
    #Autor
    path('autores/',views.autor_list,name='autor_list'),
    path('autores/nuevo/',views.autor_create, name='autor_create'),
    #Libros
    path('libros/', views.libro_list,name='libro_list'),
]