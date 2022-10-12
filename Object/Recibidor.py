from Object import CartaDePorte

class Recibidor():
    def __init__(self, apellido: str, nombre: str, legajo: str, cartasDePorte: list[CartaDePorte]):
        self.apellido = apellido
        self.nombre = nombre
        self.legajo = legajo
        self.cartasDePorte = cartasDePorte