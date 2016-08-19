#método de clasificación KNN
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 22:13:36 2016

@author: Arturo
"""
from resources import trayectorias#se importa la libreria trayectorias desde la carpeta resources    
import csv#libreria que nos permite interactuar con archivos csv
import math#libreria que nos permite hacer uso de funciones matemáticas
import matplotlib.image as mpimg#libreria para leer la imagen y pueda ser procesada mediante una relación filas, columnas
from PIL import Image#libreria para abrir la imagen y poder obtener sus caracteristicas
import numpy as np#libreria para efectuar operaciones entre vectores y matrices
lns=csv.reader(open('DataSet.csv'))#leemos el dataset con extensión csv
dataset=list(lns)#el contenido del dataset csv se almacena en la variable dataset en forma de lista
print("Nombre de la imagen: ")#impresion de pantalla para recibir el nombre de la imagen que se desea clasificar
NImagen=input()#variable donde se almacena la entrada del usuario
print("Ingrese el valor de K: ")#impresion de pantalla para recibir el valor de K
ktemp=input()#variable donde se almacena la entrada del usuario
k=int(ktemp)#convertimos la entrada recibida a int
img=mpimg.imread('./test/'+NImagen+'.bmp')#se lee la imagen que se desea clasificar
img2=Image.open('./test/'+NImagen+'.bmp')#se abre la imagen que se desea clasificar
columnas=img2.size[0]#se obtienen las columnas de la imagen en procesamiento
filas=img2.size[1]#se obtienen las filas de la imagen en procesamiento
print('Filas: '+str(filas))#impresión en pantalla "filas" de la imagen 
print('Columnas: '+str(columnas))#impresión en pantalla "filas" de la imagen
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

c6=np.count_nonzero(centro)/centro.size#se obtiene la cantidad pixeles distintos de 0 en la región relacionada

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
#se imprimen todas las características de la imagen que se va a clasificar
print('C1: '+str(c1)+'\nC2: '+str(c2)+'\nC3: '+str(c3)+'\nC4: '+str(c4)+'\nC5: '+str(c5)+"\n"+'\nC6: '+str(c6)+"\n"+'\nC7: '+str(c7)+"\n"+'\nC8: '+str(c8)+"\n"+'\nC9: '+str(c9)+"\n"
    +'\nC10: '+str(c10)+"\n"+'\nC11: '+str(c11)+"\n"+'\nC12: '+str(c12)+"\n"+'\nC13: '+str(c13)+"\n"+'\nC14: '+str(c14)+"\n"+'\nC15: '+str(c15)+"\n"+'\nC16: '+str(c16)+"\n"+'\nC17: '+str(c17)+"\n"
    +'\nC18: '+str(c18)+"\n"+'\nC19: '+str(c19)+"\n"+'\nC20: '+str(c20)+"\n"+'\nC21: '+str(c21)+"\n"+'\nC22: '+str(c22)+"\n"+'\nC23: '+str(c23)+"\n"+'\nC24: '+str(c24)+"\n"+'\n25: '+str(c25)+"\n"
    +'\nC26: '+str(c26)+"\n"+'\nC7: '+str(c27)+"\n"+'\nC28: '+str(c28)+"\n"+'\nC29: '+str(c29)+"\n"+'\nC30: '+str(c30)+"\n"+'\nC31: '+str(c31)+"\n"+'\nC32: '+str(c32)+"\n"+'\nC33: '+str(c33)+"\n"
    +'\nC34: '+str(c34)+"\n"+'\nC35: '+str(c35)+"\n"+'\nC36: '+str(c36)+"\n"+'\nC37: '+str(c37)+"\n"+'\nC38: '+str(c38)+"\n"+'\nC39: '+str(c39)+"\n"+'\nC40: '+str(c40)+"\n"+'\nC41: '+str(c41)+"\n"
    +'\nC42: '+str(c42)+"\n"+'\nC43: '+str(c43)+"\n"+'\nC44: '+str(c44)+"\n"+'\nC45: '+str(c45)+"\n"+'\nC46: '+str(c46)+"\n")
contador=0#se declara un contador para recorrer las filas del dataset
for i in dataset:#ciclo for para convertir todo el dataset a numeros flotantes
  dataset[contador][2]=float(dataset[contador][2])#se realiza un cast de string a float 
  dataset[contador][3]=float(dataset[contador][3])#se realiza un cast de string a float
  dataset[contador][4]=float(dataset[contador][4])#se realiza un cast de string a float
  dataset[contador][5]=float(dataset[contador][5])#se realiza un cast de string a float
  dataset[contador][6]=float(dataset[contador][6])#se realiza un cast de string a float
  dataset[contador][7]=float(dataset[contador][7])#se realiza un cast de string a float
  dataset[contador][8]=float(dataset[contador][8])#se realiza un cast de string a float
  dataset[contador][9]=float(dataset[contador][9])#se realiza un cast de string a float
  dataset[contador][10]=float(dataset[contador][10])#se realiza un cast de string a float
  dataset[contador][11]=float(dataset[contador][11])#se realiza un cast de string a float
  dataset[contador][12]=float(dataset[contador][12])#se realiza un cast de string a float
  dataset[contador][13]=float(dataset[contador][13])#se realiza un cast de string a float 
  dataset[contador][14]=float(dataset[contador][14])#se realiza un cast de string a float
  dataset[contador][15]=float(dataset[contador][15])#se realiza un cast de string a float
  dataset[contador][16]=float(dataset[contador][16])#se realiza un cast de string a float
  dataset[contador][17]=float(dataset[contador][17])#se realiza un cast de string a float
  dataset[contador][18]=float(dataset[contador][18])#se realiza un cast de string a float
  dataset[contador][19]=float(dataset[contador][19])#se realiza un cast de string a float 
  dataset[contador][20]=float(dataset[contador][20])#se realiza un cast de string a float
  dataset[contador][21]=float(dataset[contador][21])#se realiza un cast de string a float
  dataset[contador][22]=float(dataset[contador][22])#se realiza un cast de string a float
  dataset[contador][23]=float(dataset[contador][23])#se realiza un cast de string a float
  dataset[contador][24]=float(dataset[contador][24])#se realiza un cast de string a float
  dataset[contador][25]=float(dataset[contador][25])#se realiza un cast de string a float 
  dataset[contador][26]=float(dataset[contador][26])#se realiza un cast de string a float
  dataset[contador][27]=float(dataset[contador][27])#se realiza un cast de string a float
  dataset[contador][28]=float(dataset[contador][28])#se realiza un cast de string a float
  dataset[contador][29]=float(dataset[contador][29])#se realiza un cast de string a float
  dataset[contador][30]=float(dataset[contador][30])#se realiza un cast de string a float
  dataset[contador][31]=float(dataset[contador][31])#se realiza un cast de string a float 
  dataset[contador][32]=float(dataset[contador][32])#se realiza un cast de string a float
  dataset[contador][33]=float(dataset[contador][33])#se realiza un cast de string a float
  dataset[contador][34]=float(dataset[contador][34])#se realiza un cast de string a float
  dataset[contador][35]=float(dataset[contador][35])#se realiza un cast de string a float
  dataset[contador][36]=float(dataset[contador][36])#se realiza un cast de string a float
  dataset[contador][37]=float(dataset[contador][37])#se realiza un cast de string a float
  dataset[contador][38]=float(dataset[contador][38])#se realiza un cast de string a float
  dataset[contador][39]=float(dataset[contador][39])#se realiza un cast de string a float
  dataset[contador][40]=float(dataset[contador][40])#se realiza un cast de string a float
  dataset[contador][41]=float(dataset[contador][41])#se realiza un cast de string a float
  dataset[contador][42]=float(dataset[contador][42])#se realiza un cast de string a float
  dataset[contador][43]=float(dataset[contador][43])#se realiza un cast de string a float
  dataset[contador][44]=float(dataset[contador][44])#se realiza un cast de string a float
  dataset[contador][45]=float(dataset[contador][45])#se realiza un cast de string a float
  dataset[contador][46]=float(dataset[contador][46])#se realiza un cast de string a float
  dataset[contador][47]=float(dataset[contador][47])#se realiza un cast de string a float
  euclidianaTemp=((dataset[contador][2]-c1)**2)+((dataset[contador][3]-c2)**2)+((dataset[contador][4]-c3)**2)+((dataset[contador][5]-c4)**2)+((dataset[contador][6]-c5)**2)+((dataset[contador][7]-c6)**2)+((dataset[contador][8]-c7)**2)+((dataset[contador][9]-c8)**2)+((dataset[contador][10]-c9)**2)+((dataset[contador][11]-c10)**2)+((dataset[contador][12]-c11)**2)+((dataset[contador][13]-c12)**2)+((dataset[contador][14]-c13)**2)+((dataset[contador][15]-c14)**2)+((dataset[contador][16]-c15)**2)+((dataset[contador][17]-c16)**2)+((dataset[contador][18]-c17)**2)+((dataset[contador][19]-c18)**2)+((dataset[contador][20]-c19)**2)+((dataset[contador][21]-c20)**2)+((dataset[contador][22]-c21)**2)+((dataset[contador][23]-c22)**2)+((dataset[contador][24]-c23)**2)+((dataset[contador][25]-c24)**2)+((dataset[contador][26]-c25)**2)+((dataset[contador][27]-c26)**2)+((dataset[contador][28]-c27)**2)+((dataset[contador][29]-c28)**2)+((dataset[contador][30]-c29)**2)+((dataset[contador][31]-c30)**2)+((dataset[contador][32]-c31)**2)+((dataset[contador][33]-c32)**2)+((dataset[contador][34]-c33)**2)+((dataset[contador][35]-c34)**2)+((dataset[contador][36]-c35)**2)+((dataset[contador][37]-c36)**2)+((dataset[contador][38]-c37)**2)+((dataset[contador][39]-c38)**2)+((dataset[contador][40]-c39)**2)+((dataset[contador][41]-c40)**2)+((dataset[contador][42]-c41)**2)+((dataset[contador][43]-c42)**2)+((dataset[contador][44]-c43)**2)+((dataset[contador][45]-c44)**2)+((dataset[contador][46]-c45)**2)+((dataset[contador][47]-c46)**2)#Formula para obtener la distancia Euclidiana (Part1)
  raiz=math.sqrt(euclidianaTemp)#Se obtiene la raiz cuadrada de la sumatoria anterior
  dataset[contador].append(raiz)#agregamos una nueva columna a nuestro dataset para guardar la distancia obtenida entre el elemento de prueba y la instancia actual  
  contador+=1#Incrementamos un número al contador
dataset.sort(key=lambda dataset: dataset[48])#Ordenamos de menor a mayor las distancias 
for i in range(0,k):#ciclo for para imprimir cada uno de los vecinos mas cercanos (de 0 al número K)
    print('Neighbor: '+str(i+1)+ '\nDistancia: '+str(dataset[i][48])+'\nClase: '+dataset[i][1]+'\nInstancia: '+dataset[i][0]+'\n')#impresión en pantalla de la información de cada vecino mas cercano
    vecinos=[]#Se declara una lista para almacenar los 11 vecinos mas cercanos
    circulo=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    cuadrado=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    elipseHorizontal=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    elipseVertical=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    estrella=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    linea=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    paralelogramoDerecha=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    paralelogramoIzquierda=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    rectanguloHorizontal=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    rectanguloVertical=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    rombo=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    trapecio=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    trianguloAbajo=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    trianguloArriba=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    trianguloDerecha=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
    trianguloIzquierda=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
for i in range(0,k):#ciclo para recorrer a los primeros K vecinos mas cercanos
  if(dataset[i][1]=='circulo'):#condición para saber si el vecino (i) es circulo
    circulo+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='cuadrado'):#condición para saber si el vecino (i) es cuadrado
    cuadrado+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='elipseHorizontal'):#condición para saber si el vecino (i) es elipseHorizontal
    elipseHorizontal+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='elipseVertical'):#condición para saber si el vecino (i) es elipseVertical
    elipseVertical+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='estrella'):#condición para saber si el vecino (i) es estrella
    estrella+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='linea'):#condición para saber si el vecino (i) es linea
    linea+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='paralelogramoDerecha'):#condición para saber si el vecino (i) es paralelogramoDerecha
    paralelogramoDerecha+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='paralelogramoIzquierda'):#condición para saber si el vecino (i) es paralelogramoIzquierda
    paralelogramoIzquierda+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='rectanguloHorizontal'):#condición para saber si el vecino (i) es rectanguloHorizontal
    rectanguloHorizontal+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='rectanguloVertical'):#condición para saber si el vecino (i) es rectanguloVertical
    rectanguloVertical+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='rombo'):#condición para saber si el vecino (i) es rombo
    rombo+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='trapecio'):#condición para saber si el vecino (i) es trapecio
    trapecio+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='trianguloAbajo'):#condición para saber si el vecino (i) es trianguloAbajo
    trianguloAbajo+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='trianguloArriba'):#condición para saber si el vecino (i) es trianguloArriba
    trianguloArriba+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='trianguloDerecha'):#condición para saber si el vecino (i) es trianguloDerecha
    trianguloDerecha+=1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='trianguloIzquierda'):#condición para saber si el vecino (i) es trianguloIzquierda
    trianguloIzquierda+=1#en ese caso se incrementa una unidad al contador del caracter  
vecinos.append(['Circulo',circulo])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Cuadrado',cuadrado])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Elipse Horizontal',elipseHorizontal])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Elipse Vertical',elipseVertical])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Estrella',estrella])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Linea',linea])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Paralelogramo Derecha',paralelogramoDerecha])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Paralelogramo Izquierda',paralelogramoIzquierda])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Rectangulo Horizontal',rectanguloHorizontal])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Rectangulo Vertical',rectanguloVertical])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Rombo',rombo])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Trapecio',trapecio])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Triangulo hacia Abajo',trianguloAbajo])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Triangulo hacia Arriba',trianguloArriba])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Triangulo hacia la Derecha',trianguloDerecha])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
vecinos.append(['Triangulo hacia la Izquierda',trianguloIzquierda])#se añade a la lista "vecinos" dos campos, (la clase y el valor total del contador de dicha letra o número)
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°Cant. Neighbors °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n')#impresion de pantallas
print(vecinos)#se imprime la lista vecinos con la cantidad correspondiente de clases y cantidad de instancias cercanas con respecto al elemento de prueba 
print('\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n')#impresion de pantallas
vecinos.sort(key=lambda  vecinos: vecinos[1], reverse=True)#se ordena de menor a mayor la lista vecinos para saber que clase es la imagen, de acuerdo a la función mayoria  
print('                        De acuerdo a la función mayoría el elemento de prueba pertenece a la clase '+str(vecinos[0][0]))#impresión final de la clasificación
print('\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n')#impresion de pantallas