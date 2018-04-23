teststring = "this is tu vieja"

lista = teststring.split(" ")
cuenta = len(lista)

def reverso():
    global lista,cuenta
    contador = 0
    indice = -1
    while contador < cuenta:
        print(lista[indice])
        contador = contador +1
        indice = indice -1
    return

reverso()
