"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Interfaz que dibuja circulos en el lugar donde detecta el
puntero del ratón.
"""
import py5

def setup():
    py5.size(980, 980)

def draw():
    py5.ellipse(py5.mouse_x, py5.mouse_y, 30, 30)

if __name__ == "__main__":
    py5.run_sketch()