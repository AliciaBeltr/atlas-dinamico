import os
import re

folder = os.getcwd() + '\especies'
path_especies = os.listdir(folder)
anio_actual = "2022"
anio_pasado = "-6000"

# Aqui se define la palabra que queremos cambiar
tif = '.tif'

# Se recorren las carpetas de especies
for folder_especie in path_especies:
    directorio = folder + '\\' + folder_especie
    folder_path = os.listdir(directorio)
    # Se recorren los archivos en la carpeta de la especie
    for archivo in folder_path:
        # Se indica que trabajaremos con los archivos .tif
        if archivo.find(tif) != -1:
            archivo_split = archivo.split('_')

            nombre_especie = archivo_split[0] + ' ' + archivo_split[1]
            tiempo = ''
            anio = ''
            escenario = ''
            # Creamos los datos segun escenario
            if re.search("pasado", archivo_split[2]):
                tiempo = "Pasado"
                anio = anio_pasado
                escenario = "1.0"
            elif re.search("presente", archivo_split[2]):
                tiempo = "Presente"
                anio = anio_actual
                escenario = "1.0"
            else:
                tiempo = "Futuro"
                anio = archivo_split[2][4:8]
                escenario = archivo_split[2][0:2]
            print archivo_split
            print nombre_especie, tiempo, anio, escenario, '\n'