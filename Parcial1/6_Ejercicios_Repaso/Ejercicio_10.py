i=1
a=0
r=0
for i in range (1,16):
    calificacion=int(input(f"Ingrese la calificacion del alumno {i}: "))

    if calificacion <=100 and calificacion>=80:
        a+=1
    elif calificacion <80 and calificacion>=0:
        r+=1
print(f"Los alumnos aprobados son: {a}")
print(f"Los alumnos reprobados son: {r}")