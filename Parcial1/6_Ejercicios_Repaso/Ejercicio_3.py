# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for
i=0
while i <60:
    resultado=i**2
    print (f"{i} al cudrado es: {resultado}")
    i+=1

for i in range (0,60):
    resultado=i**2
    print (f"{i} al cudrado es: {resultado}")