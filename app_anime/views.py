from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bson.objectid import ObjectId
from .models import Personaje, EscuadronGremio, Mision
from mi_proyecto.mongo import obtener_db_mongo


# ==========================================
# 🔐 AUTENTICACIÓN (GUARDADA EN POSTGRESQL)
# ==========================================

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('home')
        messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()

    return render(request, 'app_anime/login.html', {'form': form})


def registrar_usuario(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el usuario en PostgreSQL
            messages.success(request, '¡Cuenta creada con éxito! Ahora inicia sesión.')
            return redirect('login')
        messages.error(request, 'Revisa los requisitos de usuario y contraseña.')
    else:
        form = UserCreationForm()

    return render(request, 'app_anime/registro.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('login')


# ==========================================
# 🎌 TUS VISTAS PRINCIPALES (POSTGRESQL)
# ==========================================

@login_required
def home(request):
    return render(request, 'app_anime/home.html')


@login_required
def personajes(request):
    personajes_list = Personaje.objects.all()
    escuadrones_list = EscuadronGremio.objects.all()
    context = {
        'personajes': personajes_list,
        'escuadrones': escuadrones_list,
    }
    return render(request, 'app_anime/personajes.html', context)


@login_required
def videos(request):
    return render(request, 'app_anime/videos.html')


@login_required
def musica(request):
    return render(request, 'app_anime/musica.html')


@login_required
def misiones(request):
    misiones_list = Mision.objects.all()
    return render(request, 'app_anime/misiones.html', {'misiones': misiones_list})


# ==========================================
# 🍃 MÓDULO DINÁMICO (GUARDADO EN MONGODB)
# ==========================================

@login_required
def coleccion_mongo(request):
    db = obtener_db_mongo()
    mongo_activo = False
    animes = []

    if db is not None:
        try:
            if request.method == 'POST':
                titulo = request.POST.get('titulo', '').strip()
                genero = request.POST.get('genero', '').strip()
                estado = request.POST.get('estado', 'Viendo')
                puntuacion = request.POST.get('puntuacion', '5')

                if titulo:
                    db.animes.insert_one({
                        'usuario': request.user.username,
                        'titulo': titulo,
                        'genero': genero,
                        'estado': estado,
                        'puntuacion': puntuacion,
                    })
                return redirect('coleccion_mongo')

            registros = list(db.animes.find({'usuario': request.user.username}))
            for item in registros:
                item['id'] = str(item['_id'])
            animes = registros
            mongo_activo = True
        except Exception:
            mongo_activo = False

    return render(request, 'app_anime/panel.html', {
    'animes': animes,
    'mongo_activo': mongo_activo,
    })


@login_required
def eliminar_anime(request, anime_id):
    db = obtener_db_mongo()
    if db is not None:
        try:
            db.animes.delete_one({
                '_id': ObjectId(anime_id),
                'usuario': request.user.username
            })
        except Exception:
            pass
    return redirect('coleccion_mongo')