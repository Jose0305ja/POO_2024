# Ciclo For Estructura iterativa que se ejecuta X veces

#Sintaxis
#  for variable in elemento_iterable (lista, rango, etc)
#   bloque de intrucciones

#Ejemplo 1 Crear un programa que imprima en pantalla 5 veces el arroba
contador=1
for contador in range (1,6):
    print("@")

#Ejemplo 2 Crear un programa que imprima los numero del uno al 5 y los sume y al final imprima la suma
contador=1
acumulador=0
for contador in range (1,6):
    print(contador)
    acumulador+=contador
print(f"La suma es: {acumulador}")

#Ejemplo 3 Crear un programa que imprima la tabla de multiplicar que el usuario desee
numero=int(input("Ingrese el numero para calcular su tabla de multiplicar: "))

i=1
multi=0
for i in range(1,11):
    multi=i*numero
    print(f"{numero} x {i} = {multi}")

