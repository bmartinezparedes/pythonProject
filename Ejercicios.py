# 7.1
l = (1, 2, 3, 4)
l2 = (4, 3, 2, 1)


def orden(lista):
    if lista[0] > lista[1]:
        return "De mayor a menor"
    else:
        return "De menor a mayor"


print(orden(l))

# 7.2
l = (3, 4)
l2 = (5, 4)


# 1
def encaja1(lista1, lista2):
    #Uso set() para que me compare las listas, con & consigo que encuentre alguno que coincida entre las dos listas
    if set(lista1) & set(lista2):
        return "encaja"
    else:
        return "no encaja"


print(encaja1(l, l2))

# 2
l3 = "3-4"
l4 = "2-5"


def encaja2(ls1, ls2):
    #con el split(termino con el que separar) lo uso para crear una lista a partir del stream
    lista1 = ls1.split("-")
    lista2 = ls2.split("-")
    if set(lista1) & set(lista2):
        return "encaja"
    else:
        return "no encaja"


print(encaja2(l3, l4))

# 7.3
# 1
lNombres=("Patri","Britza","Hector","Brais","Joel")


def estimadoUsuario(lista):
    for n in lista:
        print("Estimado "+n)

estimadoUsuario(lNombres)
#2
"""def estimadoUsuarioPosicion(lista,posicion,cantidad):
    num=0
    for n in lista[posicion:]:
        while num <cantidad:
           print("Estimado "+n)
            num=num+1

estimadoUsuarioPosicion(lNombres,1,2)"""

# 7.5
listaEnteros=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)

def primos(listaNumeros):
    listaPrimos=[]
    for l in listaNumeros:
        if l < 1:
            return False
        elif l==2:
            listaPrimos.append(l)
        else:
            for n in range(2, l):
                if l % n ==0:
                    return False
            listaPrimos.append(l)
    print(listaPrimos)
primos(listaEnteros)

#8.2
#1

def vecesQueApareceAsPalabras(frase):
    diccionario=dict()
    palabras=frase.split()
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra.lower()]=diccionario[palabra.lower()]+1
        else:
            diccionario[palabra.lower()]=1
    return diccionario

print(vecesQueApareceAsPalabras("Que bonito dia fai hoxe, pese a que chove"))

