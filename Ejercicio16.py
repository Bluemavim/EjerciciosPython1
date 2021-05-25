# Variables para contador

catc = 0
catd = 0
cate = 0
catf = 0

print ("Introduzca el sueldo (0 para salir): ")
sueldo = float(input())

while sueldo != 0:
    if sueldo < 2000:
        catc = catc + 1
    elif sueldo < 3000:
        catd = catd + 1
    elif sueldo < 5000:
        cate = cate + 1
    else:
        catf = catf + 1
    sueldo = float(input())

print("**************************************")
print(catc , " empleados ganan menos de $2.000.")
print(catd , " empleados ganan $2.000 o más pero menos de $3.000.")
print(cate , " empleados ganan $3.000 o más pero menos de $5.000.")
print(catf , " empleados ganan $5.000 o más.")
   