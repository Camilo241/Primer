import csv
import os

TABLA = '.Traductor.csv'
ESQUEMA = ['Palabra' , 'Traduccion']
Traductor =[]

def _inicialize_dict_from_storage():
    with open(TABLA,mode= 'r') as f:
        reader = csv.DictReader(f, fieldnames = ESQUEMA)

        for row in reader:
            Traductor.append(row)

def _save_dict_to_storage():
    tmp_table_name = '{}.tmp'.format(TABLA)
    with open(tmp_table_name , mode = 'w') as f:
        writer = csv.DictWriter(f, fieldnames=ESQUEMA)
        writer.writerows(Traductor)

        os.remove(TABLA)
        os.rename(tmp_table_name , TABLA)


def _get_traslator():
    dictionary = {
        'Palabra':_get_key(),
        'Traduccion':_get_value(),
    }

    return dictionary

def _get_key(): 
    field = None
    while not field:
        field = input('Escriba la palabra: ')
    return field

def _get_value():  
    field = None
    while not field:
        field = input('Escriba la Traduccion de la palabra: ')
    return field

def consulta(consulta):
    print('N | Palabra | Traduccion')
    for idx,dic in enumerate(Traductor):

        nombre = dic['Palabra']
        nombre = nombre.upper()
        consulta = consulta.upper()
        
        if nombre == consulta:
            print('{N} | {Palabra} | {Traduccion}'.format(
                N =idx,
                Palabra = dic['Palabra'],
                Traduccion = dic['Traduccion'],
                ))
        elif nombre != consulta and idx < len(Traductor):
            continue
        elif idx == len(Traductor):
            print('La palabra no existe. ')
            break

def list_dict():
    print('N | Palabra | Traduccion')
    for idx,dic in enumerate(Traductor):
        print('{N} | {Palabra} | {Traduccion}'.format(
            N = idx, 
            Palabra = dic['Palabra'],
            Traduccion = dic['Traduccion'] 
            ))

def Actualizar(dict_id,upda_dic):
    global Traductor

    for idx, dic in enumerate(Traductor):

        if idx == dict_id:
            Traductor[dict_id] = upda_dic
            print('La palabra ha sido actualizda')
            input('\n Preseione enter pa continuar. ')
            break
        elif idx != dict_id and idx < len(Traductor):
            continue
        elif idx == len(Traductor):
            print('La palabra no existe.')
            input('\n Preseione enter pa continuar. ')
            break

def main():
    _inicialize_dict_from_storage()
    global Traductor

    while True:

        opcion = 0
        os.system("clear")
        while True:
            try:
                opcion = int(input('''
        Menu Principal
                
    1.Insertar Palabra
    2.Consultar Palabra
    3.Modificar Palabra
    4.Salir

    Digite la opcion que desea: '''))

                break
            except ValueError :
                print('Solo puede escribir numeros.')
                input('\n Preseione enter pa continuar. ')
    
        if opcion == 1 :
            Tra = _get_traslator()
            Traductor.append(Tra)
            print('La palabra ha sido almacenada. ')
            input('\n Preseione enter pa continuar. ')
        elif opcion == 2:
            key = _get_key()
            consulta(key)
            input('\n Preseione enter pa continuar. ')
        elif opcion == 3:
            print('Seleccione la palabra que desea moodificar: ')
            list_dict()
            dic_id = int(input('Digite el N de la Palabra: '))
            upda_dic = _get_traslator()
            Actualizar(dic_id,upda_dic)

        elif opcion == 4:
            break 
        else: 
            print('Digite una opcion valida,Gracias :D.')
            input('\n Preseione enter  Pa continuar. ')

    _save_dict_to_storage()
if __name__ == '__main__':
    main()
