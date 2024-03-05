"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para mostrar el uso de un ciclo for.
"""

import py5

def setup():
    py5.size(500, 500)

def draw():
    py5.background(0)
    py5.no_stroke()
    py5.fill(255)
    for i in range(5):
        py5.circle(50 + i*100, 250, 100)


if __name__ == "__main__":
    py5.run_sketch()