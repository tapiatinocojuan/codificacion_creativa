"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para cargar una imagen.
"""
import py5

def setup():
    py5.size(900, 900)
    img = py5.load_image('sailor_moon.png')
    py5.image(img, 0, 0, py5.width, py5.height)
    py5.no_fill()
    py5.stroke_weight(3)

if __name__ == "__main__":
    py5.run_sketch()