#Ejercicio 20: Dados N valores informar el mayor, el menor y en que posición del conjunto fueron ingresados.

numingresados = []

num = int(input('Por favor, ingrese números. Escriba 0 para finalizar la carga.'))
numingresados.append(num)

#Se ingresan los números a la lista
while num != 0:
    num = int(input())
    if num != 0:
        numingresados.append(num)
    else:
        print("Finalizó la carga. Desplegando resultados : ")
    

print("El valor máximo es: ", max(numingresados), ".")
print("Su número de posición es : ", numingresados.index(max(numingresados)) + 1)
print("El valor mínimo es: ", min(numingresados), ".")
print("Su número de posición es : ", numingresados.index(min(numingresados))+ 1 )