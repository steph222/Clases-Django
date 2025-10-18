from django.urls import path
from . import views

urlpatterns=[
    path('saludo/',views.saludo, name='saludo'),
    path('info/',views.informacion, name='info'),
    path('productos/', views.ProductosView.as_view(), name='productos'),
    path('contacto/',views.ContactosView.as_view(), name='contacto'),
]