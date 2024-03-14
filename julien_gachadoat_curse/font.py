"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear palabras con movimiento .
"""
from text_to_points import text_to_points
import py5_tools
import py5
puntos = None
fps = 12
def setup():
    global puntos, fps
    py5.size(1000, 500)
    py5.background(0)
    py5.frame_rate(fps)
    puntos = text_to_points(50, 400, "Juan","DATA/Roboto-Regular.ttf", 400, 0.001, 50)
    

def draw():
    global puntos
    py5.background(0)
    py5.no_fill()
    py5.stroke(255)
    for punto in puntos:
        py5.circle(punto[0], punto[1], py5.random(1, 20))

if __name__ == "__main__":
    py5_tools.animated_gif(
        filename = r'DATA\sandy_great_vibes.gif', 
        frame_numbers= range(int(fps*3)), 
        duration = 1/fps
    )
    py5.run_sketch()