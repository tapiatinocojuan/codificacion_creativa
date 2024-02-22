"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear mozaico con puntos aleatorios.
"""
import py5
import utilidades
import networkx as nx
from paleta_colores import colormap, colormap2
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png
from create_letter import dibujar_letra

s = 1; i = 0; j = 0; radio = 0; count = 0; i_color = 0
pts = None; edges = None; colores = None; rows = None; cols = None; puntos = None
puntos_flg = False; triangulos_flg = True; grafo_flg = False; circulo_flg = False
color = False; diagonal = None
fps = 60

class Punto():
    """Clase para almacenar las coordenadas de un punto"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Coordenadas {self.x}, {self.y}"

def setup():
    global pts, edges, s, colores, rows, cols, puntos, diagonal, fps
    py5.size(800, 800)
    py5.background(255)
    py5.frame_rate(fps)
    #py5.random_seed(s)
    py5.background("#FFFFFF")
    #colores = utilidades.get_colors_4_colormap(py5.random_choice(colormap))
    colores = utilidades.get_colors_4_colormap(colormap2[i_color])
    
    pts, edges, puntos = calcular()
    cols = len(pts)
    rows = len(pts[0])
    diagonal = (py5.width**2 + py5.height**2)**0.5 * 2.5

def draw():
    global pts, edges, s, colores, rows, cols, i, j, color, radio, diagonal
    global puntos_flg, triangulos_flg, grafo_flg, circulo_flg, count, i_color

    py5.push_matrix()
    if count % 4 == 0:
        pass
    if count % 4 == 1:
        py5.translate(py5.width, 0)
        py5.rotate(py5.HALF_PI)
    elif count % 4 == 2: 
        py5.translate(py5.width, py5.height)
        py5.rotate(py5.PI)
    elif count % 4 == 3: 
        py5.translate(0, py5.height)
        py5.rotate(py5.PI + py5.HALF_PI)
        

    py5.stroke(color * 255)
    py5.fill(color * 255)
    
    if triangulos_flg:
        if  i >= rows -1:
            triangulos_flg = False
            puntos_flg = True
            i = rows - 1
            j = cols - 1
            py5.pop_matrix()
            return
        window = [
            [pts[i][j], pts[i+1][j]], 
            [pts[i][j+1], pts[i+1][j+1]]
        ]
        dibujar_triangulos(window, colores)
        j += 1
        if j >= cols -1:
            j = 0
            i += 1
    elif puntos_flg:
        if  i < 0:
            puntos_flg = False
            grafo_flg = True
            i = 0
            j = 0
            py5.pop_matrix()
            return
        pt = pts[i][j]
        r = min(py5.width, py5.height)/200
        py5.circle(pt.x, pt.y, r)
        j -= 1
        if j < 0:
            j = cols - 1 
            i -= 1
    elif grafo_flg:
        if i >= len(edges):
            grafo_flg = False
            circulo_flg = True
            i = 0
            j = 0
            py5.pop_matrix()
            return
        pta = puntos[edges[i][0]]
        ptb = puntos[edges[i][1]]
        py5.line(pta.x,pta.y, ptb.x, ptb.y )
        i += 1
    elif circulo_flg:
        py5.fill(255*color, 20)
        py5.push_matrix()
        py5.translate(py5.width, py5.height)
        py5.circle(0, 0, radio)
        py5.pop_matrix()
        radio += py5.width/20
        if radio > (diagonal):
            circulo_flg = False
            i = 0
            j = 0
            radio = 0
    else:
        i_color +=  1
        colores = utilidades.get_colors_4_colormap(colormap2[i_color%6])
        triangulos_flg = True
        puntos_flg = False
        grafo_flg = False
        circulo_flg_flg = False
        color = not color
        count += 1
        py5.translate(py5.width, 0)
        py5.rotate(py5.HALF_PI)
        py5.redraw()
    py5.pop_matrix()
    dibujar_letra(0, 0, py5.width, py5.height, "S", "#000000")
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")

def calcular():
    nx = 20
    ny = 20
    x_off = 0
    y_off = 0
    pts = calcular_puntos(py5.width, py5.height, nx, ny, x_off, y_off)
    puntos = []
    for row in pts:
        puntos += row
    edges = crear_grafo(puntos)
    return pts, edges, puntos
    
def calcular_puntos(w, h, nx, ny, x_off, y_off):
    """Funcion para calcular puntos distribuidos en una malla
    con variaciones aleatorias.
    
    El area se divide en n * n secciones y en cada una de ellas
    se obtiene un punto semialeatorio.
    """
    step_x = w/nx
    step_y = h/ny
    out = []
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

def dibujar_triangulos(pts, colores=[]):
    global color
    py5.stroke((not color) * 255)
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
        r, g, b, _ = py5.random_choice(colores)
        py5.fill(r*255, g*255, b*255, 180)
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
        r, g, b, _ = py5.random_choice(colores)
        py5.fill(r*255, g*255, b*255, 180)
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
            weight = utilidades.calcular_distancia((pt_a.x, pt_a.y), (pt_b.x, pt_b.y))
            G.add_edge(i, j+i+1, weight=weight)
    T = nx.minimum_spanning_tree(G)
    return sorted(T.edges(data=True))


if __name__ == '__main__':
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "mozaico_triangulos_letra_s")
    remove_png(RUTA)