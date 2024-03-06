"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para trabajar con un sistema de particulas para un campo de flujo.
"""

import py5
particulas = []
num_par = 1000
noise_scale = 0.005
age_max = 600
noise_angle = py5.TAU
noise_speed = 1

class Particle():
    """Clase para la creacion de una particula"""
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.vx = py5.random(-2, 2) #Pixeles por frame
        self.vy = py5.random(-2, 2) #Pixeles por frame

    def draw(self):
        self.update()
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
                or self.y > py5.width):
            self.x = py5.random(0, py5.width)
            self.y = py5.random(0, py5.height)

def setup():
    global particulas, num_par
    py5.size(500,500)
    py5.background(0)
    py5.fill(255)
    for _ in range(num_par):
        particulas.append(
            Particle(
                py5.random(0, py5.width),
                py5.random(0,py5.height)
            )
        )

def draw():
    global particulas, age_max
    py5.stroke(255, py5.remap(py5.frame_count, 1, age_max, 255, 0))
    for particula in particulas:
        particula.draw()

if __name__ == '__main__':
    py5.run_sketch()