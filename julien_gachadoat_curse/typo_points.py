"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para trabajar con tipografias.
"""
from text_to_points import text_to_points
import py5_tools
import py5
from os import path
import sys
import colorsys
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

text = "SandInk"
font = "DATA/Roboto-Regular.ttf"
size = 140
spacing = 40
puntos = None
fps = 40
x = 0
y = 250
size_max = 35
speed = 5
ages = 300


colores = [(192/360, 100/100, 96/100),
           (265/360, 70/100, 89/100),  
           (319/360, 65/100, 97/100)] 

class Particle():
    """Clase para la creacion de una particula"""
    def __init__(self, x, y, ages):
        self.vx = py5.random(-2, 2) #Pixeles por frame
        self.vy = py5.random(-2, 2) #Pixeles por frame
        self.x = x - self.vx*ages 
        self.y = y - self.vy*ages 
        self.ages = ages

    def draw(self):
        if py5.frame_count < self.ages:
            self.update()

        phase = py5.dist(py5.width, py5.height/2, self.x, self.y)
        d = py5.sin((speed*py5.frame_count + phase)*py5.PI/180)
        h = py5.remap(self.x, 0, py5.width, 0, 3)
        if h < 0:
            h = 0
        if h > 3:
            h = 2
        else:
            h = int(h)
        s = py5.remap(py5.frame_count, 1, ages*2, 0.5, colores[h][1])
        l = py5.remap(py5.frame_count, 1, ages*2, 0.5, colores[h][2])

        if s > colores[h][1]:
            s =  colores[h][1]
        if l > colores[h][2]:
            l =  colores[h][2]
        r, g, b = colorsys.hsv_to_rgb(colores[h][0], s, l)
        py5.fill(r*255, g*255, b*255)
        py5.stroke(255)
        py5.circle(self.x, self.y, size_max * d)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy

def setup():
    global puntos, fps, x, y, text, size, spacing, ages
    py5.size(720, 1280)
    py5.background(0)
    py5.frame_rate(fps)
    xc = py5.width/2
    yc = py5.height/2
    pts = text_to_points(xc, yc, text, font, size, 0.001, spacing)
    x, y = zip(*pts)
    x_min = min(x)
    y_min = min(y)
    w = max(x) - x_min
    h = max(y) - y_min
    for i, punto in enumerate(pts):
        new_x = punto[0] + py5.width/2 - w/2 -xc
        new_y = punto[1] + py5.height/2 + h/2 -yc
        pts[i] = (new_x, new_y)

    factor = 0.05
    puntos = []
    for pt in compute_points(pts, factor):
        puntos.append(Particle(pt[0], pt[1], ages))

    
def draw():
    global puntos, size_max, speed
    py5.background(0)
    py5.no_fill()
    py5.stroke(255)
    weigth = py5.remap(py5.frame_count, 0, ages, 0.1, 0.5)
    if weigth > 1:
        weigth = 1
    py5.stroke_weight(weigth)
    py5.begin_shape()
    for punto in puntos:
        py5.vertex(punto.x, punto.y)
    py5.end_shape()
    
    py5.stroke_weight(0.5)
    for punto in puntos:
        punto.draw()
    
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    if py5.frame_count > ages*2:
        py5.no_loop()
    
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
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "typo_points")
    remove_png(RUTA)