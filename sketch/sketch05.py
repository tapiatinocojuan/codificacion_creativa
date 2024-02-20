"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear estrellas.
"""
import py5
import utilidades

def setup():
    py5.size(980, 980)
    py5.background(0)
    puntas=10
    estrellas = 100
    ancho = py5.width/2
    relacion = 0.7   
    #py5.no_stroke()
    COL = utilidades.MplColorHelper('hsv_r', 0, 255)
    for i in range(estrellas):
        factor = decrecimiento(i/estrellas)
        r, g, b, alpha = COL.get_rgb(255*factor)
        py5.fill(r*255, g*255, b*255, 255-255*factor)
        pts = star(
            py5.width/2, py5.height/2, ancho*factor, 
            ancho*factor*relacion, puntas, 
            py5.PI/puntas*i%2
        )
        draw_shape(pts)


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
    py5.run_sketch()