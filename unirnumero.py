def unirnumero(lista, n):
    if len(lista) == 1:
        return n+lista[0]
    else:
        return unirnumero(lista[1:],(n+lista[0])*(10**contardigitos(lista[1])))

def contardigitos(numero):
    if numero/10 == 0:
        return 1
    else:
        return 1+contardigitos(numero/10)
