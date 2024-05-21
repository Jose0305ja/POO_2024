#Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla 
#y luego las multiplicaciones del 1 al 10
print("Tablas de multiplicar")

numero=[1,2,3,4,5,6,7,8,9]
i=1
z=1
for i in range(1,11):
    print(f"Tablas de multiplicar {i}")
    for z in range(1,11):
        res=i*z
        print(f"{i} x {z} = {res}")
        z+=1
    print("")
    i+=1
