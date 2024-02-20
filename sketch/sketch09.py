"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear imagen por medio de grafos.
"""
import py5
import utilidades
import networkx as nx
import paletas_colores

WMIN = 10
HMIN = 10
s = 1
save_file = True

def setup():
    global WMIN, HMIN
    py5.size(980, 980)
    py5.background(255)
    WMIN = py5.width/20
    HMIN = py5.height/20
    py5.no_loop()

def draw():
    global save_file, s
    if save_file: 
        py5.begin_record(py5.SVG, f"grafos.svg")
    py5.background(255)
    x_off = 50
    y_off = 50
    w = py5.width - 2*x_off
    h = py5.height - 2*y_off
    n = 30
    colores = utilidades.get_colors_4_colormap("autumn")
    #colores = paletas_colores.paleta_sailor_moon
    for _ in range(50):
        ramas(x_off, y_off, w, h, n, colores)
    if save_file:    
        py5.end_record()

def ramas(x_off, y_off, w, h, n, colores):
    global WMIN, HMIN
    if w < WMIN or h < HMIN:
        return
    pts = calcular_pts_ordenados2(x_off, y_off, w, h, n)
    step = (w*h/n)**0.5
    #draw_line(pts, step*1.5)
    edges = crear_grafo(pts)
    dibujar_grafo(pts, edges, colores, w, h)
    # for pt in pts:
    #     if py5.random_int(1,3) == 1:
    #         new_w = w/10
    #         new_h = h/10
    #         new_n = n//10
    #         new_x_off = pt[0] - new_w*0.5 
    #         new_y_off = pt[1] - new_h*0.5 
    #         ramas(new_x_off, new_y_off, new_w, new_h, new_n, colores)        

def calcular_pts(x_off, y_off, w, h, n):
    return [
        (py5.random(x_off, x_off + w), 
         py5.random(y_off, y_off + h)) for _ in range(n)
    ]

def calcular_pts_ordenados(x_off, y_off, w, h, n):
    pts = []
    step = (w*h/n)**0.5
    nx = round(w/step) 
    ny = round(h/step) 
    for i in range(nx):
        for j in range(ny):
            pts.append((x_off + i*step + step/2, y_off + j*step + step/2))
    return pts

def calcular_pts_ordenados2(x_off, y_off, w, h, n):
    pts = []
    step = (w*h/n)**0.5
    nx = round(w/step) 
    ny = round(h/step) 
    for i in range(nx):
        for j in range(ny):
            pts.append(
                (py5.random(x_off + i*step, x_off + (i+1)*step),
                 py5.random(y_off +j*step, y_off + (j+1)*step)
                )
            )
    return pts

def dibujar_grafo(pts, edges, colores, w, h):
    d = utilidades.calcular_hipotenusa(w, h)
    color_idx = py5.random_int(len(colores)-1)
    r, g, b, _ = colores[color_idx]
    py5.stroke(r*255, g*255, b*255)
    py5.fill(r*255, g*255, b*255)
    for p1, p2, _ in edges:
        py5.line(pts[p1][0],pts[p1][1], pts[p2][0], pts[p2][1] )
    for cx, cy in pts:
        r = min(w, h)/100
        py5.circle(cx, cy, r)
    
def crear_grafo(pts):
    G = nx.Graph()
    for pt in pts:
        G.add_node(pt)    
    for i, pt_a in enumerate(pts):
        for j, pt_b in enumerate(pts[i+1:]):
            G.add_edge(i, j+i+1, weight=utilidades.calcular_distancia(pt_a, pt_b))
    T = nx.minimum_spanning_tree(G)
    return sorted(T.edges(data=True))

def draw_line(pts, r_max):
    py5.stroke("#000000")
    for i, pt_a in enumerate(pts):
        for j, pt_b in enumerate(pts[i+1:]):
            r = utilidades.calcular_distancia(pt_a, pt_b)
            print(r)
            if r < r_max:
                py5.line(pt_a[0], pt_a[1], pt_b[0], pt_b[1])
            


    
def mouse_pressed():
    global s
    s += 1
    print(s)
    py5.redraw()

def key_pressed():
    global save_file
    save_file = True

def mouse_wheel():
    global s
    if s > 0:
        s -= 1
        print (s)

if __name__ == "__main__":
    py5.run_sketch()