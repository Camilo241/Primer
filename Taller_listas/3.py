import operator
pobla = {}
n = int(input("Cuantos paises desea ingresar? "))
for i in range(0,n):
    pais = input("ingrese el pais: ")
    poblacion = input("ingrese la poblacion del pais: ")
    pobla[pais] = poblacion

p_s =sorted(pobla.items(),key =operator.itemgetter(1))

for pais in enumerate(p_s):
    print(pais[1][0],"tiene",pobla[pais[1][0]],"habitantes")
