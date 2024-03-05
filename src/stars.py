"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear estrellas.
"""
import py5
import utilidades
from paleta_colores import colormap3
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png
i = 0
colores = utilidades.get_colors_4_colormap(py5.random_choice(colormap3))
num_estrellas = 100
num_puntas = 10
relacion = 0.7
ancho = None
fps = 15

def setup():
    global ancho, fps
    py5.size(980, 980)
    py5.background(0)
    ancho = py5.width/2
    py5.frame_rate(fps)
    

def draw():    
    global i, num_estrellas, num_puntas, ancho, colores
    factor = decrecimiento(i/num_estrellas)
    r, g, b, alpha = colores[int(255*factor)]
    py5.fill(r*255, g*255, b*255, 255-255*factor)
    pts = star(
        py5.width/2, py5.height/2, ancho*factor, 
        ancho*factor*relacion, num_puntas, 
        py5.PI/num_puntas*i%2
    )
    draw_shape(pts)
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    i += 1
    if i == num_estrellas:
        colores = utilidades.get_colors_4_colormap(py5.random_choice(colormap3))
        i = 0



def decrecimiento(x):
    """Funcion cuadratica de decrecimiento"""

    if x<0:
        return 1
    if x>1:
        return 0
    return -x**2 + 1


def draw_shape(pts):
    """Dibuja una figura cerrada a partir de los puntos en pts"""
    py5.begin_shape()
    for x, y in pts:
        py5.vertex(x, y)
    py5.end_shape(py5.CLOSE)

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


if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "stars")
    remove_png(RUTA)