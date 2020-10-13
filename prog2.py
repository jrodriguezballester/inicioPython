# Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona
# y que calcule su índice de masa corporal (imc).
# Se recuerda que el imc se calcula con la fórmula imc = peso / altura^2

peso = float(input("introduce tu peso en kg"))
altura = int(input('introduce tu altura en cm'))

# pow (a,b) tambien se puede poner a**b es a elevado a b
imc = peso / pow(altura, 2)
print(f"el indice de masa corporal {imc}")