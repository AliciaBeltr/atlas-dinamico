# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# estructura_datos_atributos.py
# Created on: 2021-11-30 10:09:02.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: estructura_datos_atributos <Raster_entrada> <POligono_salida> <Conservacion> <Especie> <tiempo> <clasificacion> <anno> <escenario> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
import re
import os
import glob
import shutil
from arcpy import env

# env.overwriteOutput = True

path = "C:\\Users\\hsdgev\\Documents\\atlas_20_especies\\datos_especies"

os.chdir(path) # Asegura que se esté trabajando en el fólder deseado

##"Allophylus racemosus",
##            "Apeiba tibourbou",
##            "Bauhinia ungulata",
##            "Calycophyllum candidissimum",
##            "Casearia corymbosa",
##            "Cochlospermum vitifolium",
##            "Coutarea hexandra",
##            "Critonia morifolia",
##            "Curatella americana",
#
#             "Hamelia patens",
#             "Ixora floribunda",
#             "Jatropha curcas",
#             "Karwinskia calderonii",
##            "Malvaviscus arboreus",
##            "Sloanea terniflora",
##            "Trichilia americana"
especies = ["Diphysa americana", # Amenazada
           "Enterolobium cyclocarpum",
            "Guaiacum sanctum", # Amenazada
            "Maclura tinctoria"]


for spp in especies:
    print spp
    std_name = re.sub("\s+","_",spp.lower()) # El nombre estandar para manipulacion ej. "genero_especie"
    print std_name, " este es el nombre de la especie"
    path = "C:\\Users\\hsdgev\\Documents\\atlas_20_especies\\datos_especies\\"+std_name+""
    print path, "este es el path"
    os.chdir(path)
    tif_files = [re.search("final.tif$",tif_file).string for tif_file in os.listdir(path) if re.search("final.tif$",tif_file)]
    print tif_files," lsitado de archivos"
    

    database="C:\\Users\\hsdgev\\Documents\\atlas_20_especies\\"+std_name
    print database, "esta es la database"
    env.workspace = database
    env.overwriteOutput = True
    
    for tif in tif_files:
        print tif, "este es el nombre original del arhivo"
        if re.search("[2-8]\.[056]",tif):
            new_tif = tif.replace('.', '',1)
            #new_tif = tif.replace(' ', '_')
            tiempo_proyeccion = tif.split("_")[2]
            #tiempo_proyeccion = re.search("20[75]0",tif).group(0)
            #anno = tiempo_proyeccion
            rcp=tif.split("_")[3][:3]
            shutil.copyfile(""+tif+"",""+new_tif+"")

        else:
            if re.search("presente",tif):
                new_tif = tif#.replace('.', '',1)
                tiempo_proyeccion = "2021"
                #anno = "2021"
                rcp = "1.0"

            else:
                new_tif=tif#.replace('.', '',1)
                tiempo_proyeccion = "-6000"
                #anno = "-6000"
                rcp = "1.0"
        print new_tif," nombre modificado"
        print tiempo_proyeccion
        print rcp
        
        #shutil.copyfile(""+tif+"",""+new_tif+"")
        ##tiempo_proyeccion = re.search("20[75]0",tif)
        #tiempo_proyeccion = tif.split("_")[1]
        #print tiempo_proyeccion

        # Script arguments
        Raster_entrada = arcpy.GetParameterAsText(0)
        print Raster_entrada
        if Raster_entrada == '#' or not Raster_entrada:
            Raster_entrada = new_tif # provide a default value if unspecified
            #Raster_entrada_renombrado=
            
            print Raster_entrada, "este es el raster de entrada"
    
        POligono_salida = arcpy.GetParameterAsText(1)
        print POligono_salida
        
        if POligono_salida == '#' or not POligono_salida:
            
            POligono_salida = database+"\\"+new_tif[:-4]+".shp" # provide a default value if unspecified
            print POligono_salida
        Conservacion = arcpy.GetParameterAsText(2)
        if Conservacion == '#' or not Conservacion:
            if std_name in ["diphysa_americana","guaiacum_sanctum"]:
                Conservacion = "\"Amenazada\""
            else:
                Conservacion = "\"Preocupación menor\"" # provide a default value if unspecified
        print arcpy.ValidateFieldName(Raster_entrada) + " VALIDACION RASTER ENTRADA"
        print arcpy.ValidateFieldName(POligono_salida), " VALIDACION POLIGONO SALIDA"
        Especie = arcpy.GetParameterAsText(3)
        if Especie == '#' or not Especie:
            Especie = '\"{0}\"'.format(spp) # provide a default value if unspecified
    
        tiempo = arcpy.GetParameterAsText(4)
        if tiempo_proyeccion=="-6000":
           tiempo = "\"Pasado\""
        else:
            if tiempo_proyeccion=="2021":
                tiempo="\"Presente\""
            else:
                tiempo = "\"Futuro\""
            
##        if tiempo == '#' or not tiempo:
##            if tiempo_proyeccion is not None:
##                tiempo = "\"Futuro\"" # provide a default value if unspecified
##            else:
##                if re.search("presente",tif):
##                    tiempo = "\"Presente\""
##                else:
##                    tiempo = "\"Pasado\""

        clasificacion = arcpy.GetParameterAsText(5)
        if clasificacion == '#' or not clasificacion:
            clasificacion = "\"arboles\"" # provide a default value if unspecified
    
        anno = arcpy.GetParameter(6)
        anno=tiempo_proyeccion
        
##        if anno == '#' or not anno:
##            if tiempo_proyeccion is not None:
##                anno = tiempo_proyeccion.group(0) # provide a default value if unspecified
##            else:
##                if re.search("presente",tif):
##                    anno = "2021"
##                else:
##                    anno = "-6000"
    
        escenario = arcpy.GetParameter(7)
        escenario=rcp
##        if escenario == '#' or not escenario:
##            if tiempo_proyeccion is not None:
##                #rcp = re.search("[2-8]\.[056]",tif).group(0)
##                rcp = tif.split("_")[2][:3]
##                escenario = rcp # provide a default value if unspecified
##            else:
##                escenario = "1.0"

        
    
        # Local variables:
        RasterT_tif1__2_ = POligono_salida
        RasterT_tif1__3_ = RasterT_tif1__2_
        RasterT_tif1__4_ = RasterT_tif1__3_
        RasterT_tif1__5_ = RasterT_tif1__4_
        RasterT_tif1__6_ = RasterT_tif1__5_
        RasterT_tif1__7_ = RasterT_tif1__6_
        RasterT_tif1__8_ = RasterT_tif1__7_
        RasterT_tif1 = RasterT_tif1__8_
        RasterT_tif1__9_ = RasterT_tif1
        RasterT_tif1__11_ = RasterT_tif1__9_
        RasterT_tif1__10_ = RasterT_tif1__11_
        RasterT_tif1__13_ = RasterT_tif1__10_
    
        # Process: Raster to Polygon
        tempEnvironment0 = arcpy.env.outputZFlag
        arcpy.env.outputZFlag = "Disabled"
        tempEnvironment1 = arcpy.env.outputMFlag
        arcpy.env.outputMFlag = "Disabled"
        print Raster_entrada, "VERIFICACIÓN RASTER ENTRADA"
        arcpy.RasterToPolygon_conversion(Raster_entrada, POligono_salida, "NO_SIMPLIFY", "Value", "SINGLE_OUTER_PART", "")
        arcpy.env.outputZFlag = tempEnvironment0
        arcpy.env.outputMFlag = tempEnvironment1
    
        # Process: Add Field
        arcpy.AddField_management(POligono_salida, "especie", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    
        # Process: Calculate Field
        arcpy.CalculateField_management(RasterT_tif1__2_, "especie", Especie, "VB", "")
    
        # Process: Add Field (2)
        arcpy.AddField_management(RasterT_tif1__3_, "tiempo", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    
        # Process: Calculate Field (2)
        arcpy.CalculateField_management(RasterT_tif1__4_, "tiempo", tiempo, "VB", "")
    
        # Process: Add Field (3)
        arcpy.AddField_management(RasterT_tif1__5_, "conserv", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    
        # Process: Calculate Field (3)
        arcpy.CalculateField_management(RasterT_tif1__6_, "conserv", Conservacion, "PYTHON_9.3", "")
    
        # Process: Add Field (4)
        arcpy.AddField_management(RasterT_tif1__7_, "clasif", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    
        # Process: Calculate Field (4)
        arcpy.CalculateField_management(RasterT_tif1__8_, "clasif", clasificacion, "PYTHON_9.3", "")
    
        # Process: Add Field (5)
        arcpy.AddField_management(RasterT_tif1, "anno", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    
        # Process: Calculate Field (5)
        arcpy.CalculateField_management(RasterT_tif1__9_, "anno", anno, "PYTHON_9.3", "")
    
        # Process: Add Field (6)
        arcpy.AddField_management(RasterT_tif1__11_, "escenario", "FLOAT", "3", "1", "", "", "NULLABLE", "NON_REQUIRED", "")
    
        # Process: Calculate Field (6)
        arcpy.CalculateField_management(RasterT_tif1__10_, "escenario", escenario, "PYTHON_9.3", "")
    
