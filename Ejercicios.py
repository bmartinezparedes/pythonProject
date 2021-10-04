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


# 1 corregir recorriendo la lista
def encaja1(lista1, lista2):
    if lista1[1] == lista2[0] or lista1[1] == lista2[1]:
        return "encaja"
    else:
        return "no encaja"


print(encaja1(l, l2))

# 2
l3 = "3-4"
l4 = "2-5"


def encaja2(ls1, ls2):
    lista1 = ls1.split()
    lista2 = ls2.split()

    if lista1 == lista2[0] or lista1[1] == lista2[1]:
        return "encaja"
    else:
        return "no encaja"


print(encaja2(l3, l4))

# 7.3
