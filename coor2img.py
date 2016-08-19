#programa que convierte un archivo de coordenadas.txt en una imagen bmp
from resources import trayectorias#se importa la libreria trayectorias desde la carpeta resources
from PIL import Image#libreria para abrir la imagen y poder procesarla
import matplotlib.pyplot as plt#libreria para mostrar la imagen mediante un plot
puntos = trayectorias.puntosFromJson('coordenadas.txt')#libreria para abrir la imagen y poder obtener sus caracteristicas
imagen = trayectorias.puntos2matrizConectada(puntos)#se convierten los puntos en una imagen conectada
img=Image.fromarray(255*imagen)#se crea img a partir de array "imagen"
plt.imshow(img)#se grafica la imagen
img.save('./test/test.bmp')#se guarda la imagen dentro de la carpeta test, con el nombre test.bmp