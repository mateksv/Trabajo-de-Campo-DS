import json
from flask import Flask, request, render_template
import time
from Object import *
valIndSilo01 = [IndicadorCalidad('Enfermedades', 0, 1), 
                 IndicadorCalidad('Gluten', 30, 50), 
                 IndicadorCalidad('Ph', 7, 9)]
valIndSilo02 = [IndicadorCalidad('Enfermedades', 0, 1), 
                 IndicadorCalidad('Gluten', 10, 38), 
                 IndicadorCalidad('Ph', 5, 6)]
valIndSilo03 = [IndicadorCalidad('Enfermedades', 0, 1), 
                 IndicadorCalidad('Gluten', 45, 75), 
                 IndicadorCalidad('Ph', 9, 12)]

ind1 = IndicadorCalidad('Enfermedades', 0, 1)
ind2 = IndicadorCalidad('Enfermedades', 0, 1)

if ind1 == ind2:
    print("iguales")