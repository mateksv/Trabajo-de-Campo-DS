import json
from flask import Flask, request, render_template
import time
from Object import *

app = Flask(__name__) # Inicializo Flask


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/encargado')
def encargado():
    return "encargadoDeCompras"



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Fecha actual
DATE = time.strftime("%d/%m/%Y", time.localtime())

# Defino los Indicadores de calidad de la carta de porte
valoresIndicadorCalidadCartaDePorte = [IndicadorCalidad('Enfermedades', 0, 1), 
                                       IndicadorCalidad('Gluten', 30, 50), 
                                       IndicadorCalidad('Ph', 7, 9)]

# Defino la lista de Indicadores de Calidad para el contrato
listaIndicadoresCalidad = [IndicadorCalidad('Enfermedades', 0, 1), 
                             IndicadorCalidad('Gluten', 30, 50), 
                             IndicadorCalidad('Ph', 7, 9)]

# Creo un Encargado de Compras          apellido  nombre  legajo
encargadoDeCompras = EncargadoDeCompras('Batista','Juan', '33032')                

# Creo un contrato
contrato = Contrato(1, 'Contrato Campodonico', Cereal('Trigo'), 
                    encargadoDeCompras, listaIndicadoresCalidad, 200, 
                    DATE, '29/10/2022', 4500, 'U$D')

# Establezco el peso neto del cargamento
pesoNeto = 33

# Defino diferentes estandares de indicadores de calidad para los Silos
valIndSilo01 = [IndicadorCalidad('Enfermedades', 0, 1), 
                 IndicadorCalidad('Gluten', 30, 50), 
                 IndicadorCalidad('Ph', 7, 9)]
valIndSilo02 = [IndicadorCalidad('Enfermedades', 0, 1), 
                 IndicadorCalidad('Gluten', 10, 38), 
                 IndicadorCalidad('Ph', 5, 6)]
valIndSilo03 = [IndicadorCalidad('Enfermedades', 0, 1), 
                 IndicadorCalidad('Gluten', 45, 75), 
                 IndicadorCalidad('Ph', 9, 12)]

# Creo cinco Silos, cada uno con un nombre, tipo de cereal y un determinado rango de Indicadores de Calidad
s1 = Silo('silo1', Cereal('Trigo'), valIndSilo01)
s2 = Silo('silo2', Cereal('Trigo'), valIndSilo02)
s3 = Silo('silo3', Cereal('Trigo'), valIndSilo03)
s4 = Silo('silo4', Cereal('Cebada'), valIndSilo02)
s5 = Silo('silo5', Cereal('Maiz'), valIndSilo01)

# Defino una lista de Silos
listaSilos = [s1,s2,s3,s4,s5]

# Creo una Carta de Porte
cartaDePorte = CartaDePorte('Carta01')

# Llamo a la funcion setSilo()                 arregloIndicadoresCalidad..?
cartaDePorte.setSilo(listaSilos, pesoNeto, contrato, contrato.indicadoresCalidad, valoresIndicadorCalidadCartaDePorte)




def convertir(objeto: object):
    try:
        jsonSTR = json.dumps(objeto.__dict__)
        return jsonSTR
    except Exception as ex:
        print("\n>>>>> ERROR >>>>>", ex)
        for dato in objeto:
            if type(dato) == list:
                for n in dato:
                    nJsonSTR = convertir(n)
                
        


print(convertir(cartaDePorte))
print(convertir(encargadoDeCompras))
