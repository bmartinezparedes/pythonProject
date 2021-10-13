l=[1,2,3,4,5,6,7,8,9,10,112,113]
l2=[1,"Dous",3+4j,2.34,[1,2,3]]


print(l[2])

print(l2[1])

print(l[-2]) #Con este empezaria desde atras el array

print(l2[-1][2]) #coge el ultimo elemento de la primera coleccion y el tercero de la segunda

print(l2[1][1]) #aqui lo mismo, considera el texto como otra coleccion

l[2]=15

print(l[2])

l3=l[1:4] # la ultima posicion a coger no se coge, solo asta la anterior
print(l3)
print(l[1:-1:2]) # el uno donde empieza, el segundo donde acaba, el tercero que coja de cada 2
print(l[1::2])

l4=list()
l5=[]
l4.append(0)
l5.append(1)

t=1,2,"tres",[4,5,2+4j]
print(t)
t2=2
print(t2)
print(t[3])
t[3]
print(t)

for elemento in t:
    print(elemento)

l.append(113)
l.extend((114,115,116,117))
l.insert(10, 112)
print(l.pop(15))
print(l.index(113))
print(l)
print("numero veces que que aparece 113 co metodo count:" + str(l.count(113)))
print(len(l))

lista=["Ola","0000la","Hola","Hi"]

def ordea(x):
    return len (x)

lista.sort(key=ordea)

#diccionario

d={
    1: "uno",
    2: "Dous",
    3:"tres",
    "Manuel":"123456789"
}

print(d[1])
print(d["Manuel"])

print(d.items()) #clave valor
print(d.keys()) #clave
print(d.values()) #valor
print(d.get("Manuela", "clave no encontrada")) #ni no encuentra la clave salta el segundo mensaje

def saudar (lingua):

    def saudar_es():
        print("hola")

    def saudar_en():
        print("hi")

    def saudar_gl():
        print("ola")

    def saudar_fr():
        print("salut")

    funcion_saudar={
        "es":saudar_es,
        "en":saudar_en,
        "gl": saudar_gl,
        "fr": saudar_fr
    }
    return funcion_saudar[lingua]
#a f le doy la funcion con el idioma dado
f = saudar("es")
#ejecuto esa fu ncion que trae un print
f()

saudar("gl")()

#Funcion Lambda

def suma (x,y):
    return x+y

s=lambda x,y:x+y

print(suma(2,3))
print(s(3,2))

l =[1,2,3,4,5]

def cadrado (n):
    return n**2
l2=map(lambda n:n**2,l)
for n in l2:
    print(n)
#composicion de listas

l2=[n**2 for n in l]
l3= [n for n in l if n % 2 ==0]

print(l3)

#Xeradores

l5=(n**2 for n in l)
print(l5)

def meuXerador(n,m,s):
    while (n<=m):
        yield n
        n+=s
xerador=meuXerador(7,15,2)
print(xerador)

for n in xerador:
    print(n)

#for (int i=7, n<=m, i+=s) esto en java

for i in range(7,16,2): #esto igual a lalinea 134
    print(i)

r=range(7,16,2)
print(type(r))


#cadeas de caracteres

cadeas= "Python para todos"
print(cadeas[3])
print(cadeas[1:18:2])

print(cadeas.count("o"))
print(len(cadeas))
print(cadeas.find("o",5,14))

cadea2=cadeas.join(("Hola ","a ","todos ", " no ", "presente ", "curso "))
print(cadea2)

print(cadeas.split(" "))
print(cadeas.replace(' ',"_"))
