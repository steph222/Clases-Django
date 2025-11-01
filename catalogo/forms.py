from django import forms 
#Nos permite crear formularios 
#Importar los modelos que usaremos para crear formularios
from .models import Autor, Libro, Genero


#Formulario del Autor
#-------------------------

class AutorForm(forms.ModelForm):
    """
    Formulario basado en el modelo Autor
    Django generará automaticamente los campos a partir del modelo
    """
    
    class Meta:
        #Especificar que modelo se generara el formulario
        model =Autor
        
        #Definir los campos del modelo que se incluiran en el formulario
        fields = ['nombre','pais']
        
        #Etiquetas personalizadas que se van a mostrar en el HTML
        labels={
            'nombre':'Nombre del autor',
            'pais':'País (opcional)',
        }
   
# Formulario Libro
#-----------------------------     

class LibroForm(forms.ModelForm):
    """
    Formulario basado en el modelo Libro
    Incluye relaciones con otros modelos Autor y Género
    """
    
    class Meta:
        #Modelo
        model = Libro
        
        #Campos
        fields=['titulo','autor','generos','fecha_publicacion','precio']
        
        #Personalizar de widgets (tipo de input html)
        widgets = {
            #Para el campo ManyToMany genero, se usa un checkboxes multiples--select
            'generos':forms.CheckboxSelectMultiple,
            #Para la fecha, usara el tipo date
            'fecha_publicacion':forms.DateInput(attrs={'type':'date'})
        }
        #Etiquetas
        labels={
            'titulo':'Título',
            'autor':'Autor',
            'generos': 'Géneros',
            'fecha_publicacion':'Fecha de publicación',
            'precio':'Precio'
        }
        