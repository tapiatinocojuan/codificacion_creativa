"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para probar uso de condicionales
"""

import py5
import utilidades
import networkx as nx

def setup():
    py5.size(980, 980)
    py5.fill(0)
    py5.no_stroke()
    py5.rect_mode(py5.CENTER)

    for x in range(80, 930, 100):
        v = py5.random_int(1, 7)
        if v == 1:
            py5.circle(x, 450, 50)
        elif v == 2:
            py5.square(x, 450, 50)
        else:
            r = py5.random_choice((10,25,40))
            pts = utilidades.star(x, 450, r, 30, v)
            utilidades.draw_shape(pts)
    
if __name__ == "__main__":
    py5.run_sketch()