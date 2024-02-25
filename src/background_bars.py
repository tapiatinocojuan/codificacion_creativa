"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear barras que se mueven en el fondo.
"""
import py5
import utilidades
from paleta_colores import colormap
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png
img = None; step = None
num_bar = 900
bars = []
fps = 60
ts = 1/fps; #Salto de tiempo de simulacion
color = py5.random_choice(colormap)
color = "nipy_spectral"
print (color)
colores = utilidades.get_colors_4_colormap(color)

class BackgroundBar():

    def __init__(self, x, y, w, h, growing_frec, bar_color="#FFFFFF"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h 
        self.growing_frec = growing_frec
        self.growing_period = 1/self.growing_frec
        self.size = 0
        self.t_ini = py5.random(0, self.growing_period)
        self.bar_color = None
        self.red = None
        self.green = None
        self.blue = None
        if isinstance(bar_color, str):
            self.bar_color = bar_color
        else:
            self.red = bar_color[0]*255
            self.green = bar_color[1]*255
            self.blue = bar_color[2]*255
        self.wt = self.growing_frec * py5.TAU

    def set_bar_color(self, bar_color):
        self.bar_color = bar_color

    def set_size(self, size):
        if size > self.w:
            self.size = self.w
        elif size < 0:
            self.size = 0
        else:
            self.size = size

    def calculate_size(self, t):
        self.set_size(abs(self.w*py5.sin(self.wt*(t+self.t_ini))))


    def draw(self):
        py5.push_style()
        py5.push_matrix()
        py5.translate(self.x, self.y)
        if isinstance(self.bar_color, str):
            py5.stroke(self.bar_color)
            py5.fill(self.bar_color)
        else:
            py5.stroke(self.red, self.green, self.blue)
            py5.fill(self.red, self.green, self.blue)
        py5.rect(0, 0, self.size, self.h)       
        py5.pop_matrix()
        py5.pop_style()


def setup():
    global img, step, num_bar, fps
    py5.size(900,900)
    img = py5.load_image('sandy.png')
    step = py5.height/num_bar
    py5.frame_rate(fps)
    for i in range(num_bar):
        bars.append(
            BackgroundBar(
                0, i*step, 
                py5.width, step, 
                py5.random(0.1, 1),
                bar_color = py5.random_choice(colores))
        )

def draw():
    global img, bars
    py5.background("#000000")
    for bar in bars:
        bar.calculate_size(ts * py5.frame_count)
        bar.draw()
    py5.image(img, 0, 0)
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")

if __name__ == '__main__':
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "barras")
    remove_png(RUTA)