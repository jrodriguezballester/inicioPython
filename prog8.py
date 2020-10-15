# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una
# palabra y diga cuántas veces aparece esa palabra en la lista.


from typing import List
lista_palabras: List[str] = []
contador = 0
palabra=''

# introduccion de datos
while palabra != "0":
    palabra = input('introduce una palabra (introduce 0 para finalizar): ')
    lista_palabras.append(palabra)

palabra_buscada = input('introduce una palabra a buscar: ')

# consulta de datos

for item in lista_palabras:  # similar a for each
    if item == palabra_buscada:
        contador +=1


# mostrar resultado

print(f'la palabra {palabra_buscada}, se repite {contador} veces')
