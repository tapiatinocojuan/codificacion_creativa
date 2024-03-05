"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear formas geometricas basicas.
"""

import py5

def setup():
    py5.size(500,500)

def draw():
    py5.background(255)
    #Puntos
    py5.point(250, 250)
    #Lineas
    py5.no_fill()
    py5.stroke(0, 250, 0)
    py5.stroke_weight(5)
    py5.line(100,100,100, 400)
    py5.line(200,150,200, 350)
    py5.line(300,200,300, 300)
    py5.line(100,100,400, 250)
    py5.line(100,400,400, 250)
    #Circulos
    py5.no_fill()
    py5.stroke(250, 0, 0)
    py5.circle(250,250,400)
    py5.circle(250,250,300)
    py5.circle(250,250,200)
    #Rectangulos
    py5.no_fill()
    py5.stroke(0, 0, 250)
    py5.rect(150,150,200,200)
    py5.rect(200,200,200,200)
    py5.rect(150,50,200,100)
    #Triangulos
    py5.no_fill()
    py5.stroke(0, 250, 250)
    py5.triangle(250, 150, 400, 400, 100, 400)
    #Forma libre
    py5.no_fill()
    py5.stroke(250, 250, 0)
    py5.begin_shape()
    py5.vertex(100,50)
    py5.vertex(400,100)
    py5.vertex(450,300)
    py5.vertex(200,450)
    py5.vertex(50,350)
    py5.vertex(150,200)
    py5.end_shape(py5.CLOSE)
    #arcos
    py5.fill(250, 0, 250, 50)
    py5.stroke(250, 0, 250)
    py5.arc(250, 250, 400, 400, deg_2_rad(-45), deg_2_rad(45))
    py5.arc(250, 250, 300, 300, deg_2_rad(0), deg_2_rad(90))
    py5.arc(250, 250, 200, 200, deg_2_rad(45), deg_2_rad(135))
    py5.arc(250, 250, 100, 100, deg_2_rad(90), deg_2_rad(180))

def deg_2_rad(degree):
    """Convierte angulos en grados a radianes"""
    return degree*py5.PI/180

if __name__ == "__main__":
    py5.run_sketch()