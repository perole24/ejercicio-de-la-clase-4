"""=> Ejercicio 4:
    Realizar una fn mostrar, que reciba una lista de frutas y un numero, e imprima 
    un numero y el elemento asociado. 

    Ej: 

      frutas = ['Banana', 'kiwi', 'Pera', 'Naranja', 'Manzana']

      mostrar(frutas, 100)

      >>> 100 Banana
      >>> 101 kiwi
      >>> 102 Pera
      >>> 103 Naranja
      >>> 104 Manzana"""
      
      
mis_frutas = ['Banana', 'kiwi', 'Pera', 'Naranja', 'Manzana']

# for frutas in mis_frutas:
#     print(frutas)
    
def mostrar(lista,acu):
  for indice, elemento in enumerate(lista,acu):
    print(indice, "=>", elemento)
    
mostrar(mis_frutas,100)