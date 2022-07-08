import random
def run():
    aleatorio = random.randint(1, 100)
    numero = int(input('Elige un numero del 1 al 100: '))
    while numero != aleatorio:
        if numero < aleatorio:
            print('Elija un numero mayor. ')
        else:
            print('Elija un numero menor. ')
        numero= int(input('Elige otro numero. '))
    print('Felicidades')

if __name__ == '__main__':
    run()