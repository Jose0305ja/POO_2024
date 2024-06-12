peliculas=[]
import math
#Funcion 1
def InsertarPeliculas():
            nombre=input("Ingrese el nombre de la pelicula: ") 
            peliculas.append(nombre)
            print("La pelicula fue agregada con exito!")

#Funcion 2
def EliminarPeliculas():
      nombre=input("Ingrese el nombre de la pelicula: ")
      if nombre in peliculas:
            respuesta=input("Esta seguro de borrar esta pelicula? SI/NO").upper()
            if respuesta=="SI":
                  posicion=peliculas.index(nombre)
                  peliculas.pop(posicion)
                  print("La pelicula fue eliminada con exito!")
            elif respuesta=="NO":
                  print(f"Para volver al menu principal")
      else:
            print("La pelicula no se encuentra en la lista!")   

#Funcion 3
def Consultar():
      print(f"Las peliculas disponibles son: {peliculas}")

#Funcion 4
def Actualizar():
      nombre=input("Ingrese el nombre de la pelicula: ")
      if nombre in peliculas:
            posicion=peliculas.index(nombre)
            nuevo_nombre=input("Ingrese el nuevo nombre de la pelicula: ")
            peliculas[posicion]=nuevo_nombre
            print("La pelicula fue cambiada con exito!")
      else:
            print("La pelicula no se encuentra en la lista!")    

#Funcion 5
def Buscar():
      nombre=input("Ingrese el nombre de la pelicula: ")
      if nombre in peliculas:
            posicion=peliculas.index(nombre)
            print(f"La pelicula es: {peliculas[posicion]}")
      else:
            print("La pelicula no se encuentra en la lista!")

#Funcion 6
def Vaciar():
      respuesta=input("Estas seguro de que deseas vaciar la cartelera? Si/No ").upper()
      if respuesta=="SI":
            peliculas.clear()
            print("La cartelera fue eliminada correctamente")

#Funcion 7
def EspereTecla():
      print("Oprima cuaquier tecla para continuar")
      input()

#Funciones Calculadoras

def solicitarNumeros():
      #global n1,n2
      n1=int(input("Numero # 1:"))
      n2=int(input("Numero # 2:"))
      return n1,n2

def solicitar_num():
      n1=int(input("Numero: "))
      return n1

def calculadora(opcion):
      if opcion=="1" or opcion=="+" or opcion=="SUMA":
            n1,n2=solicitarNumeros()
            return f"{n1}+{n2}={n1+n2}"
      elif opcion=="2" or opcion=="-" or opcion=="RESTA":
            n1,n2=solicitarNumeros()
            return f"{n1}-{n2}={n1-n2}"
      elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
            n1,n2=solicitarNumeros()
            return f"{n1}*{n2}={n1*n2}"
      elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
            n1,n2=solicitarNumeros()
            return f"{n1}/{n2}={n1/n2}"
      elif opcion=="5" or opcion=="**" or opcion=="^" or opcion=="POTENCIA":
            n1=solicitar_num()
            x=pow(n1,2)
            return f"{n1}^2={x}"
      elif opcion=="6" or opcion=="RAIZ":
            n1=solicitar_num()
            x=math.sqrt(n1)
            return f"raiz de {n1}={x}"