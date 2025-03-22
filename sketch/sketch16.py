"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para cuadrados con 2 curvas bezier que serviran como bloques 
para un mosaico.
"""


import py5
s=1
BACKGROUD_COLOR = "#000000"

def setup():
    global s
    py5.size(500, 500)
    py5.background(BACKGROUD_COLOR)
    py5.begin_record(py5.SVG, "salida.svg")
    pintar()
    py5.end_record()

def pintar():
    py5.random_seed(s)
    n = 2
    nm = 20
    step_x = py5.width/n
    step_y = py5.height/n
    #color = [                       #CMYK
    #    ("#00FFFF","#FF00FF"),
    #    ("#FFFF00", "#FFFFFF")
    #]
    # color = [                        #RGB
    #     ("#FF0000","#00FF00"),
    #     ("#0000FF", "#FFFFFF")
    # ]
    # color = [                         #Verdes
    #     ("#008080", "#20B2AA"),
    #     ("#66CDAA", "#3CB371"),
    # ]
    color = [                         #Arcoiris
        ("#ff0000", "#ff9900"),
        ("#ffff00", "#00ff00"),
    ]
    color = [                         #Arcoiris
        ("#000000", "#222222"),
        ("#444444", "#666666"),
    ]
    for i in range(n):
        for j in range(n):
            bg_color = BACKGROUD_COLOR
            megamozaico(step_x, step_y, step_x*i, step_y*j, bg_color, color[i][j], nm)



def megamozaico(w, h, x_off, y_off, bg_color, fill_color, n):
    step_x = w/n
    step_y = h/n
    for i in range(n):
        for j in range(n):
            mozaico(step_x, step_y, x_off + step_x*i, y_off + step_y*j, bg_color, fill_color)




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





def mouse_pressed():
    global s 
    s += 1

if __name__ == '__main__':
    py5.run_sketch()


