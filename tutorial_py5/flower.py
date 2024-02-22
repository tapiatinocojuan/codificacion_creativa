"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para realizar la animacion de una flor.
"""
import py5
import sys
from os import path
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

num_leaves = 20
num_leaves_2 = 15
num_circles = 5
step = 1/num_leaves
step_2 = py5.TAU/num_leaves_2
i = 0
j = 0
k = 0
fps = num_leaves

def setup():
    py5.size(600, 600)
    py5.frame_rate(num_leaves)
    py5.no_fill()
    py5.stroke('#F58617')
    py5.background(0)
    
def draw():
    global num_leaves_2, num_leaves, step, step_2, i, j, k, num_circles
    if j >= num_leaves_2:
        if k >= num_circles:
            return
        py5.fill("#7B3212")
        py5.stroke("#000000")
        py5.push_matrix()
        py5.translate(py5.width/2, py5.height/2)
        rep = num_circles-k
        for l in range (rep):
            initial_angle = py5.TAU/(2**k*rep)
            py5.rotate(initial_angle)
            draw_circles(k, 8)
        py5.pop_matrix()
        k += 1
        py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
        return
    if i == num_leaves:
        i = 0
        j += 1
    
    i += 1
    py5.push_matrix()
    py5.translate(py5.width/2, py5.height/2)
    py5.rotate(j*step_2)
    py5.translate(25, 0)
    py5.scale(i*step)
    draw_leaf(0, 200, 50, 50)
    py5.pop_matrix()

    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")

def draw_leaf(x0, w, bx, by):
    """Funcion que dibuja una hoja unica de la planta"""
    py5.begin_shape()
    py5.vertex(x0, 0)
    py5.bezier_vertex(x0 + bx, -by, x0 + w - bx, -by, x0+w, 0)
    py5.bezier_vertex(x0 + w - bx, by, x0 + bx, by, x0, 0)
    py5.end_shape()


def draw_circles(n, w):
    """Funcion que dibuja circulos"""

    num_circles = 2**n
    angle_step =  py5.TAU/num_circles
    for i in range(num_circles):
        py5.push_matrix()
        py5.rotate(angle_step*i)
        py5.translate(n*w*0.7, 0)
        py5.circle(0,0,w)
        py5.pop_matrix()

if __name__ == '__main__':
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "my_video")
    remove_png(RUTA)
