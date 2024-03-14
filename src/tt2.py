""""Codigo para elaboracion de logo de transformaciones tecnologicas
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""


import py5
s = None

def setup():
    global s
    py5.size(720, 1280)
    s = py5.load_image(r"DATA\firma.png")



def draw():
    py5.image(s, 0, 0)

if __name__ == "__main__":
    py5.run_sketch()