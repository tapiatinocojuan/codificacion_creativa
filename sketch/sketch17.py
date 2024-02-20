"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear mozaico con puntos aleatorios.
"""
import py5
import utilidades
import networkx as nx
from paletas_colores import colormap, paleta_noche_estrellada

s = 11
save_file = True
class Punto():
    """Clase para almacenar las coordenadas de un punto"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Coordenadas {self.x}, {self.y}"


def setup():
    #py5.size(742, 300)
    py5.size(800, 800)
    py5.background(255)
    py5.no_loop()

def draw():
    global s, save_file
    py5.random_seed(s)
    py5.background("#FFFFFF")
    if save_file:
        py5.begin_record(py5.SVG, 'taza.svg')
    colores = utilidades.get_colors_4_colormap(py5.random_choice(colormap))
    #colores = paleta_noche_estrellada
    crear(colores)
    if save_file:
        py5.end_record()
        save_file = False

def crear(colores):
    nx = 15
    ny = 15
    x_off = 0
    y_off = 0
    pts = calcular_puntos(py5.width, py5.height, nx, ny, x_off, y_off)
    recorrer_ventana(pts, dibujar_triangulos, colores)

    puntos = []
    for row in pts:
        puntos += row
    edges = crear_grafo(puntos)
    dibujar_grafo(puntos, edges, [(0, 0, 0, 0)], py5.width, py5.height)


def calcular_puntos(w, h, nx, ny, x_off, y_off):
    """Funcion para calcular puntos distribuidos en una malla
    con variaciones aleatorias.
    
    El area se divide en n * n secciones y en cada una de ellas
    se obtiene un punto semialeatorio.
    """
    step_x = w/nx
    step_y = h/ny
    out = []
    py5.no_stroke()
    for i in range(nx):
        row = []      
        for j in range(ny):
            row.append(
                Punto(
                    py5.random(x_off + i*step_x, x_off + (i+1)*step_x),
                    py5.random(y_off + j*step_y, y_off + (j+1)*step_y),
                )
                
            )
        out.append(row)
    return out

def recorrer_ventana(pts, func, colores=[]):
    """Funcion para recorrer la matriz de puntos en ventanas de 2 x 2.
    La submatriz es enviada como argumento a la funcion almacenada en 
    func"""
    rows = len(pts)
    cols = len(pts[0])
    for i in range(rows - 1):
        for j in range(cols - 1):
            window = [
                [pts[i][j], pts[i+1][j]], 
                [pts[i][j+1], pts[i+1][j+1]]
            ]
            func(window, colores)

def dibujar_triangulos(pts, colores=[]):
    py5.no_stroke()
    if colores:
        r, g, b, _ = py5.random_choice(colores)
        py5.fill(r*255, g*255, b*255, 180)
    pt1 = pts[0][0]
    pt2 = pts[1][0]
    pt3 = pts[0][1]
    pt4 = pts[1][1]
    if py5.random_int(0, 1):
        py5.begin_shape()
        py5.vertex(pt1.x, pt1.y)
        py5.vertex(pt2.x, pt2.y)
        py5.vertex(pt3.x, pt3.y)
        py5.end_shape(py5.CLOSE)

        py5.begin_shape()
        py5.vertex(pt2.x, pt2.y)
        py5.vertex(pt3.x, pt3.y)
        py5.vertex(pt4.x, pt4.y)
        py5.end_shape(py5.CLOSE)
    else:
        py5.begin_shape()
        py5.vertex(pt1.x, pt1.y)
        py5.vertex(pt2.x, pt2.y)
        py5.vertex(pt4.x, pt4.y)
        py5.end_shape(py5.CLOSE)

        py5.begin_shape()
        py5.vertex(pt1.x, pt1.y)
        py5.vertex(pt3.x, pt3.y)
        py5.vertex(pt4.x, pt4.y)
        py5.end_shape(py5.CLOSE)


def crear_grafo(pts):
    G = nx.Graph()
    for pt in pts:
        G.add_node(pt)   
    for i, pt_a in enumerate(pts):
        for j, pt_b in enumerate(pts[i+1:]):
            G.add_edge(i, j+i+1, weight=utilidades.calcular_distancia((pt_a.x, pt_a.y), (pt_b.x, pt_b.y)))
    T = nx.minimum_spanning_tree(G)
    return sorted(T.edges(data=True))

def dibujar_grafo(pts, edges, colores, w, h):
    r, g, b, _ = py5.random_choice(colores)
    py5.stroke(r*255, g*255, b*255)
    py5.fill(r*255, g*255, b*255)
    for p1, p2, _ in edges:
        py5.line(pts[p1].x,pts[p1].y, pts[p2].x, pts[p2].y )
    for pt in pts:
        r = min(w, h)/200
        py5.circle(pt.x, pt.y, r)

def mouse_pressed():
    global s
    s += 1

    py5.redraw()

def key_pressed():
    global save_file
    save_file = True

def mouse_wheel():
    global s
    if s > 0:
        s -= 1
    py5.redraw()

if __name__ == '__main__':
    py5.run_sketch()