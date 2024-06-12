numeros=[2,1,6,3,9,4,8,5]
def reco_mos():
    for x in numeros:
        print (x)
    return f"Se imprimieron todos los numeros de la lista"

def reco_mos():
    for x in numeros:
        print (x)
    return f"Se imprimieron todos los numeros de la lista"

def ordenar():
    numeros.sort()
    print(numeros)


def longi():
    longitud=len(numeros)
    return f"La longitud de la lista es {longitud}"


def buscar():
    try:
        num_bus=int(input("Ingrese un numero a buscar: "))
        if num_bus in numeros:
            posicion=numeros.index(num_bus)
            print(f"El numero {num_bus} se encontro en la posicion {posicion}")
    except ValueError:
        print("El dato ingresado no es valido")

print("\n\t..::: Ejercicio 1 :::... \n 1.- Recorrer la lista \n 2.- Ordenarla \n 3.-Ver la longitud \n 4.- Buscar un elemento")
respuesta=input("Ingrese una opcion: ")
if respuesta=="1":
    reco_mos()
elif respuesta=="2":
    ordenar()
elif respuesta=="3":
    print(longi())
elif respuesta=="4": 
    buscar()



