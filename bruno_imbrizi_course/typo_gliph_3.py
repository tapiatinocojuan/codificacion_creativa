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
size = 400
total_text = [
    "Juan",
    "Y",
    "Sandy"
]
i = 0
pixel_list = []
fps = 20
max_ages = 1
explode_frame = 100
escala = 0.1
num_cambio = 100
dic_puntos = {}
dic_puntos_indx = {}
margen_y = 200
colores = [
(0,197,252),
(249,87,198),
(135,69,230),
(255,255,255),
]

corazon = [
    (0, 40),
    (40, 5),
    (40, 5, 52, -14, 35, -30),
    (18, -45, 0, -30, 0, -30),
    (0, -30, -18, -45, -35, -30),
    (-52, -15, -40, 5, -40, 5),
    #(0, 40)
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
        self.visible = False

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
    global font, size, pixel_list, escala, font_1px, total_text, i, dic_puntos, margen_y, dic_puntos_indx
    py5.size(2475, 1155)
    py5.background(255)
    font = py5.create_font(r"Great Vibes", size)
    py5.text_font(font)
    h = (py5.height-2*margen_y)/len(total_text)
    for k, word in enumerate(total_text):
        dic_puntos[word] = calculate_points(word, py5.width/2, h*k + margen_y + size/2, font, escala)
        dic_puntos_indx[word] = list(range(len(dic_puntos[word])))

def draw():
    global font, size, texto, pixel_list, explode_frame, escala, font_1px, i, num_cambio, dic_puntos, total_text
    global dic_puntos_indx
    print (py5.frame_count)
    if py5.frame_count >= max_ages:
        py5.no_loop()
    py5.stroke(255)
    #py5.background(0,0,0)
    py5.push_matrix()
    py5.scale(1/escala)
    py5.fill(255,255,255)
    py5.stroke_weight(0.1)
    for word in total_text:
        for pixel_a in dic_puntos[word]:
            if not pixel_a.visible:
                continue 
            alpha = py5.alpha(pixel_a.color)
            py5.fill(255, 175, 3, alpha)
            py5.stroke(255, 175, 3, alpha)
            #py5.ellipse(pixel_a.x, pixel_a.y, py5.sin(2*py5.frame_count*py5.PI/180), 1)
            py5.push_matrix()
            py5.translate(pixel_a.x, pixel_a.y)
            py5.scale(1/100)
            py5.begin_shape()
            for vertex in corazon:
                if len(vertex) == 2:
                    py5.vertex(*vertex)
                else:
                    py5.bezier_vertex(*vertex)
            py5.end_shape(py5.CLOSE)
            py5.pop_matrix()
    py5.pop_matrix()
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")


    ##Aparecen renglon a renglon
    #for word in total_text:
    #    try:
    #        dic_puntos[word][py5.frame_count].visible = True
    #   except:
    #        pass

    #Aparecen de forma aleatoria
    for word in total_text:
        try:
            indx = py5.random_choice(dic_puntos_indx[word])
            idx = dic_puntos_indx[word].index(indx)
            dic_puntos_indx[word].pop(idx)
            print (word, len(dic_puntos_indx[word]))
            dic_puntos[word][indx].visible = True
        except Exception as err:
            pass


if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "transformaciones_glyph_3")
    remove_png(RUTA)