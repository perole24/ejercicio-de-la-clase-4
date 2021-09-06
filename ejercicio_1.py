"""=> Ejercicio 1:
    Realiza una función separar(lista) que tome una lista de números enteros 
    y devuelva dos listas la primera con los números pares 
    y la segunda con los números impares.

    Ej:
        pares, impares = separar([6,5,2,1,7])
        print(pares)
        print(impares)

        >>> [2, 6]
        >>> [1, 5, 7]"""
        

numeros = [0,1,2,3,4,5,6,7,8,9,10]

def separar(lista_num: list[int]):
    """funcion separar los numeros de la lista en numeros pares y en inpares."""
    numeros_pares = list(filter(lambda x: x % 2 == 0 and x != 0, lista_num))
    numeros_impares = list(filter(lambda x: x % 2 != 0 or x == 0, lista_num))
    return numeros_impares, numeros_pares

numeros_inpares, numeros_pares = separar(numeros)

print(numeros_pares)
print(numeros_inpares)
