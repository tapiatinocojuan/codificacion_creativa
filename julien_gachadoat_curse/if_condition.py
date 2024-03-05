"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para probar las condicionales .
"""

import py5

def setup():
    py5.size(500, 500)

def draw():
    py5.background(255)
    py5.fill(0)
    if py5.mouse_x < py5.width/3:
        py5.rect_mode(py5.CENTER)
        py5.square(py5.width/2, py5.height/2, 400)
    elif py5.mouse_x < 2*py5.width/3:
        py5.circle(py5.width/2, py5.height/2, 400)
    else:
        py5.triangle(250, 50, 450, 450, 50, 450)


if __name__ == "__main__":
    py5.run_sketch()