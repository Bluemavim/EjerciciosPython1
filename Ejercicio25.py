text = input("Por favor, ingrese la oración que quiere analizar aquí:")

#Limpio el texto y lo bajo a minúsculas:

for char in '-.,\n':
    text = text.replace(char,' ')
text = text.lower()

#Cuento la cantidad de palabras. 
cantpalabras =  len(text.split())

#Calculo la palabra más larga.
pal_mas_larga = max(text.split(), key=len)

#Cuento la cantidad de veces que aparecen las vocales.
vocala = text.count("a")
vocale = text.count("e")
vocali = text.count("i")
vocalo = text.count("o")
vocalu = text.count("u")


#Imprimo resultados
print("La cantidad de veces que aparece la letra A es ", vocala, ".")
print("La cantidad de veces que aparece la letra E es ", vocale, ".")
print("La cantidad de veces que aparece la letra I es ", vocali, ".")
print("La cantidad de veces que aparece la letra O es ", vocalo, ".")
print("La cantidad de veces que aparece la letra U es ", vocalu, ".")
print("La cantidad de palabras es: ", cantpalabras, ".")
print("La palabra más larga es: ", pal_mas_larga, ".")