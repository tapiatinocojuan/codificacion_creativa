"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear composicion basica de rectangulos.
"""

import py5

def setup():
    py5.size(500,500)

def draw():
    py5.background("#F1FAEE")
    py5.no_stroke()
    py5.fill("#E63946")
    py5.rect(50,50,200,400)
    py5.fill("#1D3557")
    py5.rect(250,50,200,200)
    py5.fill("#A8DADC")
    py5.rect(250,250,200,200)
    py5.fill("#457B9D")
    py5.rect(250,250,100,100)
    py5.rect(350,350,100,100)



if __name__ == "__main__":
    py5.run_sketch()