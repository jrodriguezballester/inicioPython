# Escriba un programa que pida dos números enteros y escriba qué números son pares y
# cuáles impares desde el primero hasta el segundo.
# ○ Un número es par cuando el resto de su división entre dos es cero (numero % 2 == 0) e impar cuando no lo es

# Introduccion de Variables

num1 = int(input("introduce un numero: "))
num2 = int(input('introduce un segundo numero: '))


# Control del sentido

if num1 < num2:
    step = 1
    num2 += 1
else:
    step = -1
    num2 -= 1


# Escribir los numeros

for i in range(num1, num2, step):
    if i % 2 == 0:
        print(f'{i} es par ')
    else:
        print(f'{i} es impar')
