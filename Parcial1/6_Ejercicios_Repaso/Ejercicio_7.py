#Hacer un programa que muestre todos los numeros impares 
#entre 2 numeros que decida el usuario

num_1=int(input("Ingrese el primer numero: "))
num_2=int(input("Ingrese el segundo numero: "))

for i in range (num_1+1, num_2):
    num_1+=1
    divi = num_1 % 2;
    if divi==0:
        print (num_1);
