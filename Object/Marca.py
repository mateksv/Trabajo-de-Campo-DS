from Object import Modelo

class Marca():
    def __init__(self, nombre: str, modelos: list[Modelo]):
        self.nombre = nombre
        self.modelos = modelos