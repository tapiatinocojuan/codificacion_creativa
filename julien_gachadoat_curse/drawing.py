"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para usar el raton como herramienta de dibujo .
"""

import py5

def setup():
    py5.size(500, 500)
    py5.background(0)

def draw():
    #py5.fill(0)
    #py5.stroke(255)
    py5.no_fill()
    py5.stroke(255, 20)
    py5.stroke_weight(2)
    if py5.is_mouse_pressed:
        #py5.circle(py5.mouse_x, py5.mouse_y, py5.random(100,200))
        my_pattern(py5.mouse_x, py5.mouse_y, py5.mouse_x/10, py5.mouse_y/10)

def key_pressed():
    py5.save(r"DATA\drawing.png")
    py5.background(0)

def my_pattern(x, y, d, amp):
    """Dibuja un cuadrilatero centrado en x y y con tamaño d cuyas esquinas son 
    modificadas aleatoriamente por amp"""
    py5.begin_shape()
    py5.vertex(x-d/2 + py5.random(-amp, amp), y-d/2 + py5.random(-amp, amp))
    py5.vertex(x+d/2 + py5.random(-amp, amp), y-d/2 + py5.random(-amp, amp))
    py5.vertex(x+d/2 + py5.random(-amp, amp), y+d/2 + py5.random(-amp, amp))
    py5.vertex(x-d/2 + py5.random(-amp, amp), y+d/2 + py5.random(-amp, amp))
    py5.end_shape(py5.CLOSE)

if __name__ == "__main__":
    py5.run_sketch()