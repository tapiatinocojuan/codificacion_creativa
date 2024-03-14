""""Codigo para elaboracion de logo de transformaciones tecnologicas
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""


import py5
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png
import colorsys

fps = 20
font = None
arcos = []
max_ages = 100
colores = ["#cdb4db", "#ffc8dd", "#ffafcc", "#bde0fe"] #pasteles
colores = ["#219ebc", "#023047", "#ffb703", "#fb8500"] #Rumania
def setup():
    global arcos ,fps, font
    py5.size(720, 1280)
    velocidad = 40
    grosor = 15
    diametro_inicial = 0
    py5.frame_rate(fps)
    py5.background(255)
    arcos = [
        Arc(py5.width/2, py5.height/2 - py5.width/2, velocidad, py5.color(colores[0]), diametro_inicial, grosor),
        Arc(0, py5.height/2, velocidad, py5.color(colores[1]), diametro_inicial, grosor),
        Arc(py5.width, py5.height/2, velocidad, py5.color(colores[2]), diametro_inicial, grosor),
        Arc(py5.width/2, py5.height/2 + py5.width/2, velocidad, py5.color(colores[3]), diametro_inicial, grosor),
    ]
    font = py5.create_font("Impact", 200)
    print (py5.Py5Font.list())

def draw():
    global arcos, font
    for arco in arcos:
        arco.draw()
        arco.update()
    py5.text_font(font)
    py5.fill(255)
    py5.stroke(255)
    py5.text_align(py5.LEFT, py5.TOP)
    py5.text(f"ELLA", 100, 150)
    py5.text(f"NO", 100, 350)
    py5.text(f"TE", 100, 550)
    py5.text(f"AMA", 100, 750)
    py5.text(f"BRO", 100, 950)

    
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    if py5.frame_count > max_ages:
        py5.no_loop()
    

class Arc():
    def __init__(self, x, y, velocidad, color, diametro, grosor):
        self.x = x
        self.y = y
        self.v = velocidad
        self.color = color 
        self.diametro = diametro
        self.grosor = grosor
        self.retardo = 0

    def update(self):
        if py5.frame_count > self.retardo:
            self.diametro += self.v

    def draw(self):
        py5.no_fill()
        py5.stroke(self.color)
        py5.stroke_weight(self.grosor)
        py5.arc(self.x, self.y, self.diametro, self.diametro, 0, py5.TAU)

if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "no_te_ama")
    remove_png(RUTA)