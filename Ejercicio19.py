#Ejercicio 19: Dados 10 valores, informar el mayor.

numingresados = []

print("Por favor, ingrese diez números: \n")

for x in range(10):
    num = int(input())
    numingresados.append(num)
    
valor_max= max(numingresados)
print('El valor máximo es: ', valor_max)