from Object import Transporte

class Modelo():
    def __init__(self, nombre: str, transportes: list[Transporte]):
        self.nombre = nombre
        self.transportes = transportes