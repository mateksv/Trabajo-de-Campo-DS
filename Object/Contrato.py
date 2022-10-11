from Object import Cereal

class Contrato():
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.cereal = Cereal('Trigo')