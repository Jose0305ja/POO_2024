"""
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa
mas pequeño que cumple una funcion especica. La funcion se puede reutilizar con el simple hecho de 
invocarla es decir mandarla llamar


Sintaxis

def nombredeMifuncion(parametros)
    boque o conjunto de instrucciones

nombredeMifuncion(parametros)

Las funciones pueden ser de 4 tipos:
1.- Funciones que no recibe parametros y no regresa valor
2.- Funcion que no recibe parametros y regresa valor
3.- Funcion que recibe parametros y no regresa valor
4.- Funcion que recibe parametros y regresa valor
"""
# #1.- Funcion que no recibe parametros y no regresa valor
# def sumaNumero1():
#     n1=int(input("Numero # 1: "))
#     n2=int(input("Numero # 2: "))
#     suma=n1+n2
#     print(f"{n1}+{n2}={suma}")
# sumaNumero1()

#2.- Funcion que no recibe parametros y regresa valor
# def sumaNumero2():
#     n1=int(input("Numero # 1: "))
#     n2=int(input("Numero # 2: "))
#     return f"{n1}+{n2}={n1+n2}"

# print(sumaNumero2())

#3.- Funcion que recibe parametros y no regresa valor
# def sumaNumero3(n1,n2):
#     print(f"{n1}+{n2}={n1+n2}")

# n1=int(input("Numero # 1: "))
# n2=int(input("Numero # 2: "))
# sumaNumero3(n1,n2)

#4.- Funcion que recibe parametros y regresa valor
# def sumaNumero4(n1,n2):
#     return f"{n1}+{n2}={n1+n2}"

# n1=int(input("Numero # 1: "))
# n2=int(input("Numero # 2: "))
# print(sumaNumero4(n1,n2))


#Crear un programa que solicite a traves de una funcion la siguiente informacion:
#nombre del paciente, edad, estatura, Tipo de sangre, utilizar los 4 tipos de funcion

#1.- Funcion que no recibe parametros y no regresa valor

# def sumaNumero1():
#     nombre=input("Ingrese el nombre del paciente: ")
#     edad=input("Ingrese la edad del paciente: ")
#     estatura=input("Ingrese la estatura del paciente: ")
#     Tipo_san=input("Ingrese el tipo de sangre del paciente: ")
#     print(f"El paciente {nombre} \ncon {edad} de edad\nmide {estatura} \ntiene el tipo de sangre {Tipo_san}")
# sumaNumero1()

#2.- Funcion que no recibe parametros y regresa valor
# def sumaNumero2():
#     nombre=input("Ingrese el nombre del paciente: ")
#     edad=input("Ingrese la edad del paciente: ")
#     estatura=input("Ingrese la estatura del paciente: ")
#     Tipo_san=input("Ingrese el tipo de sangre del paciente: ")
#     return f"El paciente {nombre} \ncon {edad} de edad\nmide {estatura} \ntiene el tipo de sangre {Tipo_san}"
# print(sumaNumero2())

#3.- Funcion que recibe parametros y no regresa valor
# def sumaNumero3(nombre,edad,estatura,Tipo_san):
#     print(f"El paciente {nombre} \ncon {edad} de edad\nmide {estatura} \ntiene el tipo de sangre {Tipo_san}")

# nombre=input("Ingrese el nombre del paciente: ")
# edad=input("Ingrese la edad del paciente: ")
# estatura=input("Ingrese la estatura del paciente: ")
# Tipo_san=input("Ingrese el tipo de sangre del paciente: ")
# sumaNumero3(nombre,edad,estatura,Tipo_san)

#4.- Funcion que recibe parametros y regresa valor
def sumaNumero3(nombre,edad,estatura,Tipo_san):
    return f"El paciente {nombre} \ncon {edad} de edad\nmide {estatura} \ntiene el tipo de sangre {Tipo_san}"

nombre=input("Ingrese el nombre del paciente: ")
edad=input("Ingrese la edad del paciente: ")
estatura=input("Ingrese la estatura del paciente: ")
Tipo_san=input("Ingrese el tipo de sangre del paciente: ")
print(sumaNumero3(nombre,edad,estatura,Tipo_san))