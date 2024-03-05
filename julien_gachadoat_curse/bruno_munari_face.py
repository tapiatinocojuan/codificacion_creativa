"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear un rostro.
"""

import py5
y_mouth = 400
y_eyes = 150
eyes_size = 30

def setup():
    py5.size(500,500)

def draw():
    global y_mouth, y_eyes, eyes_size
    py5.background(255)
    py5.stroke_weight(8)
    step = 100
    for i in range(5):
        #Lineas verticales
        py5.line(50 + i*step, 50, 50 + i*step, 450)
        #Lineas horizontales
        py5.line(50, 50 + i*step, 450, 50 + i*step)
    #Cejas
    py5.no_fill()
    py5.begin_shape()
    py5.vertex(50, 150)
    py5.vertex(150, 50)
    py5.vertex(250, 150)
    py5.vertex(350, 50)
    py5.vertex(450, 150)
    py5.end_shape()
    #Nariz
    py5.line(150, 250, 250, 350)
    py5.line(250, 350, 350, 250)
    #Boca
    py5.line(150, y_mouth, 350, y_mouth)
    #Ojos
    py5.fill(0)
    py5.circle(150, y_eyes, eyes_size)
    py5.circle(350, y_eyes, eyes_size)

def key_pressed():
    print("tecla presionada")
    py5.save(r"DATA\face_bruno_munari.png")

if __name__ == "__main__":
    py5.run_sketch()