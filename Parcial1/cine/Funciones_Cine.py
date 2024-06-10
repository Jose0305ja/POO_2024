"""
Ejemplo 4.- Crear un programa que permita gestionar(Administrar) peliculas, colocas un menu
de opciones para agregar,remover,consultar peliculas.
Notas:
1- Utilizar funciones y mandar llamar desde otro archivo
2- Utilizar listas para almacenar los nombres de peliculas
"""
peliculas=[]
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
def EspereTecla():
      print("Oprima cuaquier tecla para continuar");
      input();
