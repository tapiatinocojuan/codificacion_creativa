"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear una imagen con arcos.
"""
import py5

def setup():
    py5.size(500, 500)
    py5.background('#004477')
    py5.stroke(255)
    py5.stroke_weight(3)
    arcos = [
        (400, py5.PI + py5.HALF_PI + 0.5,  py5.TAU - py5.PI/5, "#00FF00"),
        (300,py5.PI, py5.TAU, "#ff96ff"),
        (300,py5.PI, py5.PI+ py5.PI/4, "#ff96ff"),
        (300,py5.PI + py5.HALF_PI + 0.5, py5.TAU, "#0096ff"),
        (300,py5.TAU - 0.5, py5.TAU, "#0096ff"),
        (200,py5.PI , py5.TAU, "#ff2b99"),
        (200, py5.PI + py5.HALF_PI + 0.5 , py5.TAU, "#6620ff"),
        (200, 0 , py5.PI, "#ff0000"),
    ]
    for size, theta_ini, theta_fin, color in arcos:
        py5.fill(color)
        py5.arc(
            py5.width/2, py5.height/2, 
            size, size, theta_ini, theta_fin, py5.PIE
        )
    
    py5.fill('#004477')
    py5.circle(py5.width/2, py5.height/2, 100)
    

if __name__ == "__main__":
    py5.run_sketch()