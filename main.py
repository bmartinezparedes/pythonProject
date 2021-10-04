# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Quiero, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('dormir')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Comentarios")
#Comentario de liña

'''
Comentario 
multi liña javaDoc
'''
"""
comentario
multi liña y javaDoc
"""

numero= 5
comaFlotante= 24.42
comaFlotante=2e-15
complexos= 7+2j
print(type(complexos))
#O tipo de cadeas e 'srt'
#para castear al tipo fuera y lo que dentro
cadeas=str(complexos)
print(cadeas)

cadea1="un tipo de 'cadea'"
cadea2='outro tipo de "cadea"'

print(cadea1+", "+cadea2)
print(type(comaFlotante))
print(comaFlotante)

#operadores
div=5.5/2
divEntero=5.5//2
modulo=5.5%2
print(div)
print(divEntero)
print(modulo)

#operacion a nivel bit &|^~
resultado = 3 & 2
print(resultado)
resultado = 3 | 2
print(resultado)
resultado = 3 ^ 2
print(resultado)
resultado = ~1
print(resultado)
resultado = 1>>1
print(resultado)
resultado = 1<<1
print(resultado)
resultado = -(2**2-1)
print(resultado)