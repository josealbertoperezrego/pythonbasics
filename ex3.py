
#Ejercicios básicos de Python. Clase 1 y 2 en Iron Hack: Listas

"""Crea una funcion que permita implementar el algoritmo de Eratóstenes. 
La criba de Eratóstenes es un algoritmo que permite hallar todos los números primos
menores que un número natural dado.

Se forma una tabla con todos los números naturales
comprendidos entre 2 y n, y se van tachando los números que no son primos de la siguiente manera:

- Comenzando por el 2, se tachan todos sus multiplos; comenzando de nuevo, cuando se encuentra
un número entero que no ha sido tachado, ese número es declarado primo, y se procede a tachar todos sus múltiplos,
así sucesivamente. El proceso termina cuando el cuadrado del siguiente número confirmado como primo es mayor que n"""

#Incluye Diagrama de flujo en ReadMe 

def eratostenes(n):
    
     primos = [True] * (n + 1)
     primos[0] = primos[1] = False

    
     for i in range(2, int(n ** 0.5) + 1):
         if primos[i]:
            
            for j in range(i * i, n + 1, i):
                 primos[j] = False

    
            print("Los números primos menores que", n, "son:")
     for i in range(2, n + 1):
         if primos[i]:
              print(i)

eratostenes(100)



# Explicación paso a paso:

"""Primero definimos una funcion, en este caso llamada eratostenes que toma el parametro n.
- Luego creaos una lista de booleanos para representar los números primos 
- inicializamos los elementos de la lista en 0 y 1 porque no son numeros primos 
- luego tachamos los multiplos de cada primo
- mostramos los primos encontrados 
""" 
   