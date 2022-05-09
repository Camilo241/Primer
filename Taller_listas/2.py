#Elaborar un programa en Python que solicite sueldos de turnos de trabajo, en las jornadas de diurno y nocturno para 10 empleados, 5 en cada turno. 
#Visualizar las listas con los sueldos correspondientes a cada turno.
diurno=list() 
nocturno=list() 
for i in range(0,10):
    sueldo=input("ingrese su sueldo ")
    jornada=input("ingrse 'd' si es jornada diurna o 'n' si es jornada nocturna ")
    if jornada=="d" or jornada=="D":
        diurno.append(sueldo)
    elif jornada=="n" or jornada=="N":
        nocturno.append(sueldo)
print(diurno)
print(nocturno)