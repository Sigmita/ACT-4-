# app_Netflix/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Pelicula # Asegúrate de importar Pelicula

# ... (tus funciones de Usuario existentes) ...

# Página de inicio (ya existente)
def inicio_netflix(request):
    return render(request, 'inicio.html')

# Vista para mostrar todos los usuarios (ya existente)
def ver_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/ver_usuarios.html', {'usuarios': usuarios})

# Vista para agregar un nuevo usuario (ya existente)
def agregar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        tipo_membresia = request.POST['tipo_membresia']
        pais = request.POST['pais']
        Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            tipo_membresia=tipo_membresia,
            pais=pais
        )
        return redirect('ver_usuarios')
    return render(request, 'usuario/agregar_usuario.html')

# Vista para actualizar un usuario (mostrar formulario) (ya existente)
def actualizar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    return render(request, 'usuario/actualizar_usuario.html', {'usuario': usuario})

# Vista para realizar la actualización del usuario (ya existente)
def realizar_actualizacion_usuario(request, id_usuario):
    if request.method == 'POST':
        usuario = get_object_or_404(Usuario, pk=id_usuario)
        usuario.nombre = request.POST['nombre']
        usuario.apellido = request.POST['apellido']
        usuario.email = request.POST['email']
        usuario.tipo_membresia = request.POST['tipo_membresia']
        usuario.pais = request.POST['pais']
        usuario.save()
        return redirect('ver_usuarios')
    return redirect('ver_usuarios') # Redirecciona si no es POST

# Vista para borrar un usuario (ya existente)
def borrar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('ver_usuarios')
    return render(request, 'usuario/borrar_usuario.html', {'usuario': usuario})


# ==========================================
# FUNCIONES PARA EL MODELO: PELICULA
# ==========================================

# Vista para mostrar todas las películas
def ver_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'pelicula/ver_peliculas.html', {'peliculas': peliculas})

# Vista para agregar una nueva película
def agregar_pelicula(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        ano_lanzamiento = request.POST['ano_lanzamiento']
        genero = request.POST['genero']
        clasificacion_edad = request.POST['clasificacion_edad']
        duracion_minutos = request.POST['duracion_minutos']
        director = request.POST['director']
        idioma_original = request.POST['idioma_original']
        
        Pelicula.objects.create(
            titulo=titulo,
            ano_lanzamiento=ano_lanzamiento,
            genero=genero,
            clasificacion_edad=clasificacion_edad,
            duracion_minutos=duracion_minutos,
            director=director,
            idioma_original=idioma_original
        )
        return redirect('ver_peliculas')
    return render(request, 'pelicula/agregar_pelicula.html')

# Vista para actualizar una película (mostrar formulario)
def actualizar_pelicula(request, id_pelicula):
    pelicula = get_object_or_404(Pelicula, pk=id_pelicula)
    return render(request, 'pelicula/actualizar_pelicula.html', {'pelicula': pelicula})

# Vista para realizar la actualización de la película
def realizar_actualizacion_pelicula(request, id_pelicula):
    if request.method == 'POST':
        pelicula = get_object_or_404(Pelicula, pk=id_pelicula)
        pelicula.titulo = request.POST['titulo']
        pelicula.ano_lanzamiento = request.POST['ano_lanzamiento']
        pelicula.genero = request.POST['genero']
        pelicula.clasificacion_edad = request.POST['clasificacion_edad']
        pelicula.duracion_minutos = request.POST['duracion_minutos']
        pelicula.director = request.POST['director']
        pelicula.idioma_original = request.POST['idioma_original']
        pelicula.save()
        return redirect('ver_peliculas')
    return redirect('ver_peliculas') # Redirecciona si no es POST

# Vista para borrar una película
def borrar_pelicula(request, id_pelicula):
    pelicula = get_object_or_404(Pelicula, pk=id_pelicula)
    if request.method == 'POST':
        pelicula.delete()
        return redirect('ver_peliculas')
    return render(request, 'pelicula/borrar_pelicula.html', {'pelicula': pelicula})