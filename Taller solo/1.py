class Robot:
    def __init__(self,nombre):
        self.nombre = nombre
    def __saludo__(self):
        print("Hola, mi nombre es", self.nombre)
    def __del__(self):
        print("Se han terminado mis baterias. Me voy a dormir.")

robot1 = Robot("C7PQ")
robot1.__saludo__() 
print(id(robot1))
del robot1 