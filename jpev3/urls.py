from django.urls import path
from . import views

#urls de la app jpev3
urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('verproducto/', views.ver_productos, name='verproducto'),
    path('venderproducto/', views.vender_productos, name='venderproducto'),
    path('detalleproducto/', views.verproducto, name='detalle'),
    path('confirmarcompra/', views.success, name='confirmarcompra'),
    path('confirmartotal/', views.detalletotal, name='confirmartotal'),
]