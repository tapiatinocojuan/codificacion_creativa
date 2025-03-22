""""Codigo para remplazar pixeles con glifos en imagenes
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""
import py5
from PIL import Image
import numpy as np
factor_escala = 0.1 #Imagenes grande
factor_crecimiento = 0.025
factor_velocidad = 1
noise_scale = 0.005
noise_angle = 360
#noise_scale = 0.005
#noise_angle = py5.TWO_PI
import sys
from os import path
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))

def setup():
    global img, pixeles, xc, yc
    py5.size(500, 500)
    py5.background(0)
    xc = py5.width/2
    yc = py5.height/2

    

def draw():
    global xc, yc
    py5.no_stroke()
    py5.fill("#ffffff")
    x = xc + py5.frame_count*factor_crecimiento*py5.sin(factor_velocidad*py5.frame_count*py5.DEG_TO_RAD)
    y = yc + py5.frame_count*factor_crecimiento*py5.cos(factor_velocidad*py5.frame_count*py5.DEG_TO_RAD)
    noise = py5.noise(x, y)
    py5.circle(x, y, py5.remap(noise,0,1, 1,3))

    

if __name__ == "__main__":
    py5.run_sketch()    


