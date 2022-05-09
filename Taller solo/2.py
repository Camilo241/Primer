class volumen:
    'Clase para controlar volumen de un reproductor multimedia'
    def __init__(self): # método constructor de objeto. Activa volumen
        self.nivel = 3 # sitúa el nivel de volumen en 3
        print('nivel', self.__class__.__name__, self.nivel)
    def subir(self): # método para subir el nivel de volumen de 1 en 1
        self.nivel += 1
        if self.nivel > 10: # al intentar sobrepasar el nivel 10
            self.nivel = 10 # el nivel permanece en 10
            print('nivel', self.__class__.__name__, self.nivel)
    def bajar(self): # método para bajar el nivel de 1 en 1
        self.nivel -= 1
        if self.nivel < 0: # al intentar bajar por debajo del nivel 0
            self.nivel = 0 # el nivel permanece en 0
            print('nivel', self.__class__.__name__, self.nivel)
    def silenciar(self): # método para silenciar
        self.nivel = 0 # el nivel se sitúa en el 0
        print('nivel', self.__class__.__name__, self.nivel)
class graves(volumen): # crea clase graves a partir de clase volumen
    pass

10

ControlVolumen = volumen() # crea objeto y activa el volumen en 3
ControlVolumen.subir() # sube el volumen del nivel 3 al 4
ControlVolumen.bajar() # baja el volumen del nivel 4 al 3
ControlVolumen.silenciar() # silencia volumen bajando del 3 al 0
ControlGraves = graves() # crea objeto control graves, activa nivel 3
ControlGraves.subir() # sube el nivel de graves del 3 nivel al 4
del ControlVolumen # borra el objeto
del ControlGraves # borra el objeto