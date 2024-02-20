"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear triangulos y guardarlos en un archivo svg.
"""
import py5
from sketch06 import dibuja_triangulos
import paletas_colores 

colores = paletas_colores.paleta_goku_blue_2

save_file = False
s = 1

def setup():
    py5.size(980, 980)

def draw():
    global s, save_file
    py5.random_seed(s)
    
    if save_file:
        py5.begin_record(py5.SVG, f"output-{s}.svg")
    py5.background(0, 0, 0, 255)
    for i in range(100):
        dibuja_triangulos(py5.random_int(py5.width), py5.random_int(py5.height), 10, colores)
    if save_file:
        py5.end_record()
        save_file = False

def mouse_pressed():
    global s
    s += 1
    print(s)

def key_pressed():
    global save_file
    save_file = True

def mouse_wheel():
    global s
    if s > 0:
        s -= 1
        print (s)


if __name__ == "__main__":
    py5.run_sketch()