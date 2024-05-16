"""
Existe una estructura de condicion llamada "if"
la cual evalua la condicion para encontrar el valor "True" y si se cumple
la condicion se ejecuta la linea o lineas codigo

Tenes 4 variantes del if

1.- if simple
2.- if compuesto
3.- if anidado
4.- if y elif
"""
"""
#Ejemplo 1 if simple
color=input("Ingresa un color ")
if color == "rojo":
    print ("Soy el color rojo")

#Ejemplo 2 if compuesto
color=input("Ingresa un color ")
if color == "rojo":
    print ("Soy el color rojo")
else:
    print("No soy el color rojo soy otra cosa")

#Ejemplo 3 if anidado
color=input("Ingresa un color ")
if color == "rojo":
    print ("Soy el color rojo")
    if color !="rojo":
        print("No soy el color rojo")
else:
    print("No soy el color rojo soy otra cosa")

#Ejemplo 4 if y elif
color=input("Ingresa un color ")
if color == "rojo":
    print ("Soy el color rojo")
elif color=="amarillo":
    print ("Soy el color amarillo")
elif color=="azul":
    print ("Soy el color azul")
elif color=="morado":
    print ("Soy el color morado")
else:
    print("No soy ningun color de los anteriores")
"""
#Ejemplo 5 Crear un programa que solicite el numero de la semana
# e imprima en pantalla el dia que le corresponde
numero=int(input("Ingrese el numero de la semana que desea saber el nombre: "))
if numero == 1:
    print ("Lunes")
elif numero==2:
    print ("Martes")
elif numero==3:
    print ("Miercoles")
elif numero==4:
    print ("Jueves")
elif numero==5:
    print ("Viernes")
elif numero==6:
    print ("Sabado")
elif numero==7:
    print ("Domingo")
else:
    print("El numero ingresado no corresponde a ningun dia de la semana")