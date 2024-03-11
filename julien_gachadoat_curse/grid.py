"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para mostrar el uso grillas.
"""

import py5
import py5_tools
from os import path
import sys
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

nc_w = 20
nc_h = 30
x_off = 20
y_off = 20
width = None; height = None
fps = 30
ts = 1/fps
f = 0.5
w = py5.TAU*f
dist_max = None


def setup():
    global width, height, x_off, y_off, fps, dist_max
    py5.size(720, 1280)
    py5.frame_rate(fps)
    width = (py5.width-2*x_off)/nc_w
    height = (py5.height-2*y_off)/nc_h
    dist_max = py5.dist(0, 0, py5.width/2, py5.height/2)

def draw():
    global nc, width, height, x_off, y_off, w, ts, dist_max
    py5.background(0)
    py5.no_stroke()
    py5.fill(255)
    #py5.stroke(255)
    #py5.no_fill()
    py5.rect_mode(py5.CENTER)
    
    for i in range(nc_w):
        for j in range(nc_h):
            x = x_off + width/2 + i*width
            y = y_off + height/2 + j*height
            d = py5.dist(x, y, py5.width/2, py5.height/2)
            r = py5.remap(x, 0, py5.width, 0, 255)
            g = py5.remap(y, 0, py5.height, 0, 255)
            alpha = py5.remap(d, 0, dist_max, 200, 255)
            py5.fill(r, g, py5.frame_count, alpha)
            mod = py5.sin(
                w*ts*py5.frame_count 
                + 2*py5.dist(py5.width/2, py5.height/2, x, y)
            )
            py5.ellipse(
                x, 
                y, 
                mod*width, 
                mod*height
            )
            # py5.rect(
            #     x_off + width/2 + i*width, 
            #     y_off +height/2 + j*height, 
            #     width*0.9, height*0.9
            # )
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    if py5.frame_count > 255:
        py5.no_loop()

if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "grid")
    remove_png(RUTA)
