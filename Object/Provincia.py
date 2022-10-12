from Object import Ciudad

class Provincia():
    def __init__(self, nombre: str, ciudades: list[Ciudad]):
        self.nombre = nombre
        self.ciudades = ciudades