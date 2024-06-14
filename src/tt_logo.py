""""Codigo para elaboracion de logo de transformaciones tecnologicas
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""


import py5
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png
t1 = (
    (29, 28),
    (7, 28),
    (7,28, 5, 28, 5, 26),
    (5, 9),
    (5, 9, 5, 7, 7, 7),
    (90, 7),
    (91,7, 92, 8, 92, 9),
    (92, 10, 91, 11, 90, 11),
    (9, 11),
    (9, 24),
    (31, 24),
    (31, 24, 33, 24, 33, 26),
    (33, 50),
    (33, 51, 32, 52, 31, 52),
    (30, 52, 29, 51, 29, 50),
    (29, 28),
)
t2 = (
    (87, 25),
    (87,20),
    (13, 20),
    (12,20,11,19,11, 18),
    (11,17,12,16,13,16),
    (90,16),
    (90,16,91,16,91,18),
    (91,27),
    (91,27,91,29,90,29),
    (41,29),
    (41,37),
    (41,38,40,39,39,39),
    (38,39,37,38,37,37),
    (37,27),
    (37,27,37,25,39,25),
    (87,25),
)
s = None
text_size = 4
text_size2 = 6
font = None
font2 = None
explode_frame = 60
max_ages = 600
fps = 60
radio_explosion_min = 30
radio_explosion_max = 80
num_puntos_explosion = 15
puntos_explosion = []

def setup():
    global s, font, font2, text_size, text_size2, pixel_list, max_ages, puntos_explosion
    py5.size(720, 1280)
    s = py5.load_image(r"DATA\firma.png")
    font = py5.create_font("Josefin Sans Regular", text_size)
    font2 = py5.create_font("Prata Regular", text_size2)
    y = 467
    step_x = py5.width/ num_puntos_explosion
    while (y<840):
        x = 0
        for _ in range(num_puntos_explosion):
            puntos_explosion.append( (x, y))
            x += step_x
        y += 50 
    pixel_list = calculate_points()
    for punto_explosion in puntos_explosion:
        x = punto_explosion[0] 
        y = punto_explosion[1] 
        retardo = py5.random_int(explode_frame, explode_frame*3)
        radio_explosion = py5.random(radio_explosion_min, radio_explosion_max)
        for pixel in pixel_list:
            d = py5.dist(x, y, pixel.x, pixel.y)
            if d < radio_explosion:
                if py5.random_int(0,1):
                    continue
                pixel.retardo = retardo
                pixel.vx = py5.random(-2, 2)
                pixel.vy = py5.random(-2, 2)
def draw():
    global s, font, font2, pixel_list, explode_frame
    if py5.frame_count == 1 or py5.frame_count>explode_frame:
        py5.background(0)
        py5.no_stroke()
        for pixel in pixel_list:        
            if py5.frame_count > explode_frame:
                pixel.update()
            py5.fill(pixel.color)
            py5.rect(pixel.x, pixel.y, 1, 1)
    
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    if py5.frame_count > max_ages:
        py5.no_loop()
    print(py5.frame_count)
    

def calculate_points():
    """Obtiene los pixeles para una tipografia"""
    global font, font2, s
    pixel_list = []
    g = py5.create_graphics(py5.width, py5.height)
    g.begin_draw()
    g.fill(255, 255, 255)
    g.no_stroke()
    g.translate(0, (py5.height-2/3*py5.width)/2)
    g.push_matrix()
    escala = 44/s.width*py5.width/100
    g.translate(44*py5.width/100, 21*py5.width/100)
    g.scale(escala)
    g.image(s, 0, 0)
    g.pop_matrix()

    g.push_matrix()
    g.scale(py5.width/100, py5.width/100)
    g.begin_shape()
    for point in t1:
        if len(point) == 2:
            g.vertex(*point)
        else:
            g.bezier_vertex(*point)
    g.end_shape(py5.CLOSE) 

    g.begin_shape()
    for point in t2:
        if len(point) == 2:
            g.vertex(*point)
        else:
            g.bezier_vertex(*point)
    g.end_shape(py5.CLOSE) 

    g.text_font(font)
    g.text_align(py5.LEFT, py5.TOP)
    g.text("TRANSFORMACIONES", 44, 34)

    g.text_font(font2)
    g.text_align(py5.LEFT, py5.TOP)
    g.text("TECNOLÓGICAS", 41, 42)

    g.pop_matrix()
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

class Particle():

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color 
        self.vx = 0 #py5.random(-2, 2) #Pixeles por frame
        self.vy = 0 #py5.random(-2, 2) #Pixeles por frame
        self.retardo = 0

    def update(self):
        if py5.frame_count > self.retardo:
            self.x += self.vx
            self.y += self.vy

if __name__ == "__main__":
    py5.run_sketch(block=True)
    #create_video(RUTA, fps, "tt_explode")
    #remove_png(RUTA)