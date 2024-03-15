""""Codigo para elaboracion de logo de transformaciones tecnologicas
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""


import py5
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png
import colorsys
from datetime import datetime
from collections import defaultdict
import re
import utilidades

color_map = 'RdYlBu_r'
estacion = "Barreras"
colores = utilidades.get_colors_4_colormap(color_map)
fps = 60
datos = defaultdict(list)
i = 0
escala_y = 0.5
step = None; t_max = None; t_min = None; llaves = None; font = None
REGEX =  re.compile(r"(\d{2,4}/\d{2}/\d{2,4})\s*(Nulo|\d*\.?\d*)\s*(Nulo|\d*\.?\d*)\s*(Nulo|-?\d*\.?\d*)\s*(Nulo|-?\d*\.?\d*)")

def setup():
    global fps, datos, step, t_max, t_min, llaves, font
    py5.size(720, 1280)
    py5.background(0)
    py5.frame_rate(fps)
    datos, t_max, t_min = read_conagua_data(f"DATA\\{estacion}.TXT")
    step = py5.TAU/len(datos)
    llaves = list(datos.keys())
    font = py5.create_font("Impact", 50)
    print (t_min, t_max)
    
def draw():
    global datos, i, step, t_max, t_min, llaves, font, estacion
    if i >= len(llaves):
        py5.no_loop()
        return
    data = datos[llaves[i]]
    anio, _ = llaves[i]
    py5.no_fill()
    py5.push_matrix()
    py5.translate(py5.width/2, py5.height/3-100)
    py5.rotate(step*i)
    py5.scale(1, -escala_y)
    #py5.line(0, 0, py5.width/2, 0)
    out = datos_to_coordenadas(data, py5.width/2)
    for j, (value, x) in enumerate(zip(out[2][0][:-2], out[2][1][:-2])):
        color_idx = int(py5.remap(value, -30, 52, 0, 255))
        r, g, b, _ = colores[color_idx]
        py5.stroke(r*255, g*255, b*255, 255)
        py5.line(x, value, out[2][1][j+1], out[2][0][j+1])
    py5.pop_matrix()
    
    py5.push_matrix()
    py5.translate(py5.width/2, 2*py5.height/3 + 100)
    py5.rotate(step*i)
    py5.scale(1, -escala_y)
    for j, (value, x) in enumerate(zip(out[3][0][:-2], out[3][1][:-2])):
        color_idx = int(py5.remap(value, -30, 52, 0, 255))
        r, g, b, _ = colores[color_idx]
        py5.stroke(r*255, g*255, b*255, 255)
        py5.line(x, value, out[3][1][j+1], out[3][0][j+1])
    py5.pop_matrix()
    


    py5.text_font(font)
    py5.text_align(py5.LEFT, py5.TOP)
    py5.fill(0)
    py5.stroke(0)
    py5.rect(600, 1190, 120, 50)
    py5.stroke(255)
    py5.fill(255)
    py5.text(anio, 600, 1200)
    py5.text(estacion, 20, 20)
    color_idx = int(py5.remap(t_max, -30, 52, 0, 255))
    r, g, b, _ = colores[color_idx]
    py5.fill(r*255, g*255, b*255)
    py5.text(f"T_MAX: {t_max}", 20, 100)
    color_idx = int(py5.remap(t_min, -30, 52, 0, 255))
    r, g, b, _ = colores[color_idx]
    py5.fill(r*255, g*255, b*255)
    py5.text(f"T_MIN: {t_min}", 20, 700)
    i += 1
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")


def datos_to_coordenadas(month_data, ancho):
    valores = zip(*month_data) 
    out = []
    for valor in valores:
        aux = [x for x in valor if x is not None]
        x_aux = [i * ancho/len(aux) for i in range(len(aux))]
        out.append((aux, x_aux))
    return out


    

def read_conagua_data(file_path):
    """Lee archivos txt de datos historicos diarios generados por CONAGUA de una estacion
    meteorologica"""

    data = defaultdict(list)
    max_t = -10000
    min_t = 10000
    with open(file_path) as fp:
        for i in range(19):
            fp.readline()
        import pdb;pdb.set_trace()
        for row in fp:
            find = REGEX.search(row)
            if find is None:
                continue
            if "Tacubaya" in file_path:
                fecha = datetime.strptime(find[1], "%Y/%m/%d")
            else:
                fecha = datetime.strptime(find[1], "%d/%m/%Y")
            precipitacion = convert_to_float(find[2])
            evaporacion = convert_to_float(find[3])
            t_max = convert_to_float(find[4])
            t_min = convert_to_float(find[5])
            if t_max is not None:
                if t_max > max_t:
                    max_t = t_max
            if t_min is not None:
                if t_min < min_t:
                    min_t = t_min
            data[(fecha.year, fecha.month)].append(
                ( precipitacion, evaporacion, t_max, t_min)
            )

    return data, max_t, min_t

def convert_to_float(texto):
    """Convierte texto a flotante
    
    En caso de que el valor leido sea Nulo, la funcion regresa None 
    """
    if texto in ["", "Nulo"]:
        return None
    return float(texto)
    

if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, fps, f"historico_temperatura_{estacion}")
    remove_png(RUTA)
    