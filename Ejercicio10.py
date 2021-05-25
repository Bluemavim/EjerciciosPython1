#Ejercicio número 10: Se ingresa una edad, mostrar por pantalla alguna de las siguientes leyendas: 
# ‘menor’ si la edad es menor o igual a 12
#‘cadete’ si la edad está comprendida entre 13 y 18 
#‘juvenil’ si la edad es mayor que 18 y no supera los 26 
#‘mayor’ en el caso que no cumpla ninguna de las condiciones anteriores


edad = int(input("Por favor, ingrese la edad: \n"))

if edad <= 12:
    print("Pertenece a la categoría MENOR.")
elif edad <= 18:
    print("Pertenece a la categoría CADETE.")
elif edad <= 26:
    print("Pertenece a la categoría JUVENIL")
else:
    print("Pertenece a la categoría MAYOR.")