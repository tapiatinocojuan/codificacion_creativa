"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para trabajar con tipografias.
"""
from text_to_points import text_to_points
import py5_tools
import py5

text = "JUAN"
font = "DATA/Roboto-Regular.ttf"
size = 180
spacing = 30
puntos = None
fps = 60
x = 0
y = 250
size_max = 50
speed = 2

def setup():
    global puntos, fps, x, y, text, size, spacing
    py5.size(500, 500)
    py5.background(0)
    py5.frame_rate(fps)
    xc = py5.width/2
    yc = py5.height/2
    puntos = text_to_points(xc, yc, text, font, size, 0.001, spacing)
    x, y = zip(*puntos)
    x_min = min(x)
    y_min = min(y)
    w = max(x) - x_min
    h = max(y) - y_min
    for i, punto in enumerate(puntos):
        new_x = punto[0] + py5.width/2 - w/2 -xc
        new_y = punto[1] + py5.height/2 + h/2 -yc
        puntos[i] = (new_x, new_y)
    
def draw():
    global puntos, size_max, speed
    factor = py5.remap(py5.mouse_x, 0, py5.width, 0.001, 0.01)
    pts =  compute_points(puntos, factor)
    py5.background(0)
    
    py5.no_fill()
    py5.stroke(255)
    py5.begin_shape()
    for punto in pts:
        py5.vertex(punto[0], punto[1])
    py5.end_shape()

    #py5.fill(0)
    
    py5.stroke_weight(2)
    for punto in pts:
        phase = py5.dist(py5.mouse_x, py5.mouse_y, punto[0], punto[1])
        d = py5.sin((speed*py5.frame_count + phase)*py5.PI/180) 

        b = py5.remap(punto[0], 0, py5.width, 0, 255)
        g = py5.remap(punto[1], 0, py5.height, 0, 255)
        py5.fill(0, g, b)
        py5.circle(punto[0], punto[1], size_max * d)
    
def compute_points(puntos, rate):
    """Entrega un submuestreo de los puntos en puntos"""
    if rate > 1:
        rate = 1
    if rate < 0.001:
        rate = 0.001
    
    factor = int(1/rate)
    pts = []
    index = 0
    while (index<len(puntos)):
        pts.append(puntos[index])
        index += factor
    
    return pts



if __name__ == '__main__':
    py5.run_sketch()