# practica-prueba-sumativa-1-backend

## Django Shop

Catálogo simple de videojuegos desarrollado con Django. Los datos del catálogo se encuentran en `DJANGO-SHOP/shop/views.py`; no se utiliza una base de datos propia para los videojuegos.

## Requisitos

- Python 3.13 o compatible con las dependencias del proyecto.
- Git.
- PowerShell en Windows o una terminal equivalente.

## Instalación desde GitHub

1. Clona el repositorio y entra en la carpeta del proyecto:

```powershell
git clone URL_DEL_REPOSITORIO
cd practica-prueba-sumativa-1-backend\DJANGO-SHOP
```

2. Crea el entorno virtual:

```powershell
py -m venv .venv
```

3. Activa el entorno virtual en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Cuando esté activo, la terminal mostrará `(.venv)` al inicio. Si PowerShell bloquea el script, permite la ejecución solo para la sesión actual y vuelve a activarlo:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

4. Instala las dependencias:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

5. Comprueba la configuración de Django:

```powershell
python manage.py check
```

6. Inicia el servidor de desarrollo:

```powershell
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` en el navegador.

## Ejecutar sin activar el entorno

También puedes usar directamente el Python del entorno virtual:

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py runserver
```

## Rutas principales

- `/`: inicio y catálogo.
- `/juegos/`: lista de videojuegos.
- `/juegos/<id>/`: detalle de un videojuego.

## Notas

- Cada vez que abras una terminal nueva debes activar `.venv` nuevamente, salvo que ejecutes directamente su `python.exe`.
- `.venv/`, `__pycache__/` y `db.sqlite3` están excluidos mediante `.gitignore`.
- No es necesario crear migraciones propias para el catálogo, porque los videojuegos están definidos como una lista de diccionarios en las vistas.