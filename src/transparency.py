import py5
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

num_particulas = 100
particulas = []
num_nx = 10
num_ny = 30
borde = 50

frame_reunir = 60
num_frames_reunir = 60


FPS = 30
class Particula():
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.vd = 0 #Incremento de radio
        self.d = d
        self.colors = ( "#FF0000", "#00FF00", "#0000FF")
    
    def draw(self):
        py5.no_stroke()
        for color in self.colors:
            py5.fill(color)
            py5.circle(
                self.x + py5.random(-self.d*0.05, self.d*0.05),
                self.y + py5.random(-self.d*0.05, self.d*0.05),
                self.d
            )

    def update_speed(self, vx=0, vy=0, vd=0):
        self.vx = vx
        self.vy = vy
        self.vd = vd

    def update_pos(self):
        self.x += self.vx
        self.y += self.vy

    def update_size(self):
        self.d += self.vd

def setup():
    global particulas
    #py5.size(2160, 4096) #4K
    py5.size(1080, 1920) #4K
    inc_x = (py5.width - 2*borde) /num_nx
    inc_y = (py5.height - 2*borde) /num_ny
    py5.background(0)
    py5.blend_mode(py5.EXCLUSION)
    for i in range(num_nx):
        for j in range(num_ny):
            particulas.append(
                Particula(
                    borde + i*inc_x + 0.5*inc_x, 
                    borde + j*inc_y + 0.5*inc_y, 
                    py5.random(0.1*inc_x, 0.8*inc_x )
                )
            )
    

def draw():
    global particulas
    py5.background(0)
    if frame_reunir == py5.frame_count:
        calcular_velocidades(py5.width/2, py5.height/2, particulas, num_frames_reunir)
        return 
    elif py5.frame_count ==  frame_reunir + num_frames_reunir:
        particulas = [particulas[0]]
        particulas[0].update_speed(0,0,30)
        return 
    else:
        for particula in particulas:
            particula.update_pos()
            particula.update_size()
            particula.draw()

    
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    if py5.frame_count >= FPS*8:
        py5.no_loop()


def calcular_velocidades(x, y, particulas, num_frames):
    for particula in particulas:
        vx = (x - particula.x)/num_frames 
        vy = (y - particula.y)/num_frames
        particula.update_speed(vx, vy) 

if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, FPS, f"color_combination")
    remove_png(RUTA)