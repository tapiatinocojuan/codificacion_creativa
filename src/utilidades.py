import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
import py5
import os
import moviepy.video.io.ImageSequenceClip
from glob import glob
from os import remove, path

class MplColorHelper:

  def __init__(self, cmap_name, start_val, stop_val):
    self.cmap_name = cmap_name
    self.cmap = plt.get_cmap(cmap_name)
    self.norm = mpl.colors.Normalize(vmin=start_val, vmax=stop_val)
    self.scalarMap = cm.ScalarMappable(norm=self.norm, cmap=self.cmap)

  def get_rgb(self, val):
    return self.scalarMap.to_rgba(val)
  
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

def punto_medio(p0, p1):
    """Dados 2 puntos calcula el punto medio"""
    x0, y0 = p0
    x1, y1 = p1
    xm = (x0 + x1)/2
    ym = (y0 + y1)/2

    return (xm, ym)

def ecuacion_recta(p0, p1, modo=0):
    """Dados 2 puntos se calcula la ecuacion de la recta que los une
    
    Parameters
    p0: tuple
        Par de coordenadas para el punto 0 (x0, y0)
    p1: tuple
        Par de coordenadas para el punto 1 (x1, y1)
    modo: int
        En modo 0 regresa las coordenadas de dos puntos de la recta perpendicular,
        en modo 1 regresa los factores m y b de la ecuacion de la recta perpendicular
        y la funcion anonima de la misma recta.
    """
    x0, y0 = p0
    x1, y1 = p1

    #Si la recta original es una recta horizontal
    if abs(y1 - y0) < 0.00001:
        return 0, y0, lambda x: y0
    
    #Si la recta original es una recta vertical
    if abs(x1 - x0) < 0.00001:
        return None, x0, None 
    
    m = (y1 - y0)/(x1 - x0)
    b = -m*x1 + y1
    func = lambda x: m*x + b
    return m, b, func

def recta_perpendicular(p0, p1, modo=0):
    """Dados 2 puntos se calculan dos puntos para una recta perpendicular
    
    Parameters
    p0: tuple
        Par de coordenadas para el punto 0 (x0, y0)
    p1: tuple
        Par de coordenadas para el punto 1 (x1, y1)
    modo: int
        En modo 0 regresa las coordenadas de dos puntos de la recta perpendicular,
        en modo 1 regresa los factores m y b de la ecuacion de la recta perpendicular
        y la funcion anonima de la misma recta.
    """
    x0, y0 = p0
    x1, y1 = p1
    xm, ym = punto_medio(p0, p1)

    #Si la recta original es una recta horizontal
    if abs(y1 - y0) < 0.00001:
        if modo == 0:
            return ((xm, y0 + (xm - x0)), (xm, y0-(xm-x0)))
        elif modo == 1:
            return None, xm, None
    
    #Si la recta original es una recta vertical
    if abs(x1 - x0) < 0.00001:
        if modo == 0:
            return ((x0 + (ym - y0), ym), (x0 - (ym - y0), ym))
        elif modo == 1:
            return 0, ym, lambda x: ym 
    
    m = (y1 - y0)/(x1 - x0)
    m_inv = -1/m
    const = -m_inv*xm + ym 
    func = lambda x: m_inv*x + const 

    if modo == 0:
        return ((x0, func(x0)), (x1, func(x1)))
    elif modo == 1:
        return m_inv, const, func

def calcula_circulo_circunscrito(pts):
    """ Dados 3 puntos se calcula el centro del circulo 
    circunscrito de un triangulo"""

    revisar_colinealidad(pts)
    p0, p1, p2 = pts
    m1, b1, func1 = recta_perpendicular(p1, p0, modo=1)
    m2, b2, func2 = recta_perpendicular(p1, p2, modo=1)

    if m1 == m2 and b1 == b2:
        raise Exception("Rectas colineales no pueden ser un triangulo")

    if m1 == None:
        xc, yc = (b1, func2(b1))
    elif m2 == None:
        xc, yc = (b2, func1(b2))
    else:
        xc = (b2-b1)/(m1-m2)
        yc = func1(xc)

    r = calcular_distancia((xc, yc), p0)
    return (xc, yc, r)

def revisar_colinealidad(pts):
    """Revisa si los puntos de un triangulo son colineales"""
    p0, p1, p2 = pts
    m1, b1, func1 = ecuacion_recta(p1, p0)
    m2, b2, func2 = ecuacion_recta(p1, p2)

    if m1 == m2  and b1 == b2:
        raise Exception("Los puntos son colineales")
    

def calcular_distancia(p0, p1):
    """Calcula la distancia entre dos puntos"""
    delta_x = p1[0] - p0[0]
    delta_y = p1[1] - p0[1]
    return  ((delta_x)**2 + (delta_y)**2)**0.5

def calcular_hipotenusa(w, h):
    """Calcula la hipotenusa de una trinagulo rectangulo"""
    return  ((w)**2 + (h)**2)**0.5


def get_colors_4_colormap(colormap):
    """Genera una lista de 256 colores a partir de un colormap"""
    COL = MplColorHelper(colormap, 0, 255)
    return [COL.get_rgb(i) for i in range(256)]

def create_video(image_folder, fps, file_name):
    """Crea un video a partir de archivos png"""
    image_files = [os.path.join(image_folder,img)
                for img in os.listdir(image_folder)
                if img.endswith(".png")]
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile(os.path.join(image_folder, f"{file_name}.mp4"))

def remove_png(dirname):
    """Borra todos los archivos png de una carpeta"""
    for file in glob(path.join(dirname, "*.png")):
        try:
            remove(file)
        except:
            pass
    
def defasar(lista):
    """Mueve el primer elemento de una lista al final"""
    val = lista.pop(0)
    lista.append(val)
    return lista