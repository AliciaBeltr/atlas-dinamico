import os

folder = os.getcwd() + '\especies'
path_especies = os.listdir(folder)

# Aqui se define la palabra que queremos cambiar
word = '_tabla'
new_word = ''

for folder_especie in path_especies:
    directorio = folder + '\\' + folder_especie
    folder_path = os.listdir(directorio)
    for archivo in folder_path:
        if archivo.find(word) != -1:
            new_name = archivo.replace(word,new_word)
            path_archivo = folder + "\\" + folder_especie + '\\' + archivo
            new_path_archivo = folder + "\\" + folder_especie + '\\' + new_name
            # Se renombra el archivo
            os.rename(path_archivo,new_path_archivo)
            print("Nombre anterior: " + archivo + "\t\tNombre nuevo: " + new_name + '\n')
            # print(path_archivo + "\t\t" + new_path_archivo)
            # print(path_archivo)
            # print(new_path_archivo)

