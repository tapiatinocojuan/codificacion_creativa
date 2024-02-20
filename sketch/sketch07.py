"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear rectas paralelas.
"""
import py5
import utilidades

def setup():
    py5.size(980, 980)
    p0 =200, 0
    p1 =200, 200

    p0_inv, p1_inv = utilidades.recta_perpendicular(p0, p1)
    py5.line(p0[0], p0[1], p1[0], p1[1])
    py5.line(p0_inv[0], p0_inv[1], p1_inv[0], p1_inv[1])


    




if __name__ == "__main__":
    py5.run_sketch()