"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para mostrar el uso grillas.
"""

import py5
import py5_tools

nc = 50
x_off = 20
y_off = 20
width = None; height = None
fps = 10
ts = 1/fps
f = -0.2
w = py5.TAU*f
dist_max = None
duracion_gif = 5


def setup():
    global width, height, x_off, y_off, fps, dist_max
    py5.size(500, 500)
    py5.frame_rate(fps)
    width = (py5.width-2*x_off)/nc
    height = (py5.height-2*y_off)/nc
    dist_max = py5.dist(0, 0, py5.width, py5.height)

def draw():
    global nc, width, height, x_off, y_off, w, ts, dist_max
    py5.background(0)
    py5.no_stroke()
    py5.fill(255)
    #py5.stroke(255)
    #py5.no_fill()
    py5.rect_mode(py5.CENTER)
    
    for i in range(nc):
        for j in range(nc):
            x = x_off + width/2 + i*width
            y = y_off + height/2 + j*height
            mod = py5.sin(
                w*ts*py5.frame_count 
                + 2*py5.dist(py5.mouse_x, py5.mouse_y, x, y)/dist_max*py5.TAU
            )
            py5.ellipse(
                x, 
                y, 
                mod*width, 
                mod*height
            )
            # py5.rect(
            #     x_off + width/2 + i*width, 
            #     y_off +height/2 + j*height, 
            #     width*0.9, height*0.9
            # )

if __name__ == "__main__":
    print(ts)
    py5_tools.animated_gif(
        filename = r'DATA\animated.gif', 
        frame_numbers= range(int(fps*duracion_gif)), 
        duration = ts/100
    )
    py5.run_sketch()
