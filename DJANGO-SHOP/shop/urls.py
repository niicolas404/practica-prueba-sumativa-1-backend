from django.urls import path

from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.mostrar_catalogo, name='inicio'),
    path('juegos/', views.mostrar_catalogo, name='lista'),
    path('juegos/<int:id>/', views.detalle, name='detalle'),
]