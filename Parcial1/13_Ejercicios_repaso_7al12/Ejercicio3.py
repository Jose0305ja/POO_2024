palabras=[]
respuesta="SI"
def ingre():
    try:
        global respuesta
        ing_palabra=input("Ingresa una palabra ")
        palabras.append(ing_palabra)
        respuesta=input("Desea agregar otra respuesta si/no ").upper()
    except:
        print("El dato ingresado no es valido")

if len(palabras)<=0:
    while respuesta=="SI":
        ingre()

print(palabras)