
#Ejercicios básicos de Python. Clase 1 y 2 en Iron Hack: WHILE 

"""Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga,
(en caso de haber más de una, mostrar la primera) y cuántas palabras había.
Precondición: se tomará como separador de palabras el carácter ESPACIO, ya sea uno o más"""

#Incluye Diagrama de flujo en ReadMe 


frase = input("Dame una frase: ")
palabras = frase.split()


palabra_mas_larga = ""
num_palabras = len(palabras)

i = 0
while i < num_palabras:
    
    if len(palabras[i]) > len(palabra_mas_larga):
     
        palabra_mas_larga = palabras[i]
  
    i += 1


print(f"La palabra más larga es: {palabra_mas_larga}")
print(f"Hay {num_palabras} palabras en la frase.")



# Explicación paso a paso:

"""
- Primero utilizamos la función input para que el usuario pueda ingresar el valor que pedimos
en este caso una frase
- utilizamos split() y sin argumentos para dividir la frase 
- almacenamos esa lista en una variable
- Luego pasamos a inicializar las variables necesarias, "más larga" que estará vacia para guardar la más larga
- Utilizamos la funcion len() para la longitud de palabras
- inicializamos la variable i con el valor 0 como indice para el bucle while 
   """