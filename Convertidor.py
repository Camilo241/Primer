
def conversacion(Tipo_pesos, Valor_dolar):
    valor = int(input('Cuantos pesos ' + Tipo_pesos +' tiene?: '))
    convertidor=valor/Valor_dolar
    Tipo_pesos =print('Hola', nombre ,'Tienes $', convertidor , ' dolares')
nombre = str(input('Ingrese su nombre: '))
nombre = nombre.capitalize()
nombre = nombre.strip()
print('Hola' , nombre , 'Que pesos deseas convertir a dolares?')
menu ="""
1.Pesos Colombianos 
2.Pesos Argentinos
3.Pesos Mexicanos

"""
opcion = int(input(menu))

if opcion == 1:
    conversacion('Colombianos' ,4000)
elif opcion ==2:
    conversacion('Argentinos' ,126)    
elif opcion ==3:
    conversacion('Mexicanos',19)
else:
    print('Ingrese una opion valida.')