import arcpy
import os
import re

path_especies = os.getcwd() + '\\especies'
path_shapes = os.getcwd() + '\\shapes'
especie_listdir = os.listdir(path_especies)
anio_actual = "2022"
anio_pasado = "-6000"

especies_en_peligro = []
especies_amenazadas = []

# Se recorren las carpetas de especies

