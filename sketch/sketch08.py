"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear el circulo circunscrito de un triangulo.
"""
import py5
import utilidades

def setup():
    py5.size(980, 980)
    p0 = 200, 200
    p1 = 400, 400
    p2 = 500, 700
    
    xc, yc, r = utilidades.calcula_circulo_circunscrito([p0, p1, p2])
    utilidades.calcula_circulo_circunscrito([p1, p2, p0])
    utilidades.calcula_circulo_circunscrito([p2, p0, p1])

    r1 = utilidades.calcular_distancia((xc, yc), p0)
    r2 = utilidades.calcular_distancia((xc, yc), p1)
    r3 = utilidades.calcular_distancia((xc, yc), p2)
    py5.circle(xc, yc, r*2)
    print (r, r1, r2, r3)

    py5.line(p0[0], p0[1], p1[0], p1[1]) 
    py5.line(p1[0], p1[1], p2[0], p2[1]) 
    py5.line(p2[0], p2[1], p0[0], p0[1]) 
    


    




if __name__ == "__main__":
    py5.run_sketch()