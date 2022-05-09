#Elaborar un programa en diccionario que permita capturar la información de numero de documento y nombre de 5 personas.
#Al finalizar debe buscar por numero de documento y mostrar la información de esa persona. Se puede elaborar con funciones simples.

estudiante = {}

def main():
    for i in range(0,5):     
        nombre = input("ingrese el nombre del estudiante: ")
        id = int(input("ingrese el id del estudiante: "))
        estudiante[nombre]= id
    buscar_id = int(input('Ingrese el id del estudiante: '))
    print(get_key(buscar_id))

def get_key(buscar_id):
        for key,value in estudiante.items():
            if buscar_id == value:
                return key

        return 'No existe el estudiante con dicho id'

if __name__ == '__main__':
    main()
