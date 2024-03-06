"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para reproducir trabajo de vera_molnar.
"""

import py5
import py5_tools

nc = 30
x_off = 20
y_off = 20
width = None; height = None
fps = 10
ts = 1/fps
f = 1
w = py5.TAU*f
dist_max = None
duracion_gif = 5


def setup():
    global width, height, x_off, y_off, fps, dist_max
    py5.size(500, 500)
    py5.frame_rate(fps)
    py5.no_loop()
    width = (py5.width-2*x_off)/nc
    height = (py5.height-2*y_off)/nc

def draw():
    global nc, width, height, x_off, y_off
    py5.background(255)
    #py5.no_stroke()
    #py5.fill(255)
    
    for i in range(nc):
        for j in range(nc):
            x = x_off + i*width
            y = y_off + j*height
            py5.stroke(0)
            py5.stroke_weight(4)
            rnd = py5.random_int(0, 3)
            match (rnd):
                case 0:
                    py5.line(x, y, x + width, y + height)
                case 1:
                    py5.line(x, y + height, x + width, y)    
                case 2:
                    py5.line(x + width/2, y, x + width/2, y + height)
                case 3:
                    py5.line(x, y + height/2, x + width, y + height/2)

def key_pressed():
    py5.redraw()


if __name__ == "__main__":
    py5.run_sketch()
