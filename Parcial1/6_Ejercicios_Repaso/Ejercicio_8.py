#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?
num_1=int(input("Ingrese un numero: "))
num_2=int(input("Ingrese numero del porcentaje que desea saber: "))

resul=(num_1/100)*num_2

print(f"El {num_2}% de {num_1} es: {resul}")