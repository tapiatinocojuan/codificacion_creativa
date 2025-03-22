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
noise_angle = 360
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
    py5.begin_record(py5.SVG, "DATA/sandy_polygons.svg")
    py5.background(0)
    py5.scale(1/factor_escala)
    py5.no_stroke()
    py5.fill("#FFFFFF")
    for i, renglon in enumerate(pixeles):
        for j, cell in enumerate(renglon):        
            try:
                draw_shape(
                    star(
                        i+0.5, j+0.5, r_int = py5.remap(cell, 0, 1, 0.1, 0.5), 
                        r_ext=0.5, n=int(py5.remap(cell, 0, 1, 3, 10)), 
                        alpha=noise_angle *py5.noise(noise_scale*i, noise_scale*j)
                    )
                )
            except Exception as err:
                import pdb; pdb.set_trace()
    py5.end_record()
    py5.no_loop()

def star(cx, cy, r_int, r_ext, n=3, alpha=0):
    """Calcula los vertices de una estrella con centro en cx y cy, 
    radio interior rint, radio exterior rext n lados y girado 
    alpha grados
    
    Parameters
    ----------
    cx: int
        Coordenada x del centro del poligono
    cy: int 
        Coordenada y del centro del poligono
    r_int: int
        Radio interior de la estrella
    r_ext: int
        Radio exterior de la estrella
    n: int
        Numero de lados del poligino
    apha: float
        Rotación del poligono en radianes
    """
    pts_int = polygon(cx, cy, r_int, n=n, alpha=alpha)
    pts_ext = polygon(cx, cy, r_ext, n=n, alpha=py5.TWO_PI/(2*n) + alpha)
    pts = []
    for pt_int, pt_ext in zip(pts_int, pts_ext):
        pts.append(pt_int)
        pts.append(pt_ext)
    return pts

def polygon(cx, cy, r, n=3, alpha=0):
    """Calcula los lados de un poligono con centro en cx y cy, radio r, 
    n lados y girado alpha grados
    
    Parameters
    ----------
    cx: int
        Coordenada x del centro del poligono
    cy: int 
        Coordenada y del centro del poligono
    r: int
        Radio del poligono
    n: int
        Numero de lados del poligino
    apha: float
        Rotación del poligono en radianes
    """
    pts = []
    step = py5.TWO_PI/n
    for i in range(n):
        theta = i * step
        pts.append(
            (cx + r * py5.sin(theta+alpha),
             cy + r * py5.cos(theta+alpha)
            ),
        )
    return pts

def draw_shape(pts):
    """Dibuja una figura cerrada a partir de los puntos en pts"""
    py5.begin_shape()
    for x, y in pts:
        py5.vertex(x, y)
    py5.end_shape(py5.CLOSE)

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


