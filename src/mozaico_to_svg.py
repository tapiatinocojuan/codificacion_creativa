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
n = 30 ; n2 = 40
fps = 120
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
#from utilidades import create_video, remove_png

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
    py5.size(300, 400)
    py5.background(BACKGROUD_COLOR)
    py5.frame_rate(fps)

def draw(): 
    py5.begin_record(py5.SVG, f"DATA/mozaico.svg")
    global s
    global color, n2
    num_row = len(color)
    num_col = len(color[0])
    step_w = py5.width/num_col
    step_h = py5.height/num_row
    step_x = step_w/n
    step_y = step_h/n2
    for i in range(num_col):
        for j in range(num_row):
            for k in range(n):
                for l in range(n2):
                    mozaico(
                        step_x, step_y, 
                        step_w*i + step_x*k,
                        step_h*j + step_y*l,
                        BACKGROUD_COLOR, color[i][j]
                    )
    py5.end_record()
    py5.no_loop()
    #dibujar_letra(0, 0, py5.width, py5.height, "S", "#000000")
    #py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")

def mozaico(w, h, x_off, y_off, bg_color, fill_color):
    #py5.fill(bg_color)
    py5.no_fill()
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
    py5.run_sketch()
    #create_video(RUTA, fps, "mozaicos_bezier_letra_s")
    #remove_png(RUTA)


