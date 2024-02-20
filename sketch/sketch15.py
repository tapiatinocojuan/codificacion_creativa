"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para cuadrados con 2 curvas bezier que serviran como bloques 
para un mosaico.
"""


import py5
s=1

def setup():
    global s
    py5.size(500, 500)

def draw():
    py5.random_seed(s)
    n = 10
    step_x = py5.width/n
    step_y = py5.height/n
    for i in range(n):
        for j in range(n):
            mozaico(step_x, step_y, step_x*i, step_y*j)




def mozaico(w, h, x_off, y_off):
    py5.fill("#0000FF")
    py5.no_stroke()
    py5.begin_shape()
    py5.vertex(x_off + 0, y_off +0)
    py5.vertex(x_off + w, y_off + 0)
    py5.vertex(x_off + w, y_off + h)
    py5.vertex(x_off + 0, y_off + h)
    py5.end_shape()

    puntos = [
        (x_off + w/2, y_off + 0),
        (x_off + w, y_off + h/2),
        (x_off + w/2, y_off + h),
        (x_off + 0, y_off + h/2),
    ]
    idx1 = py5.random_int(0, 3)
    idx2 = (idx1 + 1) % 4
    idx3, idx4 = list(set([0, 1, 2, 3]) - set([idx1, idx2]))

    pt1 = puntos[idx1]
    pt2 = puntos[idx2]
    pt3 = puntos[idx3]
    pt4 = puntos[idx4]

    py5.stroke_weight(2)
    py5.no_fill()
    py5.stroke("#FFFFFF")
    bezier_print(pt1, pt2, w, h, x_off, y_off)
    bezier_print(pt3, pt4, w, h, x_off, y_off)

    
def bezier_print(pt1, pt2, w, h, x_off, y_off):
    py5.begin_shape()
    py5.vertex(pt1[0], pt1[1])
    py5.bezier_vertex(
        py5.random(x_off, x_off + w), py5.random(y_off, y_off + h),
        py5.random(x_off, x_off + w), py5.random(y_off, y_off + h),
        pt2[0], pt2[1]
    )
    py5.end_shape()

def mouse_pressed():
    global s 
    s += 1

if __name__ == '__main__':
    py5.run_sketch()


