"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Prueba de creacion de imagenes con letras animadas.
"""
import py5
from letters import letters

BACKGROUND = "#000000"

def setup():
    py5.size(500, 500)
    py5.background("#FF0000")
    dibujar_letra(100, 100, 100, 300, "S", BACKGROUND)

def dibujar_letra(x_ini, y_ini, w, h, letra, bg_color):
    """Dibuja una letra en modo transparencia sobre un fondo"""
    escale_x = w/100
    escale_y = h/100

    py5.fill(bg_color)
    py5.stroke(bg_color)
    py5.push_matrix()
    py5.translate(x_ini, y_ini)
    py5.scale(escale_x, escale_y)

    py5.begin_shape()
    py5.vertex(0, 0)
    py5.vertex(100, 0)
    py5.vertex(100, 100)
    py5.vertex(0, 100)
    py5.vertex(0, 0)
    py5.begin_contour()
    for point in letters[letra]:
        if len(point) == 2:
            py5.vertex(*point)
        else:
            py5.bezier_vertex(*point)
    py5.end_contour()
    py5.end_shape(py5.CLOSE)
    py5.pop_matrix()


if __name__ == "__main__":
    py5.run_sketch()


    