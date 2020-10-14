# Escriba un programa que pida un número entero mayor que cero y que escriba sus
# divisores.
# ○ Un número es divisible por otro cuando el resto de su división es cero (numero % divisor == 0).
# ○ Se puede hacer un programa más rápido, teniendo en cuenta que los divisores son siempre menores o iguales que la
# mitad del número (salvo el propio número, que es divisor de sí mismo). Es decir,no hace falta probar todos
# los números entre 1 y el propio número, sino únicamente hasta la mitad. Si se hace así,
# no hay que olvidarse de añadir el propio número a la lista de divisores.


import sys

# introduccion de la variable
num1 = int(input("introduce un numero: "))
divisores = 0
# Control de la variable
if num1 <= 0:
    sys.exit()

# a) recorriendo todos los numeros
for i in range(1, num1 + 1):
    if num1 % i == 0:
        print(i, "es divisor de ", num1)

print('---------')

# b) recorriendo hasta la mitad del numero
for i in range(1, int(num1 / 2 + 1)):
    if num1 % i == 0:
        divisores += 1
        print(i, "es divisor de ", num1)

print(num1, "es divisor de ", num1)
print('---------')

# añadido si es primo
if divisores <= 1:
    print('Es un numero primo')
else:
    print('no es un numero primo')
