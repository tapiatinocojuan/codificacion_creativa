"""Curso "Creative Coding: Making Visuals with JavaScript".

Impartido por Bruno Imbrizi

Adaptado para py5 en python
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear reticula de cuadros (arreglos y ciclos).
"""


import py5
fps = 12

def setup():
    global fps
    py5.size(600, 600)
    py5.frame_rate(fps)

def draw():
    py5.background(255)
    py5.stroke_weight(4)
    width = 60
    height = 60
    gap = 20
    for i in range(5):
        for j in range(5):
            x = 100 + (width + gap)*i
            y = 100 + (height + gap)*j
            py5.rect(x, y, width, height)
            if py5.random_int(1):
                py5.rect(x + 8, y + 8, width - 16, height - 16)



if __name__ == "__main__":
    py5.run_sketch()