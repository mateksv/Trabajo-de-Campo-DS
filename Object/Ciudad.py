from Object import Direccion

class Ciudad():
    def __init__(self, nombre: str, codigoPostal: str, direcciones: list[Direccion]):
        self.nombre = nombre
        self.codigoPostal = codigoPostal
        self.direcciones = direcciones