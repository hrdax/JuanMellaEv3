from django.shortcuts import render, redirect
from django.contrib import messages
from jpev3.lista import *
from jpev3.models import *
# Create your views here.  
     
#vista que confirma la compra y descuenta el stock        
def success(request):
    if request.method == "POST":
        codproducto = request.POST['codproducto']
        stock = request.POST['cantidad']
        ret = validacod(codproducto)
        ret.stock = ret.stock - int(stock)
        return render(request, 'jpev3/compraconfirmada.html')

#da el detalle de la compra con el total
def detalletotal(request):
    if request.method == "POST":
        codproducto = request.POST['codproducto']
        stock = request.POST['cantidad']
        retcod = validacod(codproducto)
        ret = validastock(codproducto,stock)
        if ret == False:
            total = retcod.precio * int(stock)
            return render(request, 'jpev3/confirmartotal.html', {"cantidad":stock, "codproducto":retcod, "total":total})
        if ret == True:
            return render(request, 'jpev3/venderproducto.html', {"listaproducto":productos, "message":"Error en el ingreso de cantidad"})


#vista que muestra el detalle del producto
def verproducto(request):
    codproducto = request.GET['codproducto']
    ret = validacod(codproducto)
    return render(request, 'jpev3/detalles.html',{"retcodigo":ret})
    
#vistas basicas
def menu(request):
    return render(request, 'jpev3/index.html')

def ver_productos(request):
    return render(request, 'jpev3/verproductos.html', {"listaproducto":productos})

def vender_productos(request):
    return render(request, 'jpev3/venderproducto.html', {"listaproducto":productos})

def detalle_productos(request):
    return render(request, 'jpev3/detalles.html', {"producto":productos})