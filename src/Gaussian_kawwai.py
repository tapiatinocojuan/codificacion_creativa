""""Codigo de movimiento de dibujitos kawaii
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""

import py5
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

imagenes = (
    ("elefantito_sombras.png", "#a1432b"),
)
fps = 30
pixel_list = []


def setup():
    global pixel_list
    py5.size(720, 1280)
    img = py5.load_image(f"DATA/{imagenes[0][0]}")
    for k in range(len(img.pixels)):
        if img.pixels[k] == 16777215:
            continue
        x = k % py5.width
        y = int (k/py5.width)
        pixel_list.append(Particle(x, y, py5.color(img.pixels[k])))
    print(len(pixel_list))

def draw():
    print(py5.frame_count)
    py5.background(imagenes[0][1])
    for particula in pixel_list:
        particula.draw()
        particula.update()
    if py5.frame_count >= py5.height:
        py5.no_loop()
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")


class Particle():
    """Clase para la creacion de una particula"""
    def __init__(self, x, y, color):
        self.x = x 
        self.y = y
        self.kill = False
        self.color = color

    def update_speed(self):
        self.vy = 1
        self.vx = py5.random_choice([1, -1])
    
    def draw(self):
        py5.stroke(self.color)
        py5.point(self.x, self.y)
    
    def update(self):
        self.update_speed()
        self.x += self.vx
        self.y += self.vy
        if self.x < 0:
            self.x = 0
        if self.x > py5.width:
            self.x = py5.width
        if self.y > py5.height:
            self.kill = True


if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, fps, f"elefantito_gaussiano")
    remove_png(RUTA)
