# Prog3: Escriba un programa que pida primero un número par y luego un número impar (positivos o
# negativos). En caso de que uno o los dos valores no sea correcto, se mostrará un único aviso.

par = int(input('escribe un numero par: '))
impar = int(input('escribe un numero impar: '))

if (par % 2 != 0) or (impar % 2 == 0):
    print("Has introducido un numero incorrectamente")
