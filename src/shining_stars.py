"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear una pantalla estrellada.
"""

import py5
import utilidades
# from paleta_colores import colormap
# from create_letter import dibujar_letra
# from os import path
# RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
# from utilidades import create_video, remove_png
# from create_letter import dibujar_letra
import py5
pts = []; fps = 60; num_points = 200;
ts = 1/fps; #Salto de tiempo de simulacion
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png
colores = [
    '#FF0000', '#00FF00', '#0000FF', '#A0544F',
    '#67F685', '#5600FF' 
]

class ShinningStar():

    def __init__(self, x, y, w, h, shinnig_frec, num_shines, shine_color="#FFFFFF"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h 
        self.shinning_frec = shinnig_frec
        self.shinning_period = 1/self.shinning_frec
        self.num_shines = num_shines
        self.step = py5.TAU/self.num_shines
        self.shine_color = shine_color
        self.alpha = 255
        self.t_ini = py5.random(0, self.shinning_period)

    def set_num_shines(self, num_shines):
        self.num_shines = num_shines
        self.step = py5.TAU/self.num_shines

    def set_shine_color(self, shine_color):
        self.shine_color = shine_color

    def set_alpha(self, alpha):
        if alpha > 255:
            self.alpha = 255
        elif alpha < 0:
            self.alpha = 0
        else:
            self.alpha = alpha

    def calculate_alpha(self, t):
        self.alpha = 125*py5.sin(py5.TAU*(t+self.t_ini)) + 125


    def draw(self):
        n = 10
        shine_step = self.alpha/n
        circle_step = self.w/n
        circle_width = self.w
        ligthing_step = self.step/n

        py5.push_style()
        py5.push_matrix()
        py5.translate(self.x, self.y)
        py5.stroke(self.shine_color)
        py5.stroke_weight(1)
        for _ in range(self.num_shines):
            py5.rotate(self.step)
            py5.push_matrix()
            py5.rotate(-self.step/2)
            for i in range(1, n+1):
                py5.stroke(self.shine_color, shine_step*i)
                py5.fill(self.shine_color, shine_step*i)
                py5.line(0, 0, self.w/2, 0)
                py5.rotate(ligthing_step)
            py5.pop_matrix()
        py5.no_stroke()
        
        for i in range(1, n):
            py5.fill(self.shine_color, shine_step*i)
            py5.circle(0, 0, circle_width)
            circle_width -= circle_step 
        py5.pop_matrix()
        py5.pop_style()




def setup():
    global pts, fps, num_points, colores
    py5.size(980, 980)
    for _ in range(num_points):
        tam = py5.random(5, 20)
        pts.append(
            ShinningStar(
                py5.random(py5.width), py5.random(py5.height),
                tam, tam,
                py5.random(1, fps/4), 20,
                shine_color = py5.random_choice(colores)
            )
        )
    py5.background(0)
    py5.frame_rate(fps)    


def draw():
    global pts, ts
    py5.background("#000000")
    if py5.frame_count >= 300:
        return
    for pt in pts:
        pt.calculate_alpha(ts * py5.frame_count)
        pt.draw()
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")


if __name__ == '__main__':
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "estrellas3")
    remove_png(RUTA)
