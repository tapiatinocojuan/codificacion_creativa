import py5

nb = 50;
f_min = 0.7

class Slider():
    def __init__(self, value):
        self.value = value

grados = Slider(0); dim = Slider(0);

def setup():
    py5.size(500, 500)
    py5.rect_mode(py5.CENTER)

def draw():
    global grados, nb, dim, f_min
    py5.background(0)
    py5.translate(py5.width/2, py5.height/2)
    py5.no_fill()
    py5.stroke(255)
    for i in range(nb):
        f = py5.remap(i, 0, nb-1, 1, f_min) 
        py5.square(0, 0, f * dim.value)
        py5.rotate(grados.value*py5.PI/180)

py5.run_sketch()