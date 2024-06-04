
#Ejercicios básicos de Python. Clase 1 y 2 en Iron Hack: FOR

"""Calcular el número de vocales en la frase "El perro corre despacio" """

#Incluye Diagrama de flujo en ReadMe 

frase = "El perro corre despacio"
vocales = "aeiouAEIOU"

contador = 0
for caracter in frase:
    if caracter in vocales:
        contador += 1

print(f"El número de vocales en la frase es: {contador}")



# Explicación paso a paso:

"""Primero definimos una funcion, en este caso llamada eratostenes que toma el parametro n.
- Luego creaos una lista de booleanos para representar los números primos 
- inicializamos los elementos de la lista en 0 y 1 porque no son numeros primos 
- luego tachamos los multiplos de cada primo
- mostramos los primos encontrados 
""" 