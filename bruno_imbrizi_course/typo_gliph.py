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

font = None; font_1px=None
size = 1000
total_text = "Transformaciones Tecnológicas"
i = 0
pixel_list = []
fps = 12
max_ages = 360
explode_frame = 100
escala = 0.1
num_cambio = 6
colores = [(192/360, 100/100, 96/100),
           (265/360, 70/100, 89/100),  
           (319/360, 65/100, 97/100)] 
dic_puntos = {}

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


def calculate_points(texto, x, y, font, escala):
    """Obtiene los pixeles para una tipografia"""
    pixel_list = []
    g = py5.create_graphics(py5.width, py5.height)
    g.begin_draw()
    g.scale(escala, escala)
    g.fill(255, 255, 255)
    g.no_stroke()
    g.text_font(font)
    g.text_align(py5.CENTER, py5.CENTER)
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
    global font, size, pixel_list, escala, font_1px, total_text, i, dic_puntos
    py5.size(720, 1280)
    py5.background(255)
    font = py5.create_font("Josefin Sans Regular", size)
    font_1px = py5.create_font("Josefin Sans Regular", 2)
    py5.text_font(font)
    for letter in set(total_text):
        dic_puntos[letter] = calculate_points(letter, py5.width/2, py5.height/3 + 100, font, escala)
    pixel_list = dic_puntos[total_text[i]]


def draw():
    global font, size, texto, pixel_list, explode_frame, escala, font_1px, i, num_cambio, dic_puntos
    if py5.frame_count % num_cambio == 0:
        if i == len(total_text) - 1:
            py5.no_loop()
            return
        i += 1
        pixel_list = dic_puntos[total_text[i]]
        
    print(py5.frame_count)
    py5.no_stroke()
    py5.background(0,0,0)
    py5.text_font(font_1px)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.push_matrix()
    py5.scale(1/escala)
    py5.fill(255,255,255)
    for pixel in pixel_list:   
        tex = choose_text(pixel.color)
        if len(tex)!= 1:
            py5.text_size(py5.random(0.8, 1))
        else:
            py5.text_size(py5.random(0.1, 3))
        py5.text(tex, pixel.x, pixel.y)
    py5.pop_matrix()

    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")

def choose_text(color):
    alpha = py5.alpha(color)
    if py5.random_int(0, 100) == 0:
        return "Transformaciones"
    if py5.random_int(0, 100) == 0:
        return "Tecnologicas"
    if 0 <= alpha < 50:
            return "/"
    if 50 <= alpha < 100:
            return "\\"
    if 100 <= alpha < 150:
            return "+"
    if 150 <= alpha < 200:
            return "-"
    if 200 <= alpha <= 255:
            return "*"
    return "#"



if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "transformaciones_glyph")
    remove_png(RUTA)