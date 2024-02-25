"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear triangulos.
"""
import py5
import utilidades
from paleta_colores import colormap
from create_letter import dibujar_letra
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png
from create_letter import dibujar_letra

j = 0; 
max_r = None; min_r = None;
num_triangulos = 500; num_repeticiones = 600;
pts = []
colores = utilidades.get_colors_4_colormap(py5.random_choice(colormap))
fps = 60

def setup():
    global pts, min_r, max_r, num_repeticiones, fps, colores
    py5.size(980, 980)
    colores = utilidades.get_colors_4_colormap('RdPu')
    py5.background(0)
    py5.frame_rate(fps)
    
    max_r = py5.width/50
    min_r = py5.width/500
    for _ in range(num_repeticiones):
        pts.append(
            utilidades.polygon(
                py5.width/2, py5.height/2, 
                py5.random(min_r, max_r), 3, 0
            )
        )


def draw():
    global j, num_repeticiones, num_triangulos, colores, pts
    #py5.background("#000000")
    if j >= num_triangulos:
        py5.background("#000000")
        j = 0
        pts = []
        for _ in range(num_repeticiones):
            pts.append(
                utilidades.polygon(
                    py5.width/2, py5.height/2, 
                    py5.random(min_r, max_r), 3, 0
                )
            )
        colores = utilidades.get_colors_4_colormap(py5.random_choice(colormap))
        return
    for k in range(num_repeticiones):
        r, g, b, _ = py5.random_choice(colores)
        py5.fill(r*255, g*255, b*255, 150)
        utilidades.draw_shape(pts[k])
        xm, ym = utilidades.punto_medio(pts[k][1], pts[k][2])
        pts[k].pop(0)
        pts[k].append(
            (py5.random(xm - max_r, xm + max_r), 
            py5.random(ym - max_r, ym + max_r) )
        )
    j += 1
    dibujar_letra(200, 200, py5.width - 400, py5.height - 400, "S", "#000000")
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")

if __name__ == '__main__':
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "triangulos_s2")
    remove_png(RUTA)