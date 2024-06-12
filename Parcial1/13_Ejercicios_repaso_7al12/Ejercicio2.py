numeros=[]
num=0
def proceso():
    try:
        global num
        num=int(input("Ingrese un numero "))
        if num<120:
            numeros.append(num) 
    except ValueError:
        print("El valor ingresado no es valido")

# while num<120:
#     proceso()

for x in range (500):
    proceso()
    if num>=120:
        break

print(numeros)