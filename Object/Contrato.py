from Object import Cereal, IndicadorCalidad, EncargadoDeCompras
class Contrato():
    def __init__(self, numero: int, nombre: str, cereal: Cereal, encargadoDeCompras: EncargadoDeCompras, indicadoresCalidad: list[IndicadorCalidad], cantidadCereal: float, fechaInicio: str, fechaFin: str, monto: float, unidad: str):
        self.numero = numero
        self.nombre = nombre
        self.cereal = cereal
        self.encargadoDeCompras = encargadoDeCompras
        self.indicadoresCalidad = indicadoresCalidad
        self.cantidadCereal = cantidadCereal
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.monto = monto
        self.unidad = unidad
