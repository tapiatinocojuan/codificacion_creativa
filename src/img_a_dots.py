""""Codigo para remplazar pixeles con glifos en imagenes
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""
import py5
from PIL import Image
import numpy as np
imagen_path = 'DATA/escala_grises.png'
im = Image.open(imagen_path)
factor_escala = 0.3 #Imagenes grande
2
import sys
from os import path
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))

def setup():
    global img, pixeles
    py5.size(im.size[0], im.size[1])
    py5.background(0)
    img = py5.load_image(imagen_path)
    img.load_np_pixels()
    pixels = img.np_pixels
    pixeles = np.zeros((py5.width, py5.height))
    for i, row in enumerate(pixels):
        for j, cell in enumerate(row):
            alpha, red, green, blue  = cell
            lum = 0.2126*red/255 + 0.7152*green/255 + 0.0722*blue/255
            lum = lum*alpha/255
            pixeles[j][i] = (lum)
    pixeles = promediar_matriz(pixeles, factor_escala)


def draw():
    global img, pixeles
    py5.begin_record(py5.SVG, f"DATA/{path.basename(imagen_path).split(".")[0]}.svg")
    py5.scale(1/factor_escala)
    py5.text_align(py5.CENTER)
    py5.no_stroke()
    py5.fill("#FFFFFF")
    for i, renglon in enumerate(pixeles):
        for j, cell in enumerate(renglon):        
            try:
                py5.circle(i, j, py5.remap(cell, 0, 1, 0.1, 1))
            except:
                import pdb; pdb.set_trace()
    py5.end_record()
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    py5.no_loop()

def get_gliph(valor):
    global simbolos
    
    if valor <= simbolos[0][1]:
        return chr(simbolos[0][0])
    if valor >= simbolos[-1][1]:
        return chr(simbolos[-1][0])
    for i, ( _, threshold) in enumerate(simbolos):
        if valor < threshold:
            return chr(simbolos[i-1][0])


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


