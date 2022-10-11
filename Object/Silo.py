from Object import Cereal, IndicadorCalidad, Contrato, Silo


class Silo():

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.cereal = Cereal('Trigo')
        self.capacidadActual = 143
        self.capacidadMaxima = 200
        self.valoresIndicadorSilo = [IndicadorCalidad('Enfermedades', 0, 1), 
                                     IndicadorCalidad('Gluten', 30, 50), 
                                     IndicadorCalidad('Ph', 7, 9)]

    def __str__(self):
        texto = "    : {0} : : {0} : : {0} : : {0} :"
        return texto.format(self.nombre, self.cereal, self.capacidadMaxima, self.capacidadActual)
    def __repr__(self):    # para debug
        texto = " {0} \tDivisores: {1}"
        return texto.format(self.nombre, self.personas)
        
    

    def setSilo(arregloSilos: list[Silo], pesoNeto: float, contrato: Contrato, arregloIndicadoresCalidad: list[IndicadorCalidad], valoresIndicadorCalidadCartaDePorte: list[IndicadorCalidad]):
        print('Silos disponibles:')
        for silo in arregloSilos: # Por cada Silo en la lista de Silos:
            if contrato.cereal.nombre == silo.cereal.nombre: # Si coincide el tipo de cereal del Contrato y del Silo:
                if (silo.capacidadActual+pesoNeto) <= silo.capacidadMaxima: # Si la cantidad de trigo que se quiere ingresar no supera la capacidad maxima del silo:
                    for indSilo in silo.valoresIndicadorSilo: # Por cada Indicador de Calidad del Silo:
                        for indCartaPorte in arregloIndicadoresCalidad: # Por cada Indicador de Calidad en la Lista pasada por parametro:
                            if indSilo.nombre == indCartaPorte.nombre: # Si coinciden los nombres de los Indicadores:
                                if (indCartaPorte.valor >= indSilo.valorDesde) and (indCartaPorte.valor <= indSilo.valorHasta): # Si el valor especifico de indCartaPorte esta dentro del rango de los Silos:
                                    print(silo)



                        