"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para cuadrados con 2 curvas bezier que serviran como bloques 
para un mosaico.
"""


import py5
from utilidades import defasar
from create_letter import dibujar_letra

BACKGROUD_COLOR = "#000000"
n = 30 ; i = 0; j = 0; s = 0
fps = 120
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

# color = [                       #CMYK
#    ("#00FFFF","#FF00FF"),
#    ("#FFFF00", "#FFFFFF")
# ]
# color = [                        #RGB
#     ("#FF0000","#00FF00"),
#     ("#0000FF", "#FFFFFF")
# ]
color = [                         #Verdes
    ("#008080", "#20B2AA"),
    ("#66CDAA", "#3CB371"),
]
# color = [                         #Arcoiris
#     ('#ff0000', '#ff9900', '#ffff00'),
#     ('#00ff00', '#0099ff', '#6633ff'),
#     ('#004477','#ff0000', '#ff9900'),
# ]

def setup():
    py5.size(900, 900)
    py5.background(BACKGROUD_COLOR)
    py5.frame_rate(fps)

def draw(): 
    global s
    if s >= 3:
        print ("Ultimo ciclo")
        return
    global color, i, j, n
    num_row = len(color)
    num_col = len(color[0])
    step_x = py5.width/n/num_col
    step_y = py5.height/n/num_row
    

    if i >= n:
        #py5.background(BACKGROUD_COLOR)
        aux = []
        for col in color:
            aux += col
        color = [aux for _ in range(len(aux))]
        i = 0
        j = 0
        s += 1
        py5.redraw()
        return
    for k in range(num_row):
        for l in range(num_col):
            mozaico(
                step_x, step_y, 
                step_x*i + py5.width/num_col*l, step_y*j + py5.height/num_row*k,
                BACKGROUD_COLOR, color[k][l]
            )
    j += 1
    if j >= n:
        i += 1
        j = 0
    
    dibujar_letra(0, 0, py5.width, py5.height, "S", "#000000")
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")


def megamozaico(w, h, x_off, y_off, bg_color, fill_color, n):
    step_x = w/n
    step_y = h/n
    for i in range(n):
        for j in range(n):
            mozaico(step_x, step_y, x_off + step_x*i, y_off + step_y*j, bg_color, fill_color)

def mozaico(w, h, x_off, y_off, bg_color, fill_color):
    py5.fill(bg_color)
    py5.no_stroke()
    py5.begin_shape()
    py5.vertex(x_off + 0, y_off +0)
    py5.vertex(x_off + w, y_off + 0)
    py5.vertex(x_off + w, y_off + h)
    py5.vertex(x_off + 0, y_off + h)
    py5.end_shape()

    if py5.random_int(0, 1):
        bezier_curve(w, h, x_off, y_off, color=fill_color)
    else:
        bezier_curve(w, h, x_off, y_off, color=fill_color, modo=1)

def bezier_curve(w, h, x_off, y_off, color="#FFFFFF", modo=0):
    #py5.stroke(color)
    py5.no_stroke()
    py5.fill(color)
    #py5.stroke_weight(1)
    if modo==0:
        py5.begin_shape()
        py5.vertex(x_off + w/2, y_off)
        py5.bezier_vertex(
            x_off +w/2 , py5.random(y_off, y_off + h/2), 
            py5.random(x_off, x_off + w/2) ,y_off + h/2,
            x_off, y_off + h/2
        )
        py5.vertex(x_off, y_off)
        py5.end_shape()

        py5.begin_shape()
        py5.vertex(x_off + w/2, y_off + h)
        py5.bezier_vertex(
            x_off + w/2, py5.random(y_off + h/2, y_off + h),
            py5.random(x_off + w/2, x_off + w ), y_off + h/2,
            x_off + w, y_off + h/2
        )
        py5.vertex(x_off + w, y_off + h)
        py5.end_shape()
        
    else:
        py5.begin_shape()
        py5.vertex(x_off + w/2, y_off)
        py5.bezier_vertex(
            x_off + w/2, py5.random(y_off, y_off + h/2),
            py5.random(x_off + w/2, x_off + w), y_off + h/2,            
            x_off + w, y_off + h/2
        )
        py5.vertex(x_off + w, y_off)
        py5.end_shape()

        py5.begin_shape()
        py5.vertex(x_off + w/2, y_off + h)
        py5.bezier_vertex(
            x_off + w/2, py5.random(y_off + h/2, y_off + h),
            py5.random(x_off, x_off + w/2), y_off + h/2,  
            x_off, y_off + h/2
        )
        py5.vertex(x_off, y_off + h)
        py5.end_shape()


if __name__ == '__main__':
    py5.run_sketch(block=True)
    create_video(RUTA, fps, "mozaicos_bezier_letra_s")
    remove_png(RUTA)


