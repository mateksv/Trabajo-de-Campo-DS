from Object import Contrato, IndicadorCalidad, Silo

class CartaDePorte():
    def __init__(self, nombre: str ):
        self.nombre = nombre
        self.silo = 'No Asignado'

    
    def setSilo(self, listaSilos: list[Silo], pesoNeto: float, contrato: Contrato, arregloIndicadoresCalidad: list[IndicadorCalidad], valoresIndicadorCalidadCartaDePorte: list[IndicadorCalidad]) -> Silo:
        '''Filtra los Silos disponibles y adecuados para depositar el cereal'''
        print('Silos disponibles:')
        for silo in listaSilos: # Por cada Silo en la lista de Silos:
            if contrato.cereal.nombre == silo.cereal.nombre: # Si coincide el tipo de cereal del Contrato y del Silo:
                if (silo.capacidadActual+pesoNeto) <= silo.capacidadMaxima: # Si la cantidad de trigo que se quiere ingresar no supera la capacidad maxima del silo:
                    for indSilo in silo.valoresIndicadorSilo: # Por cada Indicador de Calidad del Silo:
                        for indCartaPorte in arregloIndicadoresCalidad: # Por cada Indicador de Calidad en la Lista pasada por parametro:
                            if indSilo.nombre == indCartaPorte.nombre: # Si coinciden los nombres de los Indicadores:
                                if (indCartaPorte.valor >= indSilo.valorDesde) and (indCartaPorte.valor <= indSilo.valorHasta): # Si el valor especifico de indCartaPorte esta dentro del rango de los Silos:
                                    print(silo)