NombreAlumno1=input("Ingrese su nombre:")
Nota1=int(input("Ingrese su primera nota:"))
Nota2=int(input("Ingrese su segunda nota:"))
Nota3=int(input("Ingrese su primera nota:"))
Nota4=int(input("Ingrese su segunda nota:"))
promedio=(Nota1+Nota2+Nota3+Nota4)/4
if promedio<40:
    print(NombreAlumno1,"usted ha reprobado con un promedio de",promedio)
else:
    print(NombreAlumno1, "usted ha aprobado con un promedio de",promedio)