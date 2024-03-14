"""Curso "Creative Coding: Making Visuals with JavaScript".

Impartido por Bruno Imbrizi

Adaptado para py5 en python
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear diseños a una regilla.
"""


import py5
import colorsys
from os import path
import sys
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

fps = 60
num_segundos = 4
max_ages = fps*num_segundos
speed = 5

def setup():
    global fps
    py5.size(720, 1280)
    py5.frame_rate(fps)


def draw():
    py5.background(255)
    cols = 10
    rows = 10
    num_cells = cols*rows

    gridw = py5.width * 0.8
    gridh = py5.height * 0.8
    cellw = gridw / cols
    cellh = gridh / cols
    margx = (py5.width - gridw) * 0.5
    margy = (py5.height - gridh) * 0.5

    for i in range(num_cells):
        col = i % cols
        row = int(i/cols)

        x = col * cellw
        y = row * cellh
        w = cellw * 0.8
        h = cellh * 0.8

        n = py5.noise((py5.frame_count + x)*0.0005, y*0.0005)
        scale = py5.remap(n, 0, 1, 1, 30)

        py5.push_matrix()
        py5.translate(x, y)
        py5.translate(margx, margy)
        py5.translate(cellw * 0.5, cellh * 0.5)
        py5.rotate(-n*py5.TAU*speed)
        py5.fill(0)
        py5.no_stroke()
        py5.rect_mode(py5.CENTER)
        py5.rect(0, 0, w, scale*2)
        #py5.line(w*-0.5, 0, w*0.5, 0)
        py5.pop_matrix()

    # py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    # if py5.frame_count > max_ages:
    #     py5.no_loop()

if __name__ == "__main__":
    py5.run_sketch()
    # py5.run_sketch(block=True)
    # create_video(RUTA, fps, "arcos")
    # remove_png(RUTA)