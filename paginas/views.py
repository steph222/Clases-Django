from django.shortcuts import render

from django.views import View

# Create your views here.

#Vistas basadas en funciones
def saludo(request):
    
    contexto = {
        'titulo':'Inicio',
        'usuario':'Steph',
        'cursos':['Django','React','Python'],
        'usuario_activo':True,
    }
    #Renderiza el template y envía contexto
    return render(request,'paginas/saludo.html',contexto)

def informacion(request):
    contexto = {
        'titulo':'Información',
        'descripcion':'Este sitio va a demostrar el uso de una página usando FBV + Template de Djando'
    }
    return render(request, 'paginas/info.html',contexto)


#Vistas basadas en clases

class ProductosView(View):
    def get(self, request):
        productos = [
            {'nombre':'Laptop Lenovo','precio':450000, 'disponible':False},
            {'nombre':'Mouse Logitech','precio':15000, 'disponible':True},
            {'nombre':'Teclado Redragon','precio':25000, 'disponible':False}
        ]
        contexto={
            'titulo':'Lista de Productos',
            'productos':productos,
        }
        return render(request,'paginas/productos.html',contexto)
    
class ContactosView(View):
    def get(self, request):
        contexto={
            'titulo': 'Contactenos',
            'direccion':'Avenida Central, San José, Costa Rica',
            'telefono': '+506 8888-8558',
            'email': 'contacto@mitienda.com'
        }
        return render(request,'paginas/contacto.html',contexto)