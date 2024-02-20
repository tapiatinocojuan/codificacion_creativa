"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para probar aletoriedad.
"""

import py5
import utilidades
import networkx as nx

def setup():
    py5.size(980, 980)
    py5.background(255)

    for x in range(50, 930, 50):
        r = 0
        g = py5.random_int(128, 255)
        b = 128
        py5.fill (r, g, b)
        py5.circle(x, 450, 45)
    
    colores = [
        py5.color(255, 200, 0),
        py5.color(0, 128, 255),
        py5.color(128, 255, 0),
    ]
    for x in range(50, 930, 50):
        py5.fill (py5.random_choice(colores))
        py5.circle(x, 550, 45)
    
    py5.fill(0)
    for x in range(50, 930, 100):
        n = py5.random_int(3, 7)
        r = py5.random_choice((10, 25, 40))
        pts = utilidades.star(x, 700, r, 50, n)
        utilidades.draw_shape(pts)



if __name__ == "__main__":
    py5.run_sketch()