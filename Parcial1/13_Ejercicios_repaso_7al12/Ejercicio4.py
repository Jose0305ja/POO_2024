def Lista():
    lista=[1,2,3,4,5,6,7]
    print(f"Esta lista {lista} contiene puros numeros enteros")

def Cadena():
    cadena="Hola, como estan!"
    print (f"Esta cadena -{cadena}- contiene puros caracteres ")

def Entero():
    entero=90
    print(f"Esta variable contiene el valor entero: {entero}")

def Logico():
    logico=True
    print(f"Esta es una variable logica contiene el valor: {logico}")

while True:
    print("\n\t..::: Ejercicio 4 :::... \n 1.-Lista \n 2.-Cadena \n 3.-Entero \n 4.-Logico")
    respuesta=input("Ingrese una opcion: ")

    if respuesta=="1":
        Lista()
    elif respuesta=="2":
        Cadena()
    elif respuesta=="3":
        Entero()
    elif respuesta=="4":
        Logico()
    opcion=input("Desea consultar otra opcion SI/NO ").upper()
    if opcion=="NO":
        break
    
