"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para trabajar con un sistema de particulas.
"""

import py5
particulas = []
num_par = 200
dist_max = 30

class Particle():
    """Clase para la creacion de una particula"""
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.vx = py5.random(-2, 2) #Pixeles por frame
        self.vy = py5.random(-2, 2) #Pixeles por frame

    def draw(self):
        self.update()
        py5.circle(self.x, self.y, 5)
    
    def update(self):
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
    py5.fill(255)
    for _ in range(num_par):
        particulas.append(
            Particle(
                py5.random(0, py5.width),
                py5.random(0,py5.height)
            )
        )

def draw():
    global particulas,  dist_max
    py5.background(0)
    py5.no_stroke()
    for particula in particulas:
        particula.draw()
    py5.stroke(255)
    for i, p_a in enumerate(particulas):
        for p_b in particulas[i:]:
            dist = py5.dist(p_a.x, p_a.y, p_b.x, p_b.y)
            if dist < dist_max:
                py5.line(p_a.x, p_a.y, p_b.x, p_b.y)

if __name__ == '__main__':
    py5.run_sketch()