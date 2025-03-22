""""Codigo para remplazar pixeles con glifos en imagenes
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""
import py5
from PIL import Image
import numpy as np
imagen_path = 'DATA/sandy.png'
im = Image.open(imagen_path)
factor_escala = 0.1 #Imagenes grande
factor_escala = 0.05
noise_scale = 0.005
noise_angle = py5.TWO_PI
import sys
from os import path
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))

def setup():
    global img, pixeles
    py5.size(im.size[0], im.size[1])
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
    pixeles = promediar_matriz(pixeles, factor_escala)

def draw():
    global img, pixeles, font
    py5.begin_record(py5.SVG, "DATA/sandy_rectangulos.svg")
    py5.background(0)
    py5.scale(1/factor_escala)
    py5.no_stroke()
    py5.fill("#FFFFFF")
    py5.rect_mode(py5.CENTER)
    for i, renglon in enumerate(pixeles):
        for j, cell in enumerate(renglon):        
            try:
                py5.push_matrix()
                py5.translate(i+0.5, j+0.5)
                py5.rotate(noise_angle *py5.noise(noise_scale*i, noise_scale*j))
                py5.rect(0, 0, 0.9, py5.remap(cell, 0, 1, 0.15, 0.9))
                py5.pop_matrix()
            except Exception as err:
                import pdb; pdb.set_trace()
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


