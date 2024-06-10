# opcion =True
# while opcion ==True:
#     print("\t*Menu de opciones* \n1. Suma \n2. Resta \n3. Multiplicacion \n4. Division \n5. Salir")
#     opcion=input("\n Elige una opcion: ").upper()
#     if opcion in ("SUMA","1","+","RESTA","2","-","MULTIPLICACION","3","*","DIVISION","4","/"):
#         n1=int(input("Numero # 1: "))
#         n2=int(input("Numero # 2: "))
#     if opcion=="SUMA" or opcion=="1" or opcion=="+":
#         print(f"{n1}+{n2}={n1+n2}")
#     elif opcion=="RESTA" or opcion=="2" or opcion=="-":
#         print(f"{n1}+{n2}={n1-n2}")
#     elif opcion=="MULTIPLICACION" or opcion=="3" or opcion=="*":
#         print(f"{n1}+{n2}={n1*n2}")
#     elif opcion=="DIVISION" or opcion=="4" or opcion=="/":
#         print(f"{n1}+{n2}={n1/n2}")
#     else :
#         print("Gracias por utilizar el sistema")
#         opcion=False
import os

from Varias_Funciones import *
# def solicitarNumeros():
#     global n1,n2
#     n1=int(input("Numero # 1:"))
#     n2=int(input("Numero # 2:"))

# def calculadora(n1,n2,opcion):
#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
        
#         return f"{n1}+{n2}={n1+n2}"
#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
#         return f"{n1}-{n2}={n1-n2}"
#     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
        
#         return f"{n1}*{n2}={n1*n2}"
#     elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
#         return f"{n1}/{n2}={n1/n2}"

# def esperetecla():
#     print("oprima cualquier tecla para continuar")
#     input()

opcion=True
while opcion:
    os.system("cls")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()
    
    if opcion in ("SUMA","1","+","RESTA","2","-","MULTIPLICACION","3","*","DIVISION","4","/"):
        n1,n2=solicitarNumeros()
        print(calculadora(n1,n2,opcion))
        esperetecla()
    else:
        opcion=False
        print("Gracias por utilizar el sistema ...")