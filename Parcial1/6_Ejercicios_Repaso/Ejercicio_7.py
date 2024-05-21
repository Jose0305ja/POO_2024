#Hacer un programa que muestre todos los numeros impares 
#entre 2 numeros que decida el usuario

num_1=int(input("Ingrese el primer numero: "))
num_2=int(input("Ingrese el segundo numero: "))

for i in range (num_1, num_2):
    divi = i % 2;
    if divi==1:
        print (i);
    i+=1
