#render que se usa para renderizar(mostrar) plantillas de html
from django.shortcuts import render

# Create your views here.

#Importar la clase HttpResponse , que Django usa para enviar respuestas simples al navegador
from django.http import HttpResponse

#Definimos una función llamada home. que será tu vista
#En Django, cada vista es una función (o clase) que recibe un parametro llamado request

#Es un objeto que representa la solicitud del navegador
#Contiene información como: La URL que se pidió, los datos de un formulario, 
# el usuario que hace la petición, metodos
#HTTP GET, POST
def home(request):
    #Aqui crear una respuesta HTTP con un texto "Hola Mundo"
    #Django empaqueta ese texto dentro de una respuesta completa que el 
    #navegador puede mostrar
    return HttpResponse("Hola Mundo, estudiantes")