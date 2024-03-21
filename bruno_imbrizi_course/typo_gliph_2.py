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
total_text = "Ink"
i = 0
pixel_list = []
fps = 20
max_ages = 360
explode_frame = 100
escala = 0.05
num_cambio = 20
dic_puntos = {}

colores = [
(0,197,252),
(249,87,198),
(135,69,230),
(255,255,255),
]
           
import colorsys
for color in colores:
    print (colorsys.hls_to_rgb(*color))

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
    font = py5.create_font(r"DATA\Sirenik-Regular.otf", size)
    font_1px = py5.create_font(r"DATA\Sirenik-Regular.otf", 2)
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
    dist_max = 1 + (py5.frame_count % num_cambio)*0.2
    py5.stroke(255)
    py5.background(0,0,0)
    py5.text_font(font_1px)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.push_matrix()
    py5.scale(1/escala)
    py5.fill(255,255,255)
    py5.stroke_weight(0.1)
    for j, pixel_a in enumerate(pixel_list):
        for pixel_b in pixel_list[j:]:   
            d = py5.dist(pixel_a.x, pixel_a.y, pixel_b.x, pixel_b.y)
            if d< dist_max:
                py5.stroke(*py5.random_choice(colores))
                py5.line(pixel_a.x, pixel_a.y, pixel_b.x, pixel_b.y)
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
    create_video(RUTA, fps, "transformaciones_glyph_3")
    remove_png(RUTA)