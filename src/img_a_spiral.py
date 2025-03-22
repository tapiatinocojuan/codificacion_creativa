""""Codigo para remplazar pixeles con glifos en imagenes
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""
import py5
from PIL import Image
import numpy as np
imagen_path = 'DATA/sandy2.png'
im = Image.open(imagen_path)
factor_escala = 0.1 #Imagenes grande
factor_crecimiento = 0.0025
factor_angulo = 0.2
factor_reduccion_velocidad = 0.95
#noise_scale = 0.005
#noise_angle = py5.TWO_PI
import sys
from os import path
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))

def setup():
    global img, pixeles, xc, yc
    py5.size(im.size[0], im.size[1])
    py5.background(0)
    xc = py5.width/2
    yc = py5.height/2
    img = py5.load_image(imagen_path)
    img.load_np_pixels()
    pixels = img.np_pixels
    pixeles = np.zeros((py5.width, py5.height))
    for i, row in enumerate(pixels):
        for j, cell in enumerate(row):
            alpha, red, green, blue  = cell
            lum = 0.2126*red/255 + 0.7152*green/255 + 0.0722*blue/255
            lum = lum*alpha/255
            pixeles[j][i] = lum
    #pixeles = promediar_matriz(pixeles, factor_escala)


def draw():
    global xc, yc, pixeles, delta_angulo, factor_crecimiento
    py5.begin_record(py5.SVG, "DATA/sandy2_spiral.svg")
    py5.background(0)
    py5.no_stroke()
    py5.fill("#ffffff")
    cont = 0
    angulo  = 1
    radio = 1
    while True:
        x = xc + radio*py5.sin(angulo*py5.DEG_TO_RAD)
        y = yc + radio*py5.cos(angulo*py5.DEG_TO_RAD)
        try:
            py5.circle(x, y, py5.remap(pixeles[int(x)][int(y)],0,1, 2,5))
        except:
            break
        cont += 1
        delta_angulo = radio/(radio + cont*factor_crecimiento)*factor_angulo
        angulo += delta_angulo
        radio = cont * factor_crecimiento

    py5.end_record()
    py5.no_loop()

def promediar_matriz(matriz, factor):
    x_size = len(matriz)
    y_size = len(matriz[0])
    paso_x = int(1/factor)
    paso_y = int(1/factor)
    new_size_x = x_size//paso_x
    new_size_y = y_size//paso_y
    new_matriz = np.zeros((new_size_x, new_size_y))
    for i in range(new_size_x):
        for j in range(new_size_y):
            new_matriz[i][j] = np.average(matriz[paso_x*i:paso_x*(i+1), paso_y*j:paso_y*(j+1)])
    return new_matriz    



if __name__ == "__main__":
    py5.run_sketch()    


