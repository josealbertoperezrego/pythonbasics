
#Ejercicios básicos de Python. Clase 1 y 2 en Iron Hack: DEFINICIÓN Y LLAMADA

"""Un país tiene monedas de 1 U, 5 U y 25 U. Si tenemos una cierta cantidad de dinero en una variable,
diseña formulas para dar el cambio óptimo en las monedas descritas. 
completa un programa que pida cierta cantidad de dinero y de una salida"""

#Ejemplo:
"""Dame la cantidad de dinero que desees cambiar: 537
- Desglose de 537 U:
21 MONEDAS DE 25 U
02 MONEDAS DE 5 U
02 MONEDAS DE 1 U"""

#Incluye Diagrama de flujo en ReadMe 


monto = int(input("Dame la cantidad de dinero que quieres cambiar: "))

cantidad_25 = monto // 25
monto = monto % 25

cantidad_5 = monto // 5
monto = monto % 5

cantidad_1 = monto // 1
monto = monto % 1

print("Cantidad de monedas de 25:", cantidad_25)
print("Cantidad de monedas de 5:", cantidad_5)
print("Cantidad de monedas de 1:", cantidad_1)

# Explicación paso a paso:

"""- Primero se crea una variable y definimos que sea INT.
   - Utilizamos la funcion INPUT para crear un campo en la consola para que el usuario
     pueda ingresar un monto. 
   - Se coloca un mensaje claro para que el usuario pueda leer.
   - Comenzamos definiendo una variable con la moneda de mayor denominación y, a partir de ahí, vamos desglosando.
   - Nos aseguramos de usar el operador aritmetico // para la division entera sin decimales y descomponer luego con
     monedas más pequeñas 
   - Al tener un solo monto, dependiendo de la cantidad que ingrese el usuario, nos quedará un restante que iremos
     resolviendo con monedas de menor denominación 
   - Aquí se usa el operador % (modulo) para obtener el restante 
   - Una vez podemos ver el restante, debemos buscar guardarlo en una variable 
   - Aquí podemos guardarlo en la misma variable, lo que se denomina "actualizar una variable"
   - En pocas palabras; el resultado pisa al resultado anterior 
   - 
   """