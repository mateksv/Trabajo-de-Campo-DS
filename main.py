from Object import *


valoresIndicadorCalidadCartaDePorte = [IndicadorCalidad('Enfermedades', 0, 1), 
                                       IndicadorCalidad('Gluten', 30, 50), 
                                       IndicadorCalidad('Ph', 7, 9)]

arregloIndicadoresCalidad = [IndicadorCalidad('Enfermedades', 0, 1), 
                             IndicadorCalidad('Gluten', 30, 50), 
                             IndicadorCalidad('Ph', 7, 9)]

contrato = Contrato('Contrato Campodonico 01')
pesoNeto = 33


s1 = Silo('silo1')
s2 = Silo('silo2')
s3 = Silo('silo3')
s4 = Silo('silo4')
s5 = Silo('silo5')

arregloSilos = [s1,s2,s3,s4,s5]

Silo.setSilo(arregloSilos, pesoNeto, contrato, arregloIndicadoresCalidad, valoresIndicadorCalidadCartaDePorte)
