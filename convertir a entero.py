import arcpy
from arcpy import env
from arcpy.sa import *
import os

path_especies = os.getcwd() + '\\especies'
path_especies_int = os.getcwd() + '\\especies_int'
especie_listdir = os.listdir(path_especies)
anio_actual = "2022"
anio_pasado = "-6000"

especies_en_peligro = []
especies_amenazadas = []

# Se recorren las carpetas de especies
arcpy.CheckOutExtension("Spatial")

for folder_especie in especie_listdir:
    directorio = path_especies + '\\' + folder_especie
    folder_path = os.listdir(directorio)
    # Se especifica el directorio de salida
    path_out = path_especies_int + '\\' + folder_especie + '\\'
    path_out_2 = path_out.replace("\\", '/')
    os.mkdir(path_out_2[:-1])
    # Se recorren los archivos en la carpeta de la especie
    for archivo in folder_path:
        # Se indica que trabajaremos con los archivos .tif
        if archivo[-4:] == ".tif":
            path_raster = path_especies + '\\' + folder_especie + '\\' + archivo
            # print path_raster, path_out_2
            env.workspace = path_out
            try:
                outInt = Int(path_raster)
                outInt.save(path_out_2 + archivo)
                print "Se convirtio a Entero: ", archivo
            except Exception as e:
                print "No se pudo convertir a Entero", archivo
                print e, '\n'

arcpy.CheckInExtension("Spatial")