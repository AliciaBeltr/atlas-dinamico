import arcpy
import os
import re

path_especies = os.getcwd() + '\\especies'
especie_listdir = os.listdir(path_especies)


shapes_vacios = []
# Se recorren las carpetas de especies

for folder_especie in especie_listdir:
    directorio = path_especies + '\\' + folder_especie
    folder_path = os.listdir(directorio)
    # Se recorren los archivos en la carpeta de la especie
    for archivo in folder_path:
        # Se indica que trabajaremos con los archivos .tif
        if archivo[-4:] == ".dbf":
            # print archivo
            path_archivo = path_especies + '\\' + folder_especie + '\\' + archivo
            print archivo, arcpy.GetCount_management(path_archivo)

