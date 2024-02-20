"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Skecth para creación de lineas utilizando el ciclo for
"""
import py5

def setup():
    py5.size(980, 980)
    py5.background(240)

    for n in range(10, 70, 2):
        py5.line(n*10, 100, n*5, 490) 

    margin = 50
    for i in range(20):
        py5.line(margin + i*8, 150, margin + i*16, 600)

if __name__ == "__main__":
    py5.run_sketch()