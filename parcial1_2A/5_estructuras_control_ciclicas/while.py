# El Ciclo while Estructura iterativa que se ejecuta X veces 
#siempre y cuando la condicion se cumpla y se seguira ejecutando 
#tantas veces como se Tru la condicion

#Sintaxis
#while condicion:
#   bloque de intrucciones

#Ejemplo 1 Crear un programa que imprima en pantalla 5 veces el arroba
contador=1
while contador <=5:
    print("@")
    contador+=1


#Ejemplo 2 Crear un programa que imprima los numero del uno al 5 y los sume y al final imprima la suma
contador=1
acumulador=0
while contador <=5:
    print(contador)
    acumulador+=contador
    contador+=1
print(f"La suma es: {acumulador}")

#Ejemplo 3 Crear un programa que imprima la tabla de multiplicar que el usuario desee
numero=int(input("Ingrese el numero para calcular su tabla de multiplicar: "))

i=1
multi=0
while i <=10:
    multi=i*numero
    print(f"{numero} x {i} = {multi}")
    i+=1
