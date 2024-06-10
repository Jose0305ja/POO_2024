from Funciones_Cine import InsertarPeliculas,EliminarPeliculas,Consultar,Actualizar,EspereTecla
import os

opcion=True
while opcion:
    print("\n\t..::: CINCEMEX :::... \n 1.- Agregar \n 2.- Eliminar \n 3.- Consultar \n 4.- Actualizar \n 5.- SALIR ")
    opcion=input("\t Elige una opción: ").upper();
    os.system("cls")
    if opcion in ("1","AGREGAR","2","ELIMINAR","3","CONSULTAR","4","ACTUALIZAR"):
        if opcion=="1" or opcion=="AGREGAR":
            InsertarPeliculas()
            EspereTecla()
            os.system("cls")
        elif opcion=="2"or opcion=="ELIMINAR":
            EliminarPeliculas()
            EspereTecla()
            os.system("cls")
        elif opcion=="3"or opcion=="CONSULTAR":
            Consultar()
            EspereTecla()
            os.system("cls")
        elif opcion=="4"or opcion=="ACTUALIZAR":
            Actualizar()
            EspereTecla()
            os.system("cls")
    else:
        opcion= False
        print("Gracias por usar el sistema")





