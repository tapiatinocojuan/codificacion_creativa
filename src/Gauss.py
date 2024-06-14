""""Codigo de movimiento de dibujitos kawaii
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""

import py5
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

imagenes = (
    #("elefantito_sombras.png", "#a1432b"),
    ("elefantito_sombras.png", "#ff7291"),
)
fps = 60
pixel_list = []
indexes = None


def setup():
    global pixel_list, indexes
    py5.size(720, 1280)
    pixel_list.append(Particle(int(py5.width/2), 0, [0, 0, 0, 255]))
    indexes = [py5.height-100 for x in range(py5.width)]
    

def draw():
    global pixel_list, indexes
    print(py5.frame_count)
    py5.background(imagenes[0][1])
    for particula in pixel_list:
        particula.draw()
        if particula.kill:
            continue
        particula.update(indexes)
    if py5.frame_count <= 5*py5.height:
        pixel_list.append(Particle(int(py5.width/2), 0, [255, 255, 255, 255]))
    if py5.frame_count >= 6*py5.height:
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
        if self.y >= int(py5.height*3/4):
            self.vx = 0
        else:
            self.vx = py5.random_choice([2, -2])
    
    def draw(self):
        py5.stroke(0, 0, 0, 255)
        py5.fill(0,0,0,255)
        py5.circle(self.x, self.y, 2)
        #py5.point(self.x, self.y)
    
    def update(self, indexes):
        y_ocupado = indexes[self.x]
        self.update_speed()
        
        self.x += self.vx
        self.y += self.vy
        if self.x < 0:
            self.x = 0
        if self.x > py5.width:
            self.x = py5.width
        if self.y >= y_ocupado:
            self.kill = True
            indexes[self.x] -= 1
            return 
        



if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, fps, f"distribucion_gaussiano")
    remove_png(RUTA)
