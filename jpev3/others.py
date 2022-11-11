#funcion que valida si es un int o no
def es_int(n):
    try:
        int(n)
    except ValueError:
        return True
    else:
        return False