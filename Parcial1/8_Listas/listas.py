"""
list (Array)
son colecciones o conjunto de datos/valores bajo 
un mismo nombre, para acceder a los valores se 
hace con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable. 
Permite miembros duplicados
"""

#Crear una lista con valores numericos enteros e imprimir la lista
# numeros=[23,34]

# print(numeros)

# #recorrer la lista con un for
# for x in numeros:
#     print(x)

# #recorrer la lista con un while
# i=0
# while i<len(numeros):
#     print(numeros[i])
#     i+=1

#Ejemplo 2 Crear una lista de palabras, posteriormente ingresar un palabra buscar la coincidencia
#en la lista e indicar si aparece la palabra y en que posicion en caso contrario indicar una sola
#vez si no la encontro
# palabras=["hola", "2024", "10.23", "True"]
# palabra_buscar=input("Ingresa la palabra a buscar: ")

# if palabra_buscar in palabras:
#     for i in palabras:
#         if palabra_buscar==i:
#             print(f"Encontre la palabra {palabra_buscar}, en la posicion: {palabras.index(i)}")
#     else:
#         print("No se encontro la palabra dentro de la lista") 
# i=0

# if palabra_buscar in palabras:
#     while i < len(palabras):
#         if palabra_buscar==palabras[i]:
#             print(f"Encontre la palabra {palabra_buscar}, en la posicion: {palabras.index(palabras[i])}")
#         i+=1
# else:
#     print("No se encontro la palabra dentro de la lista") 

#Ejemplo 3 Lista multilinea o multidimensional (matriz) para crear una agenda telefonica
# agenda=[
#     ["Carlos",6181234567],
#     ["Fernando", 6182334567],
#     ["Matias", 6691112233],
#     ["Juan Polainas", 6182332345],
# ]

# print (agenda)

# for i in  agenda:
#     print(f"{agenda.index(i)+1}.-{i}")

"""
Ejemplo 4 Crear un porgama que permita gestionar (Administrar) peliculas, colocar un menu de opciones para
agregar, remover, consultar peliculas
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar listas para almacenar los nombres de peliculas
"""

peliculas=[]



def insertarPeliculas():
    pelicula=input("ingrese pelicula: ")
    peliculas.append(pelicula)
    # espereTecla()

def eliminarPeliculas():
    pelicula=input("ingrese pelicula: ")
    peliculas.remove(pelicula)
    if pelicula in peliculas:
        res=input("Desea ")
    # espereTecla()


print("\t*Menu de opciones* \n1. Agregar \n2. Eliminar \n3. consultar \n4. Salir")
opcion=input("Elige la opcion: ").upper()

if opcion in ("1", "AGREGAR", "UNO", "+"):
    peliculas.append(input("Ingrese el nombre de la pelucula: "))
elif opcion in ("2", "REMOVER", "ELIMINAR", "-"):
    peliculas.remove(input("Ingrese el nombre de la pelucula: "))