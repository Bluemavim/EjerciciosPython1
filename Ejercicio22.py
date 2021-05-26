#Ejercicio 35: Desarrollar un procedimiento que imprima una fecha en formato DD/MM/AA. 
#El dato que recibe es un longint con una fecha en formato aaaammdd.


from datetime import datetime
a = int(input("Ingrese la fecha con el formato: AAAAMMDD:  \n"))
date = datetime.strptime(str(a), '%Y%m%d').strftime('%m/%d/%Y')
print("La fecha ingresada es: ", date, " .")