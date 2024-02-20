"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para animar una imagen rebotando por las paredes de la pantalla.
"""

import py5

x = 0
xspeed = py5.random(0, 5)

y = 0
yspeed = py5.random(0, 5)
logo = None

def setup():
    global logo
    py5.size(800,600)
    logo = py5.load_image('dvd-logo.png')

def draw():
    global x, xspeed, logo, y, yspeed
    py5.background('#000000')
    x += xspeed
    y += yspeed
    py5.image(logo, x, y)
    if (x >= (py5.width - 100) or x <= 0):
        # print('Bye!')
        xspeed *= -1 # Multiplying xspeed by negative 1
    
    if (y >= (py5.height - 45) or y <= 0):
        # print('Bye!')
        yspeed *= -1 # Multiplying xspeed by negative 1

py5.run_sketch()