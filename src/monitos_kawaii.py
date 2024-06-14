""""Codigo de movimiento de dibujitos kawaii
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""

import py5
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

imagenes = (
    ("borreguito.png","#709191"),
    ("carnero.png", "#0022ab"),
    ("cocodrilo.png", "#800080"),
    ("elefantito.png", "#a1432b"),
    ("gatito.png", "#aaaaaa"),
    ("gorki.png", "#aed1e8"),
    ("leon.png", "#29a9ff"),
    ("perecita.png", "#aed1e8"),
    ("pollito.png","#0033ff"),
    ("puerquito.png", "#abffff"),
    ("vaquita.png", "#aaaaaa"),
)
img = []
fps = 30
distancia = 265
escala = 0.5
escala2 = 1
angle = 5 #angulo en grados 
inc_angle = angle *(py5.PI/180)
animalito_idx = None
stop_frame = None
cont_stop  = None
cuenta = 0
color = 180

def setup():
    global img
    py5.size(720, 1280)
    py5.frame_rate(fps)
    py5.rect_mode(py5.CENTER)
    for imagen, _ in imagenes:
        img.append(py5.load_image(f"DATA/{imagen}"))

def draw():
    global i, animalito_idx, stop_frame, cont_stop, cuenta
    if animalito_idx == None:
        py5.background(color)
    else:
        py5.background(imagenes[animalito_idx][1])
    angle = py5.TAU/len(img)
    py5.push_matrix()
    py5.translate(py5.width/2, py5.height/2)
    py5.scale(escala)
    for i, imagen in enumerate(img):
        py5.image(
            imagen, 
            distancia*py5.cos(i*angle)/escala - imagen.width/2, 
            distancia*py5.sin(i*angle)/escala - imagen.height/2
        )
    py5.pop_matrix()
    py5.fill(255, 0, 0)
    py5.stroke(0)
    py5.push_matrix()
    py5.translate(py5.width/2, py5.height/2)
    py5.rotate(cuenta%360*inc_angle)
    py5.translate(330,0)
    py5.triangle(0, 0, 20, 20, 20, -20)
    py5.pop_matrix()
    if cont_stop == None:
        cuenta += 1
    else:
        cont_stop += 1
        if cont_stop > fps/2:
            cont_stop = None
    if animalito_idx == None:
        py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
        return
    py5.push_matrix()
    py5.translate(py5.width/2, py5.height/2)
    py5.scale(abs(escala2*py5.sin(py5.frame_count*py5.PI/180)))
    imagen = img[animalito_idx]
    py5.image(
        imagen, 
        -imagen.width/2, 
        -imagen.height/2
    )
    py5.pop_matrix()
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")

def mouse_pressed():
    global animalito_idx, cont_stop, cuenta
    cut_angle = 360/len(imagenes)
    animalito_idx =  round(cuenta*angle%360 / cut_angle)
    if animalito_idx >= len(imagenes):
        animalito_idx = len(imagenes)-1
    cont_stop = 0



if __name__ == "__main__":
    py5.run_sketch(block=True)
    create_video(RUTA, fps, f"ruleta_kawai")
    remove_png(RUTA)
