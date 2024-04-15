""""Codigo de movimiento de particulas en campo vectorial básico
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""

import py5
from process_svg import get_point_from_svg
import colorsys
fps = 60;
ts = 1/fps; #Salto de tiempo de simulacion
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png
from paleta_colores import paleta_noche_estrellada

CIRCULOS = 1
CIRCULOS_R = 2
CONSTANTE = 6
INTERIOR = 1
EXTERIOR = 0
punto = (600, 235)
field = None;
particulas = []; particulas2 = []
n = 1000
caso = 0
invertir = -1
factor = 3
num_nuevas_particulas = 10
caso = 0
age_max = 1500
margen = 100

def setup():
    global field, punto, particulas, factor, s1, particulas2, field2
    py5.size(720, 1080)
    field = VectorialField(
        py5.width, py5.height, punto[0], punto[1], caso, invertir
    )
    field2 = VectorialField(
        py5.width, py5.height, punto[0], punto[1], caso, invertir
    )

    field.modificar_campo(250, 140, 100, 9, INTERIOR, -1)
    field.modificar_campo(675, 250, 55, 9, INTERIOR, -1)
    field.modificar_campo(412, 400, 115, 9, INTERIOR, -1)
    field.modificar_campo(128, 692, 120, 9, INTERIOR, -1)
    field.modificar_campo(350, 945, 100, 9, INTERIOR, -1)
    field.modificar_campo(680, 980, 52, 9, INTERIOR, -1)

    s1 = py5.load_shape("DATA/Transformaciones_kawai.svg")
    for i in range(n):
        particulas.append(
            Particle(punto[0]+py5.random(-10, 10), punto[1]+py5.random(-margen, margen))
        )
        particulas2.append(
            Particle(punto[0]+py5.random(-10, 10), punto[1]+py5.random(-margen, margen))
        )
    py5.background(0)

def draw():
    global particulas, field,s1, particula2, field2
    #py5.background(0)
    for particula in particulas:
        speed = field.get_speed(particula.x, particula.y)
        particula.set_speed(speed[0], speed[1])
        particula.draw()
    for particula in particulas2:
        speed = field2.get_speed(particula.x, particula.y)
        particula.set_speed(speed[0], speed[1])
        particula.draw()
    for i in range(num_nuevas_particulas):
        particulas.append(
            Particle(punto[0]+py5.random(-10, 10), punto[1]+py5.random(-margen, margen))
        )
        particulas2.append(
            Particle(punto[0]+py5.random(-10, 10), punto[1]+py5.random(-margen, margen))
        )
    
    py5.shape(s1,0,0, s1.width, s1.height )
    if py5.frame_count >= age_max:
        py5.no_loop()
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    

class Particle():
    """Clase para la creacion de una particula"""
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.vx = py5.random(-2, 2) #Pixeles por frame
        self.vy = py5.random(-2, 2) #Pixeles por frame
        self.color = py5.random_choice(paleta_noche_estrellada)

    def set_speed(self, vx, vy):
        self.vx = vx
        self.vy = vy


    def draw(self):
        self.update()
        #s = py5.remap(py5.frame_count, 1, age_max, 0.3, 0)
        #l = py5.remap(py5.frame_count, 1, age_max, 1, 0.75)
        #r, g, b = colorsys.hsv_to_rgb(59/360,s,l)
        #alpha =  py5.remap(py5.frame_count, 1, age_max, 0, 255)

        #l = py5.remap(py5.frame_count, 0, 500, 0.5, 1)
        #alpha = py5.remap(py5.frame_count, 0, 500, 0, 255)
        #r, g, b = colorsys.hsv_to_rgb(64/360,1,l)

        #r = py5.remap(self.x, 0, py5.width, 0, 255)
        #g = py5.remap(self.y, 0, py5.width, 0, 255)
        #alpha = 255
        
        #efecto noche estrellada
        r =  self.color[0]*255
        g =  self.color[1]*255
        b =  self.color[2]*255
        alpha =  py5.remap(py5.frame_count, 1, age_max, 0, 255)

        py5.fill(r, g, b, alpha)
        py5.stroke(r, g, b, alpha)
        py5.point(self.x, self.y)
        #py5.circle(self.x, self.y, 2)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        if (self.x < 0 
                or self.x > py5.width 
                or self.y < 0 
                or self.y > py5.height):
            self.x = punto[0]+ py5.random(-margen, margen)
            self.y = punto[1]+ py5.random(-margen, margen)

class VectorialField():
    """Campo vectorial"""
    def __init__(self, width, height, px, py, caso, invertir=1):
        self.width =  width
        self.height =  height
        self.px =  px
        self.py = py
        self.field = {}
        self.caso = caso
        self.invertir =  invertir
        self.add_noise = True
        self.vx =  py5.random(-py5.width, py5.width)
        self.vy =  py5.random(-py5.height, py5.height)
        self.calculate_field()


    def calculate_field(self):
        self.field = {}
        for y in range(self.height):
            aux = {}
            for x in range(self.width):
                delta_x, delta_y = self.calculate_deltas(x, y, self.px, self.py, self.caso)
                distancia = py5.dist(x, y, self.px, self.py)
                if distancia == 0:
                    aux[x] = (0, 0)
                else:
                    aux[x] = (delta_x/distancia*self.invertir, delta_y/distancia*self.invertir)
            self.field[y] = aux

    def calculate_deltas(self, x, y, px, py, caso):
        match caso:
            case 0:
                delta_x = (px - x)
                delta_y = (py - y)
            case 1:
                delta_x = -(px - x)
                delta_y = (py - y)
            case 2:
                delta_x = (px - x)
                delta_y = -(py - y)
            case 3:
                delta_x = abs(px - x)
                delta_y = abs(py - y)
            case 4:
                delta_x = abs(px - x)
                delta_y = (py - y)
            case 5:
                delta_x = (px - x)
                delta_y = abs(py - y)
            case 6:
                delta_x = self.vx
                delta_y = self.vy
            case 7:#Radial
                self.add_noise = False
                noise_scale = 0.0001
                n = py5.noise(noise_scale*x, noise_scale*y)
                delta_x = 5*py5.width*py5.cos(n + py5.random(0, py5.TAU))
                delta_y = 5*py5.height*py5.sin(n + py5.random(0, py5.TAU))
            case 8:
                delta_x = (py - y)
                delta_y = (px - x)
            case 9:
                delta_x = -(py - y)
                delta_y = (px - x)

        if self.add_noise:
            noise_scale = 0.0001
            n = py5.noise(noise_scale*x, noise_scale*y)
            delta_x += delta_x*py5.cos(n)
            delta_y += delta_x*py5.sin(n)

        return delta_x, delta_y
    
    def modificar_campo(self, px, py, radio, caso, modo, invertir):
        """modifica una region del campo"""
        for y in range(self.height):
            aux = {}
            for x in range(self.width):
                dist = py5.dist(x, y, px, py)
                if modo == 0: #modificar campo exterior al circulo
                    if dist < radio:
                        continue
                else: #modificar campo interior al circulo
                    if dist > radio:
                        continue
                delta_x, delta_y = self.calculate_deltas(x, y, px, py, caso)
                if dist != 0:
                    self.set_speed(x, y, delta_x/dist*invertir, delta_y/dist*invertir)
                else:
                    self.set_speed(x, y, 0, 0)

    def modificar_campo_rect(self, x, y, w, h, px, py, caso, modo, invertir):
        """modifica una region del campo"""
        for y_aux in range(self.height):
            aux = {}
            for x_aux in range(self.width):
                dist = py5.dist(x_aux, y_aux, px, py)
                if modo == 0: #modificar campo exterior al rectangulo
                    if x < x_aux < x+w :
                        continue
                    if y < y_aux < y+h :
                        continue
                else: #modificar campo interior al circulo
                    if not(x < x_aux < x+w) :
                        continue
                    if not(y < y_aux < y+h) :
                        continue
                delta_x, delta_y = self.calculate_deltas(x_aux, y_aux, px, py, caso)
                if dist != 0:
                    self.set_speed(x_aux, y_aux, delta_x/dist*invertir, delta_y/dist*invertir)
                else:
                    self.set_speed(x_aux, y_aux, 0, 0)

    def modificar_campo_linea(self, px1, py1, px2, py2, factor=1.001):
        """modifica una region del campo"""
        delta_x = px2 - px1
        delta_y = py2 - py1
        distancia = py5.dist(px1, py1, px2, py2)
        vx = delta_x/distancia
        vy = delta_y/distancia
        d = distancia*factor
        for h in range(int(min((px1, px2))-py5.width/10), int(max(px1,px2)+py5.width/10)):
            for w in range(int(min((py1, py2))-py5.height/10), int(max(py1,py2)+py5.height/10)):
                d1 = py5.dist(h, w, px1, py1)
                d2 = py5.dist(h, w, px2, py2)
                if (d1+d2 > d):
                    continue
                self.set_speed(h, w, vx, vy)

    def modificar_campo_from_svg(self, s, caso, modo, invertir):
        """modifica una region del campo basado en un archivo svg"""
        for y in range(self.height):
            for x in range(self.width):
                contiene = s.contains(x, y)
                dist = py5.dist(x, y, self.px, self.py)
                if modo == 0: #modificar elementos externos al dibujo
                    if  contiene:
                        continue
                else: #modificar campo interior interno del dibujo
                    if not contiene:
                        continue
                delta_x, delta_y = self.calculate_deltas(x, y, self.px, self.py, caso)
                if dist != 0:
                    self.set_speed(x, y, delta_x/dist*invertir, delta_y/dist*invertir)
                else:
                    self.set_speed(x, y, 0, 0)

    def get_speed(self, x, y):
        x = int(x)
        y = int(y)
        if y not in self.field:
            return (0, 0)
        if x not in self.field[y]:
            return (0, 0)
        return self.field[y][x]
    
    def set_speed(self, x, y, delta_x, delta_y):
        x = int(x)
        y = int(y)
        if y not in self.field:
            return 
        if x not in self.field[y]:
            return 
        self.field[y][x] = (delta_x, delta_y)

if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, fps, f"corgi_{caso}")
    remove_png(RUTA)