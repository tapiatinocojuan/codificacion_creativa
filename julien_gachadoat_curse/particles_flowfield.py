"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para trabajar con un sistema de particulas para un campo de flujo.
"""

import py5
import colorsys
from os import path
import sys
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png


particulas = []
num_par = 3000
noise_scale = 0.005
age_max = 600
noise_angle = py5.TAU
noise_speed = 1
fps = 45
img  = None

class Particle():
    """Clase para la creacion de una particula"""
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.vx = py5.random(-2, 2) #Pixeles por frame
        self.vy = py5.random(-2, 2) #Pixeles por frame

    def draw(self):
        self.update()
        #s = py5.remap(self.x, 0, py5.width, 0, 1)
        s = py5.remap(py5.frame_count, 1, age_max, 0.3, 0)
        #l = py5.remap(self.y, 0, py5.height, 1, 0.5)
        l = py5.remap(py5.frame_count, 1, age_max, 1, 0.75)
        r, g, b = colorsys.hsv_to_rgb(59/360,s,l)
        alpha =  py5.remap(py5.frame_count, 1, age_max, 255, 0)
        py5.stroke(r*255, g*255, b*255, alpha)
        py5.point(self.x, self.y)
    
    def update(self):
        global noise_scale, noise_angle, noise_speed
        n = noise_angle *py5.noise(noise_scale*self.x, noise_scale*self.y)
        self.vx = noise_speed * py5.cos(n)
        self.vy = noise_speed * py5.sin(n)
        self.x += self.vx
        self.y += self.vy
        if (self.x < 0 
                or self.x > py5.width 
                or self.y < 0 
                or self.y > py5.height):
            self.x = py5.random(0, py5.width)
            self.y = py5.random(0, py5.height)

def setup():
    global particulas, num_par, fps, img
    py5.size(1600,798)
    py5.background(0)
    py5.fill(255)
    py5.frame_rate(fps)
    img = py5.load_image('cempasuchitl.png')
    for _ in range(num_par):
        particulas.append(
            Particle(
                py5.random(0, py5.width),
                py5.random(0,py5.height)
            )
        )

def draw():
    global particulas, age_max, img
    for particula in particulas:
        particula.draw()
    py5.image(img, 0, 0)
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    if py5.frame_count > age_max:
        py5.no_loop()

if __name__ == '__main__':
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "flow_field")
    remove_png(RUTA)