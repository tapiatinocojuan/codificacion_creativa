"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear ojos (introducción a las funciones).
"""
import py5

def setup():
    py5.size(980, 980)
    py5.background(0, 0, 200)
    for y in range (100, 1000, 100):
        eye(py5.width/2, y, 150)

def eye(x, y, w):
    py5.no_stroke()
    py5.fill(255)
    py5.ellipse(x, y, w, w/3)
    py5.fill(0, 0, 255)
    py5.ellipse(x, y, w/3, w/3)
    py5.fill(0)
    py5.ellipse(x, y, w*0.1, w*0.1)


if __name__ == "__main__":
    py5.run_sketch()