"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch de como dibujar un archivo vectorial
"""

import py5
import utilidades
import networkx as nx


save_document = False

def setup():
    py5.size(700, 980)

def draw():
    global save_document 
    if save_document:
        py5.begin_record(py5.SVG, "output.svg")
    
    py5.background(0, 0, 100)
    py5.circle(py5.width/2, py5.height/2, 500)

    if save_document:
        py5.end_record()
        save_document = False

def key_pressed():
    global save_document
    if py5.key == 'p':
        save_document = True


if __name__ == "__main__":
    py5.run_sketch()