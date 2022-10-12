from Object import Provincia

class Pais():
    def __init__(self, nombre: str, provincias: list[Provincia]):
        self.nombre = nombre
        self.provincias = provincias