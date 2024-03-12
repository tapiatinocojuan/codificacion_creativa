"""Curso "Creative Coding: Making Visuals with JavaScript".

Impartido por Bruno Imbrizi

Adaptado para py5 en python
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear diseños a partir de arcos.
"""


import py5
import colorsys
from os import path
import sys
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

fps = 30
num_segundos = 4
max_ages = fps*num_segundos

def setup():
    global fps
    py5.size(720, 1280)
    py5.frame_rate(fps)


def draw():
    py5.background(0)
    cx = py5.width/2
    cy = py5.height/2
    w = py5.width * 0.01 
    h = py5.height * 0.5 
    num = 40
    radius = py5.width * 0.05
    rp_min = 1
    rp_max = 8
    color_min = 0.5
    color_max = 0.65
    slice = py5.TAU/num
    for i in range(num):
        l = py5.remap(py5.frame_count, 0, max_ages, 0.75, 1)
        angle = i*slice
        x = cx + radius * py5.sin(angle)
        y = cy + radius * py5.cos(angle)
        py5.push_matrix()
        py5.translate(x, y)
        py5.rotate(-angle)
        py5.scale(py5.random(0.1, 2), py5.random(0.2, 0.5))
        hc = py5.remap(
            angle, 0, py5.TAU, color_min-0.5, color_max-0.5
        )
        r, g, b = colorsys.hsv_to_rgb(hc,1,l)
        py5.fill(r*255, g*255, b*255)
        py5.no_stroke()
        py5.rect(-w*0.5, 0, w, h)
        py5.pop_matrix()
        py5.push_matrix()
        py5.translate(cx, cy)
        py5.rotate(-angle)
        py5.stroke_weight(py5.random(5, 10))
        d = radius*py5.random(rp_min, rp_max)*2
        hc = py5.remap(
            d, radius*rp_min*2,radius*rp_max*2, color_min, color_max
        )
        l = py5.remap(py5.frame_count, 0, max_ages, 0.5, 1)
        r, g, b = colorsys.hsv_to_rgb(hc,1,l)
        py5.no_fill()
        py5.stroke(r*255, g*255, b*255)
        py5.arc(0, 0, d, d, slice * py5.random(-8, 1), slice * py5.random(1, 5))
        py5.pop_matrix()

    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    if py5.frame_count > max_ages:
        py5.no_loop()

if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "arcos")
    remove_png(RUTA)