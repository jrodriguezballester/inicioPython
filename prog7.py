# Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene
# que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el
# programa tiene que escribir la lista.


from typing import List
lista_palabras: List[str] = []

# introduccion de datos
num1 = int(input("introduce el numero de palabras: "))

# recorrer introduciondo una palabra y guardandola en un list
for _ in range(0, num1):
    palabra = input('introduce una palabra: ')
    lista_palabras.append(palabra)

# mostrar resultado
# recorre la lista
for item in lista_palabras:  # similar a for each
    print(item)
