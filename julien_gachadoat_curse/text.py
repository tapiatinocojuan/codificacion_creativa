"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch .
"""

import py5

font = None; puntos = None

def preload():
    global font
    

def setup():
    global font, puntos
    py5.size(500, 500)
    font = py5.create_font("Great Vibes", 400)
    puntos = []
    for letter in "b":
        shape = font.get_shape(letter)
        aux = []
        for vertex_num in range(shape.get_vertex_count()):
            aux.append(shape.get_vertex(vertex_num))
        puntos.append(aux)
    

def draw():
    global puntos
    py5.push_style()
    py5.fill(0)
    py5.circle(py5.width/2, py5.height/2, 50)
    py5.pop_style()
    for letter in puntos:
        py5.begin_shape()
        for vertex in letter:
            py5.circle(vertex.x + py5.width/2, vertex.y + py5.height/2, 10)
            py5.vertex(vertex.x + py5.width/2, vertex.y + py5.height/2)
        py5.end_shape(py5.CLOSE)

if __name__ == "__main__":
    py5.run_sketch()