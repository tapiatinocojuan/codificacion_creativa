"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para controlar los frames por segundo.
"""
import py5
FRAME_RATE = 5 #Frames por segundo

def setup():
    py5.size(742, 300)
    py5.frame_rate(FRAME_RATE)

def draw():
    py5.background(255)
    print(py5.frame_count)
    if py5.frame_count % 2:
        py5.fill(255)
        py5.circle(py5.width*0.5, py5.height*0.5, py5.width*0.25)
    else:
        py5.fill(120)
        py5.circle(py5.width*0.5, py5.height*0.5, py5.width*0.25)


if __name__ == '__main__':
    py5.run_sketch()