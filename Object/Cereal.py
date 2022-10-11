class Cereal():
    def __init__(self, nombre: str):
        self.nombre = nombre
    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)
    def __repr__(self):    # para debug
        texto = "{0}"
        return texto.format(self.nombre)
    