#Manejo de errores es la forma en la que tienen los lenguajes de programacion para evitar
#que sucedan errores en tiempo de ejecución

#Ejemplo 1 Error cuando una varible no se genera
# try:
#     nombre=input("Dame el nombre: ")

#     if len(nombre)>1:
#         nombre_usuario="EL nombre es: "+nombre

#     print(nombre_usuario)
# except:
#     print("Es necesario introducir un nombre de usuario")

# #Ejemplo 2 cuando se solicita un numero y se introduce una letra

# try:
#     numero=int(input("Dame un numero: "))

#     if numero>0:
#         print("Soy un numero entero positivo")
#     else:
#         print("Soy un numero entero negativo")
    
# except:
#     print("No se puede convertir un caracter no numerico a numero")
# else:
#     print("Todo se ejecuto sin errores")

#Ejemplo 3 Cuando se generan multiples excepciones

try:
    numero=int(input("Dame un numero: "))
    print("El cuadrado es: "+str(numero*numero))
except ValueError:
    print("Debes de introducir un numro, no se puede convertir un caracter que no sea numerico")
except TypeError:
    print("No es posible convertir el numero a entero")

#Else cuando no se encuentre ningun error
else:
    print("Finalizo correctamente")

#Finally cuando ya termine la ejecucion si tiene errores o no
finally:
    print("Se realizo el proceso")