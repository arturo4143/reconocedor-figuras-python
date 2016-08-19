#Programa que genera nuestro conjunto de entrenamiento, es decir, convierte archivos de coordenadas.txt a imagenes bmp
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 22:13:36 2016

@author: Arturo
"""
from resources import trayectorias#se importa la libreria trayectorias desde la carpeta resources
import os#libreria para el manejo de directorios y archivos
import shutil#libreria para manejo de directorios y archivos (eliminar directorios llenos)
from PIL import Image#libreria para abrir la imagen y poder obtener sus caracteristicas
path1='./Coordenadas/'#se define la ruta de nuestras figuras
coordenadas=os.listdir(path1)#se obtienen los directorios contenidos en la carpeta coordenadas
if os.path.exists('./Imagenes'):#se comprueba existencia del directorio Imagenes
    print('Eliminando carpeta existente....')#impresión de pantalla
    shutil.rmtree('./Imagenes/',  ignore_errors=True)#si existe el directorio Imagenes, este se elimina
for carpeta in coordenadas:#ciclo que recorre los directorios contenidos en la carpeta coordenadas 
    print('Procesando carpeta:  '+carpeta+'...................')#impresión de pantalla de la carpeta que se está procesando
    path2=path1+carpeta+'/'#se define la ruta donde se encuentran las coordenadas de cada figura
    figura=os.listdir(path2)#se obtienen los archivos contenidos en la carpeta de coordenadas de cada figura
    i=1#contador para enumerar las imagenes conforme se vayan creando
    if not os.path.exists('./Imagenes/'):#se comprueba existencia del directorio Imagenes
        os.mkdir('./Imagenes/')#si el directorio no existe se crea la carpeta Imagenes
    os.mkdir('./Imagenes/'+carpeta)#se crea una carpeta por cada figura dentro de la carpeta Imagenes
    for file in figura:#ciclo for que recorre los archivos contenidos en cada carpeta
        try:#bloque try para manejo de errores
            puntos = trayectorias.puntosFromJson(path1+carpeta+'/'+file)#leer coordenadas from json y se convierten a puntos
            imagen = trayectorias.puntos2matrizConectada(puntos)#se convierten los puntos en una imagen conectada         
        except:#excepción del bloque try
            continue#si se genera algun error en la lectura del json, sale del ciclo y continua con la siguiente coordenada
        img=Image.fromarray(255*imagen)#se crea imagen a partir de un arreglo, multiplicandole 255 a cada pixel para invertir los colores
        img.save('./Imagenes/'+carpeta+'/'+carpeta+str(i)+'.bmp')#se guarda la imagen
        i=i+1#se incrementa el contador que enumera las imagenes