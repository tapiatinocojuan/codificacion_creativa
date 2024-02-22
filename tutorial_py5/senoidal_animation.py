"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para diseñar una animación a partir de una señal senoidal.
"""
import py5
from datetime import datetime
import sys
from os import path
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

n = 20 #Numero de arcos
f = 0.2
periodo = 1/f
paso = periodo/(2*n+1) 
w = py5.TAU* f #Frecuencia angular
mp = 100 #Magnitud de la senal senoidal
t_ini = datetime.timestamp(datetime.now())
base = 100 #Distancia de los circulos a la animacion.
fps = 20

def setup():
    global fps
    py5.size(800, 800)
    py5.frame_rate(fps)

def draw():
    global t_ini, n, base, w, paso
    ts = datetime.timestamp(datetime.now()) - t_ini

    py5.background(0)
    step = py5.width*0.8/n
    py5.translate(py5.width/2, py5.height/2)
    py5.stroke(255)
    py5.stroke_weight(3)
    py5.no_fill()
    for i in range(n):
        width = (step) * (i + 1)
        py5.arc(0, 0, width, width, py5.PI, py5.TAU)

    py5.translate(-n/2*step, 0)
    for i in range(2*n + 1):
        py5.line(0, 0, 0, base + senusoidal(ts+ i*paso)+100)
        py5.translate(step/2, 0)
    
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")


def senusoidal(t):
    global w, mp
    return mp*(py5.sin(w*t) + py5.sin(2*w*t) + py5.sin(3*w*t))/3
    return mp*py5.sin(w*t)

if __name__ == '__main__':
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "my_video")
    remove_png(RUTA)
    