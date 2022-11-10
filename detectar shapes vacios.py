import arcpy
import os
import re

path_especies = os.getcwd() + '\\especies_int'
path_shapes = os.getcwd() + '\\shapes_vacios'
especie_listdir = os.listdir(path_especies)
anio_actual = "2022"
anio_pasado = "-6000"

especies_amenazadas = ["Diphysa americana", "Dussia cuscatlanica","Maclura tinctoria","Manilkara chicle","Sloanea terniflora"]
especies_en_peligro = ["Guaiacum sanctum", "Lonchocarpus rugosus", "Ulmus mexicana"]

# Se recorren las carpetas de especies

for folder_especie in especie_listdir:
    directorio = path_especies + '\\' + folder_especie
    folder_path = os.listdir(directorio)
    # Se crea una carpeta para guardar los shapes
    os.mkdir(path_shapes + '\\' + folder_especie)
    # Se recorren los archivos en la carpeta de la especie
    for archivo in folder_path:
        # Se indica que trabajaremos con los archivos .tif
        if archivo[-4:] == ".tif":
            archivo_split = archivo.split('_')
            nombre_especie = archivo_split[0] + ' ' + archivo_split[1]
            tiempo = ''
            anio = ''
            escenario = ''
            estado_conservacion = ''

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

            # IF PARA SELECCIONAR ESPECIES EN PELIGRO
            if nombre_especie in especies_en_peligro:
                estado_conservacion = "En Peligro"
            elif nombre_especie in especies_amenazadas:
                estado_conservacion = "Amenazada"
            else:
                estado_conservacion = "Preocupacion menor"

            # print archivo_split
            # print nombre_especie, tiempo, anio, escenario, '\n'

            # Se crea un entorno de trabajo para la especie
            workspace_especie = path_shapes + "\\" + nombre_especie
            # print workspace_especie
            arcpy.env.workspace = workspace_especie
            arcpy.env.overwriteOutput = True
            raster_entrada = path_especies + '\\' + folder_especie + '\\' + archivo
            poligono_salida = path_shapes + '\\' + folder_especie + '\\' + archivo[:-4] + ".shp"

            # Process: Raster to Polygon
            tempEnvironmentZ = arcpy.env.outputZFlag
            arcpy.env.outputZFlag = "Disabled"
            tempEnvironmentM = arcpy.env.outputMFlag
            arcpy.env.outputMFlag = "Disabled"
            try:
                arcpy.RasterToPolygon_conversion(
                    raster_entrada,
                    poligono_salida,
                    "NO_SIMPLIFY",
                    "Value",
                    "SINGLE_OUTER_PART",
                    ""
                )
                arcpy.AddField_management(poligono_salida, "especie", "TEXT", "", "", "20")
                # Se agregan los valores
                arcpy.CalculateField_management(poligono_salida,
                                                "especie",
                                                "Consulta erronea",
                                                "PYTHON_9.3"
                                                )
            except Exception as e:
                print "Fallo el archivo", archivo
                print e
            else:
                print "Se realizo el raster de:", archivo
                # Se crean columnas
                arcpy.AddField_management(poligono_salida, "especie", "TEXT", "", "", "20")
                # Se agregan los valores
                arcpy.CalculateField_management(poligono_salida,
                                                "especie",
                                                "Consulta erronea",
                                                "PYTHON_9.3"
                                                )