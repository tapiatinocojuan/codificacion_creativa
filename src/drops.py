"""Script que trata de emular gotas de agua cayendo"""

import py5
from paleta_colores import colores_neon as colores
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

FPS = 30
periodo = 1/FPS
num_segundos = 5
num_gotas = 600
gotas = []
 

class Particula():
    def __init__(self, x_min, x_max, y_min, y_max, periodo):
        self.x = py5.random(x_min, x_max)
        self.y = py5.random(y_min, y_max)
        self.vx = 0 #pixeles/segundo
        self.vy = 0 #pixeles/segundo
        self.h = py5.random_int(50, 300)
        self.r = py5.random_int(5, 15)
        self.color = py5.random_choice(colores)
        self. periodo = periodo
        self.g = 10 #pixeles/segundo2
        
    def update_speed(self):
        """Consideramos que la velocidad de las gotas solo se modifica en el eje y
        
        Simplificamos a la velocidad en caida libre
        """
        self.vy = self.g * self.periodo * py5.frame_count
    
    def update_speed2(self, frame):
        """Consideramos que la velocidad de las gotas solo se modifica en el eje y
        
        Simplificamos a la velocidad en caida libre
        """
        g = 10 #pixeles/segundo2
        self.vy = g * self.periodo * frame
    
    def update_pos (self):
        self.x += self.vx * self.periodo
        self.y += self.vy * self.periodo

    def draw(self, frame=None):
        if self.h <= 0:
            return
        py5.push_style()
        py5.no_stroke()
        #if frame is None:
        #    py5.fill(self.color, py5.remap(py5.frame, 255, 50, 0, num_segundos*FPS))
        #else:
        #    py5.fill(self.color, py5.remap(frame, 255, 50, 0, num_segundos*FPS))
        py5.fill(self.color, 255)
        py5.circle(self.x, self.y, self.r)
        py5.pop_style()
        if frame is None:
            self.update_speed()
        else:
            self.update_speed2(frame)
        self.update_pos()
        self.h -= 1
    
    

def setup():
    global gotas
    py5.size(720, 1280)
    py5.background(0)
    for _ in range(num_gotas):
        gotas.append(
            Particula(py5.width/4, 3*py5.width/4, py5.height/5, py5.height/2, periodo)
        )
        #gotas.append(
        #    Particula(0, py5.width, py5.height/4, py5.height/2, periodo)
        #)

def draw():
    global gotas
    #py5.begin_record(py5.SVG, "DATA/barras.svg")
    #py5.background(0)
    #for i in range(num_segundos * FPS):
    for gota in gotas:
        gota.draw()
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    #py5.end_record()
    #py5.no_loop()

if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, FPS, f"drops")
    remove_png(RUTA)

