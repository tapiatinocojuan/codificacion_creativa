"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch donde se utilizan figuras básicas como la elipse
y el rectangulo.
"""
import py5

def setup():
    py5.size(980, 980)
    py5.background(200, 0, 200)
    py5.rect_mode(py5.CENTER)
    #Diseño de rectangulo
    py5.fill(0, 200, 0)
    py5.stroke(255, 0, 0)
    py5.stroke_weight(5)
    py5.rect(py5.width/2,py5.height/2, 200, 50)
    
    #Diseño de la elipse    
    py5.no_stroke()
    py5.fill(255)
    py5.ellipse(200, 200, 300, 100)

if __name__ == "__main__":
    py5.run_sketch()