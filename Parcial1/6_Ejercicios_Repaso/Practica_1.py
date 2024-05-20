# Crear un programa que permita calcular e imprimir el precio a pagar por un articulo.
# En el precio a pagar se incluye el IVA. El programa debera de funcionar n veces como el usuario desee.
print("..::: Sistema tipo Ticket :::..")
#Arrays
nom_arti=[]
precio_uni=[]

#Variables inicializadas
acum=0
conta=0

respuesta=True

while respuesta==True:
    #Entrada de datos
    articulo=str(input("Ingrese el nombre del articulo: "))
    nom_arti.append(articulo)

    precio=float(input("Ingrese el precio del articulo: "))
    precio_uni.append(precio)

    cantidad=int(input("Ingrese la cantidad de articulos: "))

    #proceso
    precio_neto=precio*cantidad

    conta+=1
    acum+=precio_neto
    respues=False
    while respues==False:
        respues=str(input("¿Desea agregar otro producto? [si/no] "))
        respues=respues.lower()
        
        if respues=="si" or "no":
            break
        else:
            print("La opcion ingresada no es valida")
    
    if respues=="si":
        respuesta=True
    else:
        respuesta=False
    print("")

iva=acum*0.16
precio_tot=acum+iva

for i in range (0,conta):
    print(f"{nom_arti[i]}    ${precio_uni[i]}")
print(f"Total a pagar: ${precio_tot}")