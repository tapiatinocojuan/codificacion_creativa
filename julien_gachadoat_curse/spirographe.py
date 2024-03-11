import py5

from os import path
import sys
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

nb = 10;
        
grados = 0
dim = 350
num_cuadros = nb
f_min = 0.7
fps = 30
ciclos = 15

def setup():
    global fps
    py5.size(500, 500)
    py5.rect_mode(py5.CENTER)
    py5.frame_rate(fps)

def draw():
    global grados, nb, dim, f_min, num_cuadros, ciclos
    py5.background(0)
    py5.translate(py5.width/2, py5.height/2)
    py5.no_fill()
    py5.stroke(255)
    for i in range(num_cuadros):
        f = py5.remap(i, 0, num_cuadros-1, 1, f_min) 
        py5.square(0, 0, f * dim)
        py5.rotate(grados*py5.PI/180)

    grados += 1
    if grados == 90:
        grados = 0
        num_cuadros += 1
        if f_min > 0.1:
            f_min -= 0.1

    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    if py5.frame_count > 90*ciclos:
        py5.no_loop()

if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "spirographe")
    remove_png(RUTA)