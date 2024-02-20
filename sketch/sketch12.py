"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para ordenando los elementos en una parrilla(grid)
"""

import py5
import utilidades
import networkx as nx

s =1
def setup():
    py5.size(700, 980)

def draw():
    py5.random_seed(s)
    py5.background(0, 0, 100)
    for _ in range(3):
        grid(50, 40, 4, 6, 600)

def grid(off_x, off_y, cols, rows, wt):
    py5.stroke(255)
    w = wt/cols 
    for j in range(rows):
        y = off_y + j*w + w/2
        r = py5.random_int(0, 128)
        g = py5.random_int(128, 255)
        b = py5.random_int(0, 255)
        for i in range(cols):
            x = off_x + i*w + w/2
            m = py5.random_int(1, 6)
            if m == 1:
                py5.fill(r, g, b, 128)
                ra = py5.random(w/20, w/2)
                rb = py5.random(1, w/2)
                np = py5.random_int(4, 10)
                pts = utilidades.star(x, y, ra, rb, np)
                utilidades.draw_shape(pts)
            elif 1 < m < 4:
                py5.fill(255,64)
                dr = py5.random_int(0, 1) * w/2
                py5.rect(x - dr, y - dr, w/2, w/2)
            elif 4 <= m < 6:
                py5.fill(200, 64)
                py5.rect(x - w/2, y - w/2, w, w)
            else:
                py5.fill(r, g, b, 64)
                py5.circle(x, y, py5.random_int(1, 2) * w/4)
            if py5.random_int(1, 3) == 3 and wt > 30:
                grid(x - w/2, y - w/2, 2, 2, w)
def mouse_pressed():
    global s
    s += 1

def key_pressed():
    if py5.key != "s":
        return 
    py5.save_frame(f"salida-{s}.png")

if __name__ == "__main__":
    py5.run_sketch()