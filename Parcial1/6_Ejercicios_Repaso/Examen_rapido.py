#sistolica valor menor o igual a 120, de 100 a 120
#diastolica valor de 60 a 80 
#pedir 3 a lo largo del dia y sacar promedio
#medicion al final del dia
respuesta="si"
paciente=0
while respuesta=='si':
    nombre=str(input("Ingrese el nombre del paciente: "))
    sangre=str(input("Ingrese el tipo de sangre del paciente: "))
    SIS_1=int(input("Ingrese la presion arterial SIStolica de la primer medicion: "))

    DIA_1=int(input("Ingrese la presion arterial DIAstolica de la primer medicion: "))

    SIS_2=int(input("Ingrese la presion arterial SIStolica de la segunda medicion: "))

    DIA_2=int(input("Ingrese la presion arterial DIAstolica de la segunda medicion: "))

    SIS_3=int(input("Ingrese la presion arterial SIStolica de la tecera medicion: "))

    DIA_3=int(input("Ingrese la presion arterial DIAstolica de la tercera medicion: "))

    SIS_F=int(input("Ingrese la presion arterial SIStolica de la medicion final: "))

    DIA_F=int(input("Ingrese la presion arterial DIAstolica de la medicion final: "))

    promedio_sis=((SIS_1+SIS_2+SIS_3)/3)
    promedio_dia=((DIA_1+DIA_2+DIA_3)/3)

    prome_fin_sis=(promedio_sis+SIS_F)/2

    prome_fin_dia=(promedio_dia+DIA_F)/2
    print(f"El promedio de la medicion de los parciales de la SIStolica es igual a: {promedio_sis}")
    print(f"El promedio de la medicion de los parciales de la DIAstolica es igual a: {promedio_dia}")

    print(prome_fin_dia)
    print(prome_fin_sis)
    if prome_fin_sis <=120 and prome_fin_sis >=80 and prome_fin_dia <=80 and prome_fin_dia>=60:
        print("Su precion es normal")
    paciente+=1
    respuesta=input("¿Desea ingresar otro paciente? si/no \n")
    respuesta=respuesta.lower()

print(f"Los pacientes capturados son: {paciente}")
