def run():
    Paises= {
        'Colombia' : 23,
        'Mexico' : 23,
        'France' :2345,
    }
    for pais,poblacion in Paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
    run()