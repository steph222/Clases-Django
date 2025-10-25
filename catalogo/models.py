# Importamos el módulo 'models' de Django,
# que contiene todas las clases base necesarias para definir modelos de base de datos.
from django.db import models   


# ==========================
# MODELO: AUTOR
# ==========================
class Autor(models.Model):
    # Campo 'nombre': un texto corto de hasta 100 caracteres.
    # CharField se usa para cadenas de texto pequeñas.
    nombre = models.CharField(max_length=100)

    # Campo 'pais': almacena el país del autor, opcional (blank=True permite dejarlo vacío).
    pais = models.CharField(max_length=60, blank=True)

    # Método especial que define cómo se mostrará el objeto Autor como texto.
    # Se usa, por ejemplo, en el panel de administración y en el shell.
    def __str__(self):
        return self.nombre



# ==========================
# MODELO: GÉNERO
# ==========================
class Genero(models.Model):
    # Campo 'nombre': texto corto y único (unique=True evita duplicados en la base de datos).
    nombre = models.CharField(max_length=50, unique=True)

    # Representación en texto del objeto Género.
    def __str__(self):
        return self.nombre



# ==========================
# MODELO: LIBRO
# ==========================
class Libro(models.Model):
    # Campo 'titulo': texto de hasta 120 caracteres.
    # db_index=True crea un índice en la base de datos para acelerar búsquedas por este campo.
    titulo = models.CharField(max_length=120, db_index=True)

    # Campo 'autor': relación de muchos a uno (ForeignKey) con el modelo Autor.
    # Cada libro tiene un autor, y si se elimina el autor, se eliminan sus libros (on_delete=models.CASCADE).
    # 'related_name' permite acceder desde Autor a sus libros con 'autor.libros.all()'.
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')

    # Campo 'generos': relación de muchos a muchos (ManyToManyField) con el modelo Género.
    # Un libro puede tener varios géneros y un género puede pertenecer a varios libros.
    # 'blank=True' permite dejar la lista vacía.
    # 'related_name' permite acceder desde Género a los libros con 'genero.libros.all()'.
    generos = models.ManyToManyField(Genero, related_name='libros', blank=True)

    # Campo 'fecha_publicacion': almacena la fecha en que se publicó el libro.
    # 'null=True' permite que el valor sea NULL en la base de datos.
    # 'blank=True' permite que el campo se deje vacío en formularios.
    fecha_publicacion = models.DateField(null=True, blank=True)

    # Campo 'precio': almacena un número decimal con hasta 7 dígitos en total
    # (incluyendo 2 decimales). Por ejemplo, 12345.67
    # 'default=0' establece el valor por defecto si no se especifica.
    precio = models.DecimalField(max_digits=7, decimal_places=2, default=0)


    # ==========================
    # CLASE INTERNA Meta
    # ==========================
    class Meta:
        # Define el orden por defecto cuando se consultan los libros (orden alfabético por título).
        ordering = ['titulo']

        # Nombre plural que se mostrará en el panel de administración ("Libros" en lugar de "Libroses").
        verbose_name_plural = 'Libros'


    # Representación del objeto Libro como texto legible.
    # Muestra el título seguido del autor entre paréntesis, por ejemplo:
    # "Cien años de soledad (Gabriel García Márquez)"
    def __str__(self):
        return f"{self.titulo} ({self.autor})"
