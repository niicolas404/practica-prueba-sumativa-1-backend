from django.http import Http404
from django.shortcuts import render


JUEGOS = [
    {
        'id': 1,
        'titulo': 'The Legend of Zelda: Breath of the Wild',
        'plataforma': 'Nintendo Switch',
        'genero': 'Aventura',
        'anio': 2017,
        'desarrollador': 'Nintendo EPD',
        'precio': 59.99,
        'descripcion': 'Explora Hyrule libremente, resuelve santuarios y descubre los secretos de una tierra llena de aventuras.',
    },
    {
        'id': 2,
        'titulo': 'Forza Horizon 5',
        'plataforma': 'Xbox Series X|S',
        'genero': 'Carreras',
        'anio': 2021,
        'desarrollador': 'Playground Games',
        'precio': 49.99,
        'descripcion': 'Disfruta carreras espectaculares y recorridos por los paisajes variados de Mexico.',
    },
    {
        'id': 3,
        'titulo': 'Hades',
        'plataforma': 'PC',
        'genero': 'Accion',
        'anio': 2020,
        'desarrollador': 'Supergiant Games',
        'precio': 24.99,
        'descripcion': 'Lucha para escapar del inframundo en este roguelike de accion con una historia dinamica.',
    },
]


def mostrar_catalogo(request):
    contexto = {
        'juegos': JUEGOS,
        'total_juegos': len(JUEGOS),
    }
    return render(request, 'home.html', contexto)


def detalle(request, id):
    juego = next((juego for juego in JUEGOS if juego['id'] == id), None)
    if juego is None:
        raise Http404('El videojuego no existe.')
    return render(request, 'categoria.html', {'juego': juego})