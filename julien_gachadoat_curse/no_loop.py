"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para mostrar como detener la ejecucion de draw.
"""

import py5

def setup():
    py5.size(500, 500)
    py5.background(255)
    py5.no_fill()
    py5.stroke(0)
    py5.stroke_weight(4)
    py5.rect(50,50,400,400)

def draw():
    py5.circle(
        py5.random(100, 400),
        py5.random(100, 400),
        15
    )
    if py5.frame_count > 100:
        py5.no_loop()


if __name__ == "__main__":
    py5.run_sketch()