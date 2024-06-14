""""Codigo para remplazar pixeles con glifos en imagenes
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""
import py5
from PIL import Image
import numpy as np
simbolos = (33, 126)
tipo_letra = "Huglove"
i = simbolos[0]

data = []
def setup():
    global img, pixeles, font
    py5.size(100, 100)
    font = py5.create_font(r"Huglove", 100)
    #py5.rect_mode(py5.CENTER)
    py5.frame_rate(5)

def draw():
    global i
    py5.background(255)
    g = py5.create_graphics(py5.width, py5.height)
    g.begin_draw()
    g.fill(255, 255, 255)
    g.text_font(font)
    g.text_align(py5.CENTER, py5.CENTER)
    g.fill(0)
    g.stroke(0)
    g.text(chr(i), py5.width/2, py5.height/2)
    g.load_pixels()
    pixel_list = []
    negros = 0
    for k in range(len(g.pixels)):        
        if g.pixels[k] == 0:
            continue
        negros += 1
    g.end_draw()
    
    data.append((negros/len(g.pixels)*100, i))
    py5.image(g, 0, 0)
    i += 1
    if i>simbolos[1]:
        py5.no_loop()
        maximo = max([x[0] for x in data]) 
        for dat in sorted(data):
            print (f"\t({dat[1]}, {dat[0]/maximo}),")

def get_gliph(valor):

    if valor == 0:
        return ""
    if 0 < valor <= 0.2:
        return "."
    if 0.2 < valor <= 0.4:
        return " "


def promediar_matriz(matriz, factor):
    x_size = len(matriz)
    y_size = len(matriz[0])
    paso_x = int(1/factor)
    paso_y = int(1/factor)
    new_size_x = x_size//paso_x
    new_size_y = y_size//paso_y
    new_matriz = np.zeros((new_size_x, new_size_y))
    for i in range(new_size_x):
        for j in range(new_size_y):
            new_matriz[i][j] = np.average(matriz[paso_x*i:paso_x*(i+1), paso_y*j:paso_y*(j+1)])
    return new_matriz


if __name__ == "__main__":
    py5.run_sketch()    


