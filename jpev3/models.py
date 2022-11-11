from django.db import models
from django.contrib import messages
from jpev3.lista import *
from jpev3.others import *
# Create your models here.

#encuentra el producto
def validacod(codigoi):
    for producto in productos:
        if producto.codigo == int(codigoi):
            return producto

#valida si hay stock
def validastock(codproducto,stock):
    encontro = validacod(codproducto)
    if es_int(stock) == False:
        if int(stock) <= 0:
            return True
        elif int(stock) <= encontro.stock and encontro.stock >= int(stock):
            return False
        else:
            return True                
    else:
        return True

