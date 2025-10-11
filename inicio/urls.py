#Importa la función path() de Django
#Basicamente, path conecta una URL con una vista
from django.urls import path

#El punto . significa "desde  el mismo paquete actual (la app)"
#Importamos la función home que creamos
#Esto es lo que permite que Django sepa que vista va a ejecutar cuando alguien entra a cierta url
from .views import home


#Lista que guarda todas las rutas que pertenecen a la app
#Django revisa la lista cuando intenta resolver que vista mostrar
urlpatterns=[
    #'' --- URL vacía --- representar la raíz del sitio
    #home --Es la vista que se ejecuta
    #name='home' ---Le damos un nombre interno a la ruta
    path('',home, name='home'),
]