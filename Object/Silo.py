
from Object import Cereal, IndicadorCalidad

class Silo():

    def __init__(self, nombre: str, cereal: Cereal, valoresIndicadorSilo: list[IndicadorCalidad]):
        self.nombre = nombre
        self.cereal = cereal
        self.capacidadActual = 143
        self.capacidadMaxima = 200
        self.valoresIndicadorSilo = valoresIndicadorSilo

    def __str__(self):
        texto = "    : {0} : : {1} : : {2} : : {3} :"
        return texto.format(self.nombre, self.cereal, self.capacidadMaxima, self.capacidadActual)
    def __repr__(self):    # para debug
        texto = "    : {0} : : {1} : : {2} : : {3} :"
        return texto.format(self.nombre, self.cereal, self.capacidadMaxima, self.capacidadActual)
    


        



                        