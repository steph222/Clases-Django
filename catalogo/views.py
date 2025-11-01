from django.shortcuts import render, redirect
#Para mostrar plantillas de mensajes temporales
from django.contrib import messages
from .models import Autor, Libro
from .forms import AutorForm,LibroForm


# ------------- Autores----------------
def autor_list(request):
    #Vista que muestra la lista completa de los autores registrados
    
    #Recuperar todos los objetos del modelo Autor 
    #(SELECT * FROM Autores)
    autores = Autor.objects.all()
    #[{},{}]
    return render(request,'catalogo/autor_list.html',{'autores':autores})

#Crear Autores

def autor_create(request):
    #Si el formulario fue enviado (metodo post)
    if request.method == 'POST':
        #Creamos una instancia de AutorForm con los datos enviados por el usuario
        form=AutorForm(request.POST)
        
        #Verificamos si los datos son válidos segun las reglas del formulario
        if form.is_valid():
            #Guardar el nuevo autor en la db
            form.save()
            #Mostrar un mensaje de éxito
            messages.success(request,'Autor creado correctamente')
            #Redirigimos a la vista de autores
            return redirect('autor_list')
        else:
            #Mostramos un mensaje de error
            messages.error(request,'ERROR, Revisa los datos del formulario')
    else:
        #Si el usuario solo abrio la página, mostramos el formulario vacio
        form=AutorForm()
    
    #Rederizado de la plantilla 
    return render(request,'catalogo/autor_form.html',{'form':form})


# ----------LIBRO
def libro_list(request):
    #select_related('autor')
    #prefetch_related('generos')
    libros= Libro.objects.select_related('autor').prefetch_related('generos').all()
    
    #Renderizado
    return render(request, 'catalogo/libro_list.html',{'libros':libros})