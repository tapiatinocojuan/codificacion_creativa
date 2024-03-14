"""Curso "Creative Coding: Making Visuals with JavaScript".

Impartido por Bruno Imbrizi

Adaptado para py5 en python
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear diseños basados en fuentes.
"""

import py5
from os import path
import sys
import colorsys
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

font = None
size = 180
texto = "A"
pixel_list = []
fps = 60
max_ages = 360
explode_frame = 100

colores = [(192/360, 100/100, 96/100),
           (265/360, 70/100, 89/100),  
           (319/360, 65/100, 97/100)] 

class Particle():

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color 
        self.vx = py5.random(-2, 2) #Pixeles por frame
        self.vy = py5.random(-2, 2) #Pixeles por frame

    def update(self):
        self.x += self.vx
        self.y += self.vy


def calculate_points(texto, x, y, font):
    """Obtiene los pixeles para una tipografia"""
    pixel_list = []
    g = py5.create_graphics(py5.width, py5.height)
    g.begin_draw()
    g.fill(255, 255, 255)
    g.text_font(font)
    g.text_align(py5.LEFT, py5.CENTER)
    g.text(texto, x, y)
    g.load_pixels()
    pixel_list = []
    for k in range(len(g.pixels)):
        if g.pixels[k] == 0:
            continue
        x = k % py5.width
        y = int (k/py5.width)
        pixel_list.append(Particle(x, y, py5.color(g.pixels[k])))
    g.end_draw()

    return pixel_list

def setup():
    global font, size, pixel_list
    py5.size(780, 1280)
    py5.background(255)
    font = py5.create_font(r"DATA\TT Chocolates Trial Regular.otf", size)
    font2 = py5.create_font(r"DATA\Sirenik-Regular.otf", size+100)
    py5.text_font(font)
    tx1_w = py5.text_width("SAND")
    pixel_list = calculate_points("SAND", 0, py5.height/2, font)
    py5.text_font(font2)
    tx2_w = py5.text_width("Ink")
    pixel_list.extend(calculate_points("Ink", tx1_w-20, py5.height/2, font2))
    


def draw():
    global font, size, texto, pixel_list, explode_frame
    print(py5.frame_count)
    py5.no_stroke()
    py5.background(0)
    #py5.image(g, 0, 0)
    for pixel in pixel_list:        
        if py5.frame_count > explode_frame:
            pixel.update()
        if py5.frame_count == explode_frame:
            h = py5.remap(pixel.x, 0, py5.width, 0, 3)
            if h < 0:
                h = 0
            if h > 3:
                h = 2
            else:
                h = int(h)
            r, g, b = colorsys.hsv_to_rgb(colores[h][0], colores[h][1], colores[h][2])
            pixel.color = py5.color(r*255, g*255, b*255)
        else:
            py5.fill(pixel.color)
        py5.rect(pixel.x, pixel.y, 1, 1)

    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    if py5.frame_count > max_ages:
        py5.no_loop()

    
    
    


def key_pressed():
    global pixel_list
    texto = py5.key
    pixel_list = calculate_points(texto, font)


if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "sandink_explode")
    remove_png(RUTA)