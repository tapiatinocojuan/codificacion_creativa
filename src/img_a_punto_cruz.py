""""Codigo para remplazar pixeles por X, esto sirve para generar diseños para punto de cruz
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""
import py5
from PIL import Image
import numpy as np
import colorsys
imagen_path = 'DATA/fer_10x10.png'
im = Image.open(imagen_path)
dpi_x = int((im.info['dpi'])[0])

CT = 14 #Numero de puntos (x) por pulgada

factor_escala = CT/dpi_x* (10*0.30) #Imagenes grande
print (factor_escala)
import sys
from os import path
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))

def setup():
    global img, pixeles, font, pixeles_colors_h,pixeles_colors_s, pixeles_colors_v, pixeles_no_print
    py5.size(im.size[0], im.size[1])
    img = py5.load_image(imagen_path)
    #img.apply_filter(py5.GRAY)
    #img.apply_filter(py5.THRESHOLD, 0.9)
    img.load_np_pixels()
    pixels = img.np_pixels
    font = py5.create_font(r"Huglove", 1)
    pixeles = np.zeros((py5.width, py5.height))
    pixeles_colors_h = np.zeros((py5.width, py5.height))
    pixeles_colors_s = np.zeros((py5.width, py5.height))
    pixeles_colors_v = np.zeros((py5.width, py5.height))
    pixeles_no_print = np.ones((py5.width, py5.height))
    for i, row in enumerate(pixels):
        for j, cell in enumerate(row):
            alpha, red, green, blue  = cell
            lum = 0.2126*red/255 + 0.7152*green/255 + 0.0722*blue/255
            lum = lum*alpha/255
            pixeles[j][i] = (1-lum)
            h, s, v = colorsys.rgb_to_hsv(red/255, green/255, blue/255)
            pixeles_colors_h[j][i] = h
            pixeles_colors_s[j][i] = s
            pixeles_colors_v[j][i] = v
            if alpha == 0:
                pixeles_no_print[j][i] = 0
    pixeles = promediar_matriz(pixeles, factor_escala)
    pixeles_colors_h = promediar_matriz(pixeles_colors_h, factor_escala)
    pixeles_colors_s = promediar_matriz(pixeles_colors_s, factor_escala)
    pixeles_colors_v = promediar_matriz(pixeles_colors_v, factor_escala)
    pixeles_no_print = promediar_matriz(pixeles_no_print, factor_escala)

def draw():
    global img, pixeles, pixeles_colors_h,pixeles_colors_s, pixeles_colors_v, pixeles_no_print, font
    print(f"DATA/{path.basename(imagen_path).split(".")[0]}.svg")
    py5.begin_record(py5.SVG, f"DATA/{path.basename(imagen_path).split(".")[0]}.svg")
    py5.background(255)
    py5.text_font(font)
    py5.scale(1/factor_escala)
    py5.text_align(py5.CENTER)
    py5.fill("#000000")
    for i, renglon in enumerate(pixeles):
        for j, cell in enumerate(renglon):   
            if i == j:
                if i % CT == 0:
                    py5.stroke("#FF0000")
                else:
                    py5.stroke("#0000FF")
                py5.stroke_weight(0.1)
                py5.line(0,i+0.2, len(pixeles), i+0.2)     
                py5.line(i-0.2, 0, i-0.2, len(renglon))     
            py5.text_align(py5.CENTER, py5.CENTER)
            try:
                if pixeles_no_print[i][j] <= 0.2:
                    continue
                # r, g, b = colorsys.hsv_to_rgb(
                #     pixeles_colors_h[i][j],
                #     pixeles_colors_s[i][j],
                #     pixeles_colors_v[i][j],
                # )
                py5.no_stroke()
                py5.stroke("#000000")
                #py5.fill(r*255, g*255, b*255)
                #py5.circle(i, j, py5.remap(cell, 0, 1, 0.5, 1))
                py5.text("X", i, j)
            except:
                import pdb; pdb.set_trace()
    py5.end_record()
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    py5.no_loop()

def get_gliph(valor):
    global simbolos
    
    if valor <= simbolos[0][1]:
        return chr(simbolos[0][0])
    if valor >= simbolos[-1][1]:
        return chr(simbolos[-1][0])
    for i, ( _, threshold) in enumerate(simbolos):
        if valor < threshold:
            return chr(simbolos[i-1][0])


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


