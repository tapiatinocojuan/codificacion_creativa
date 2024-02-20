"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para realizar transformaciones.
"""
import py5

def setup():
    py5.size(800, 800)

    py5.no_fill()
    py5.stroke('#FFFFFF')
    py5.stroke_weight(3)

    x = 400; y = 200
    w = 200; h = 200

    py5.rect(x,y, w,h)

    # The translate() function makes things so easy...
    py5.translate(100,-80)
    py5.rotate(py5.PI/10)
    py5.scale(0.5)

    py5.stroke('#FFFF00')
    py5.rect(x,y, w,h)

    # So where will this square end up?
    py5.stroke('#FF0000')
    py5.rect(0,0, 100,100)

py5.run_sketch()