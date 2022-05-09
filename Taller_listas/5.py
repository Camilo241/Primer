#8.Elaborar un programa en Python que permita capturar información en un diccionario para una agenda donde capture fecha y hora de actividades a realizar (descripción). 
#Pregunte si desea capturar otra actividad 
#Y permita buscar por fecha las actividades registradas
from datetime import datetime
agenda ={}

def main():
    while True:
        actividad = str(input('Ingrese la actividad que desea agendar: '))
        n = print('para la fecha y hora debe ingresarlo con la siguiente secuencia dd-mm,H:M')
        fecha_hora = input('Ingrese la fecha y la hora de la actividad. ')
        fecha_hora = datetime.now()
        format = fecha_hora.strftime('Día :%d-Mes: %m, Hora: %H: Minutos: %M')
        print(actividad)
        print(format)
    
        i = int(input('Ingrese 1 para continuar y capturar otra actividad o 0 para terminar. '))
        if i == 0:
            break

if __name__ == '__main__':
    main()
