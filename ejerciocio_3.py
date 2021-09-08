#IMPORTACION DE MODULO
from functools import reduce

numeros = [4, 5, 22]

def suma(a,b):
    return a+b

funcion = reduce(suma,numeros, 100)

print(funcion)