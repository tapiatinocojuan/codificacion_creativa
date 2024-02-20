"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para realizar un reloj analogico.
"""
import py5

def setup():
    py5.size(600, 600)
    py5.frame_rate(1)
    py5.no_fill()
    py5.stroke('#FFFFFF')
    
def draw():
    py5.background('#004477')
    h = py5.hour()
    m = py5.minute()
    s = py5.second()
    # print( str(h) + ':' + str(m) + ':' + str(s) )
    
    # Translating to the center of the sketch window...
    py5.translate(py5.width/2, py5.height/2)
    
    # Clock face
    py5.stroke_weight(3)
    py5.ellipse(0, 0, 350, 350)
    
    # Hour hand
    py5.rotate(-py5.HALF_PI) # Rotated counterclockwise by HALF_PI

    py5.push_matrix()
    py5.rotate(py5.TAU / 12 * h) # ... and then rotated to the current hour!
    py5.stroke_weight(10)
    py5.line(0, 0, 100, 0)
    py5.pop_matrix()

    py5.push_matrix()
    py5.rotate(py5.TAU / 60 * m) # ... and then rotated to the current hour!
    py5.stroke_weight(7)
    py5.line(0, 0, 120, 0)
    py5.pop_matrix()

    py5.push_matrix()
    py5.rotate(py5.TAU / 60 * s) # ... and then rotated to the current hour!
    py5.stroke_weight(5)
    py5.line(0, 0, 140, 0)
    py5.pop_matrix()
    
py5.run_sketch()