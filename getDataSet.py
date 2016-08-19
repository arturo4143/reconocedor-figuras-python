#programa que genera nuestro DataSet
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 22:13:36 2016

@author: Arturo
"""
import matplotlib.image as mpimg#libreria para leer la imagen y pueda ser procesada
import numpy as np#libreria para efectuar operaciones entre vectores y matrices
import csv#libreria que nos permite interactuar con archivos csv
from PIL import Image#libreria para abrir la imagen y poder obtener sus caracteristicas
import os#libreria para el manejo de directorios y archivos
from resources import trayectorias#se importa la libreria trayectorias desde la carpeta resources    
archivo= open('DataSet.csv', 'w', newline='')#se crea el archivo csv donde se guardará el Dataset
salida = csv.writer(archivo) #se transfiere el archivo a esta variable para poder escribir en el
img_path='./Imagenes/'#se define la ruta de nuestro training set
trainingSet=os.listdir(img_path)#se obtienen los directorios (folders) contenidos en la carpeta Imagenes en forma de lista
for folder in trainingSet:#ciclo for que recorre los folders contenidos en la carpeta "Imagenes"
    print('Procesando carpeta-----------------------> '+folder)#se imprime el nombre de la imagen en procesamiento, en la términal de Python        
    figura=os.listdir(img_path+folder)#se crea una lista que contiene todos los archivos contenidas en el folder de cada figura
    for file in figura:#ciclo para recorrer todas las imagenes (file) contenidos en la carpeta
        img=mpimg.imread(img_path+folder+'/'+file)#se lee la imagen que se desea clasificar
        img2=Image.open(img_path+folder+'/'+file)#se abre la imagen que esta en procesamiento        
        columnas=img2.size[0]#se obtienen las columnas de la imagen en procesamiento
        filas=img2.size[1]#se obtienen las filas de la imagen en procesamiento
        divfil=filas/11#se divide la cantidad de filas entre 11 para obtener 10 lineas verticales
        divcol=columnas/11#se divide la cantidad de columnas entre 11 para obtener 10 lineas horizontales
        c1=filas/columnas#se calcula la razón filas columnas y se almacena en la variable c1
        completa=img[0:filas,0:columnas]#se copian todos los pixeles de la imagen a una variable
        corner1=img[0:filas*0.10,0:columnas*0.10]#se obtiene la region correspondiente a la esquina 1 de la imagen
        corner2=img[0:filas*0.10,(columnas-(columnas*0.10)):columnas]#se obtiene la region correspondiente a la esquina 2 de la imagen
        corner3=img[(filas-(filas*0.10)):filas,0:columnas*0.10]#se obtiene la region correspondiente a la esquina 3 de la imagen
        corner4=img[(filas-(filas*0.10)):filas,(columnas-(columnas*0.10)):columnas]#se obtiene la region correspondiente a la esquina 4 de la imagen
        centro=img[(divfil*5):(divfil*6),(divcol*5):(divcol*6)]#se obtiene la region correspondiente a la esquina 4 de la imagen
        total=np.count_nonzero(completa)#se obtiene la cantidad pixeles distintos de 0 en la región relacionada        
        c2=np.count_nonzero(corner1)/total#se obtiene la cantidad pixeles distintos de 0 en la región relacionada
        c3=np.count_nonzero(corner2)/total#se obtiene la cantidad pixeles distintos de 0 en la región relacionada
        c4=np.count_nonzero(corner3)/total#se obtiene la cantidad pixeles distintos de 0 en la región relacionada
        c5=np.count_nonzero(corner4)/total#se obtiene la cantidad pixeles distintos de 0 en la región relacionada
        try:#bloque try para manejo de errores
            c6=np.count_nonzero(centro)/centro.size#se obtiene la cantidad pixeles distintos de 0 en la región relacionada
        except:#excepción del bloque try
            continue#si se genera algun error en la lectura del json, sale del ciclo y continua con la siguiente coordenada
        c7=trayectorias.distSup(img,divcol*1,filas)#se obtiene y se almacena la distancia entre el borde superior de la imagen y el pixel más cercano verticalmente 
        c8=trayectorias.distSup(img,divcol*2,filas)#se obtiene y se almacena la distancia entre el borde superior de la imagen y el pixel más cercano verticalmente 
        c9=trayectorias.distSup(img,divcol*3,filas)#se obtiene y se almacena la distancia entre el borde superior de la imagen y el pixel más cercano verticalmente 
        c10=trayectorias.distSup(img,divcol*4,filas)#se obtiene y se almacena la distancia entre el borde superior de la imagen y el pixel más cercano verticalmente 
        c11=trayectorias.distSup(img,divcol*5,filas)#se obtiene y se almacena la distancia entre el borde superior de la imagen y el pixel más cercano verticalmente 
        c12=trayectorias.distSup(img,divcol*6,filas)#se obtiene y se almacena la distancia entre el borde superior de la imagen y el pixel más cercano verticalmente 
        c13=trayectorias.distSup(img,divcol*7,filas)#se obtiene y se almacena la distancia entre el borde superior de la imagen y el pixel más cercano verticalmente 
        c14=trayectorias.distSup(img,divcol*8,filas)#se obtiene y se almacena la distancia entre el borde superior de la imagen y el pixel más cercano verticalmente 
        c15=trayectorias.distSup(img,divcol*9,filas)#se obtiene y se almacena la distancia entre el borde superior de la imagen y el pixel más cercano verticalmente 
        c16=trayectorias.distSup(img,divcol*10,filas)#se obtiene y se almacena la distancia entre el borde superior de la imagen y el pixel más cercano verticalmente 
        
        c17=trayectorias.distInf(img,divcol*1,filas)#se obtiene y se almacena la distancia entre el borde inferior de la imagen y el pixel más cercano verticalmente 
        c18=trayectorias.distInf(img,divcol*2,filas)#se obtiene y se almacena la distancia entre el borde inferior de la imagen y el pixel más cercano verticalmente 
        c19=trayectorias.distInf(img,divcol*3,filas)#se obtiene y se almacena la distancia entre el borde inferior de la imagen y el pixel más cercano verticalmente 
        c20=trayectorias.distInf(img,divcol*4,filas)#se obtiene y se almacena la distancia entre el borde inferior de la imagen y el pixel más cercano verticalmente 
        c21=trayectorias.distInf(img,divcol*5,filas)#se obtiene y se almacena la distancia entre el borde inferior de la imagen y el pixel más cercano verticalmente 
        c22=trayectorias.distInf(img,divcol*6,filas)#se obtiene y se almacena la distancia entre el borde inferior de la imagen y el pixel más cercano verticalmente 
        c23=trayectorias.distInf(img,divcol*7,filas)#se obtiene y se almacena la distancia entre el borde inferior de la imagen y el pixel más cercano verticalmente 
        c24=trayectorias.distInf(img,divcol*8,filas)#se obtiene y se almacena la distancia entre el borde inferior de la imagen y el pixel más cercano verticalmente 
        c25=trayectorias.distInf(img,divcol*9,filas)#se obtiene y se almacena la distancia entre el borde inferior de la imagen y el pixel más cercano verticalmente 
        c26=trayectorias.distInf(img,divcol*10,filas)#se obtiene y se almacena la distancia entre el borde inferior de la imagen y el pixel más cercano verticalmente 
        
        c27=trayectorias.distIzq(img,divfil*1,columnas)#se obtiene y se almacena la distancia entre el borde izquierdo de la imagen y el pixel más cercano horizontalmente 
        c28=trayectorias.distIzq(img,divfil*2,columnas)#se obtiene y se almacena la distancia entre el borde izquierdo de la imagen y el pixel más cercano horizontalmente
        c29=trayectorias.distIzq(img,divfil*3,columnas)#se obtiene y se almacena la distancia entre el borde izquierdo de la imagen y el pixel más cercano horizontalmente
        c30=trayectorias.distIzq(img,divfil*4,columnas)#se obtiene y se almacena la distancia entre el borde izquierdo de la imagen y el pixel más cercano horizontalmente
        c31=trayectorias.distIzq(img,divfil*5,columnas)#se obtiene y se almacena la distancia entre el borde izquierdo de la imagen y el pixel más cercano horizontalmente
        c32=trayectorias.distIzq(img,divfil*6,columnas)#se obtiene y se almacena la distancia entre el borde izquierdo de la imagen y el pixel más cercano horizontalmente
        c33=trayectorias.distIzq(img,divfil*7,columnas)#se obtiene y se almacena la distancia entre el borde izquierdo de la imagen y el pixel más cercano horizontalmente
        c34=trayectorias.distIzq(img,divfil*8,columnas)#se obtiene y se almacena la distancia entre el borde izquierdo de la imagen y el pixel más cercano horizontalmente
        c35=trayectorias.distIzq(img,divfil*9,columnas)#se obtiene y se almacena la distancia entre el borde izquierdo de la imagen y el pixel más cercano horizontalmente
        c36=trayectorias.distIzq(img,divfil*10,columnas)#se obtiene y se almacena la distancia entre el borde izquierdo de la imagen y el pixel más cercano horizontalmente
        
        c37=trayectorias.distDer(img,divfil*1,columnas)#se obtiene y se almacena la distancia entre el borde derecho de la imagen y el pixel más cercano horizontalmente
        c38=trayectorias.distDer(img,divfil*2,columnas)#se obtiene y se almacena la distancia entre el borde derecho de la imagen y el pixel más cercano horizontalmente
        c39=trayectorias.distDer(img,divfil*3,columnas)#se obtiene y se almacena la distancia entre el borde derecho de la imagen y el pixel más cercano horizontalmente
        c40=trayectorias.distDer(img,divfil*4,columnas)#se obtiene y se almacena la distancia entre el borde derecho de la imagen y el pixel más cercano horizontalmente
        c41=trayectorias.distDer(img,divfil*5,columnas)#se obtiene y se almacena la distancia entre el borde derecho de la imagen y el pixel más cercano horizontalmente
        c42=trayectorias.distDer(img,divfil*6,columnas)#se obtiene y se almacena la distancia entre el borde derecho de la imagen y el pixel más cercano horizontalmente
        c43=trayectorias.distDer(img,divfil*7,columnas)#se obtiene y se almacena la distancia entre el borde derecho de la imagen y el pixel más cercano horizontalmente
        c44=trayectorias.distDer(img,divfil*8,columnas)#se obtiene y se almacena la distancia entre el borde derecho de la imagen y el pixel más cercano horizontalmente
        c45=trayectorias.distDer(img,divfil*9,columnas)#se obtiene y se almacena la distancia entre el borde derecho de la imagen y el pixel más cercano horizontalmente
        c46=trayectorias.distDer(img,divfil*10,columnas)#se obtiene y se almacena la distancia entre el borde derecho de la imagen y el pixel más cercano horizontalmente
        dataset=[]#se define una lista llamada dataset, donde se almacenarán las instancias obtenidas en cada imagen procesada
        #se define una lista llamada instancia, donde se almacenan los datos y caracteristicas de la imagen procesada        
        instancia=[(file), (folder), (c1),(c2),(c3),(c4),(c5),(c6),
                   (c7),(c8),(c9),(c10),(c11),(c12),(c13),(c14),(c15),(c16),
                   (c17),(c18),(c19),(c20),(c21),(c22),(c23),(c24),(c25),(c26),
                   (c27),(c28),(c29),(c30),(c31),(c32),(c33),(c34),(c35),(c36),  
                   (c37),(c38),(c39),(c40),(c41),(c42),(c43),(c44),(c45),(c46)]
        ######################################################################################################################################################################################
        dataset.append(instancia)#la instancia es agregada en una nueva linea del dataset
        salida.writerows(dataset)#el contenido del dataset es enviado al archivo csv
archivo.close()#se cierra la escritura del achivo csv
os.system("Dataset.csv")#se apertura el achivo creado "DataSet.csv"