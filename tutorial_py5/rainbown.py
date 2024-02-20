"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear un arcoiris.
"""
import py5



def setup():
    py5.size(980, 980)
    py5.background('#004477')
    py5.no_stroke()

    colores = [
        '#ff0000', '#ff9900', '#ffff00', '#00ff00', 
        '#0099ff', '#6633ff', '#004477'
    ]
    w = 900
    step = 80
    for color in colores:
        py5.fill(color) # red 
        py5.circle(py5.width/2, py5.height/2, w)
        w -= step
    py5.rect(0, py5.height/2, py5.width, py5.height/2)



    
if __name__ == "__main__":
    py5.run_sketch()