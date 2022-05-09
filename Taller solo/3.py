class Telefono:
    "Clase teléfono"
    def __init__(self):
        pass
    def telefonear(self):
        print('llamando')
    def colgar(self):
        print('colgando')
class Camara:
    "Clase camara fotográfica"
    def __init__(self):
        pass
    def fotografiar(self):
        print('fotografiando')
class Reproductor:
    "Clase Reproductor Mp3"
    def __init__(self):
        pass
    def reproducirmp3(self):
        print('reproduciendo mp3')
    def reproducirvideo(self):
        print('reproduciendo video')
class Movil(Telefono, Camara, Reproductor):
        def __del__(self):
            print('Móvil apagado')
movil1 = Movil()
#print(dir(movil1))
movil1.reproducirmp3()
movil1.reproducirvideo()
movil1.fotografiar()
movil1.telefonear()
movil1.colgar() 
del movil1