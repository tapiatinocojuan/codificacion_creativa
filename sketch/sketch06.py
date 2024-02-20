"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear triangulos.
"""
import py5
import utilidades

def setup():
    py5.size(980, 980)
    py5.background(0)
    COL = utilidades.MplColorHelper('inferno_r', 0, 255)
    colores = [COL.get_rgb(i) for i in range(256)]
    for i in range(20):
        #dibuja_triangulos(py5.random_int(py5.width), py5.random_int(py5.height), 200)
        dibuja_triangulos(py5.width/2, py5.height/2, 100, colores)

def dibuja_triangulos(x, y, n, colores):
    triangulos = n
    max_r = py5.width/10
    min_r = py5.width/100
    
    cx = py5.width/2
    cy = py5.height/2
    pts = utilidades.polygon(
            x, y, 
            py5.random(min_r, max_r), 3, 0
    )
    r, g, b, alpha = py5.random_choice(colores)
    py5.fill(r*255, g*255, b*255, 80)
    utilidades.draw_shape(pts)
    pts = list(pts)
    for i in range(triangulos):
        #factor = utilidades.decrecimiento(i/estrellas)
        xm, ym = utilidades.punto_medio(pts[1], pts[2])
        r, g, b, alpha = py5.random_choice(colores)
        py5.fill(r*255, g*255, b*255, 150)
        pts.pop(0)
        pts.append(
            (py5.random(xm - max_r, xm + max_r), 
             py5.random(ym - max_r, ym + max_r) )
        )
        utilidades.draw_shape(pts)


if __name__ == "__main__":
    py5.run_sketch()