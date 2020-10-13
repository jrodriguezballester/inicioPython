# Escriba un programa que pida primero un número par (positivo o negativo) y si el valor no es
# correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o negativo) y si
# el valor no es correcto, mostrará un aviso.


par = int(input('escribe un numero par: '))
if par % 2 !=0:
    print("Has introducido un numero impar")
else:
    impar = int(input('escribe un numero impar: '))
    if impar % 2 == 0:
        print("Has introducido un numero par")


