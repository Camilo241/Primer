paises = list()
num_paises = int(input('Ingrese la cantidad de paises a ingresar: '))
for i in range(0,num_paises):
    pais=input(f"num_paises {i+1}: ")
    paises.append(pais)
    paises.sort()
print(paises)
