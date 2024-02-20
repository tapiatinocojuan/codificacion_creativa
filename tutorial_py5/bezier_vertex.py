"""
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear curvas (vertices)
"""
import py5

def setup():
    py5.size(800, 800)
    grid = py5.load_image('grid.png')
    py5.image(grid, 0, 0)
    py5.no_fill()
    py5.stroke_weight(3)

    #Forma de s
    py5.begin_shape()
    py5.vertex(400,200) # starting (upper) vertex
    py5.bezier_vertex(
        300,300, # control point for the starting vertex
        500,500, # control point for the second (lower) vertex
        400,600  # second (lower) vertex coordinates
    )
    py5.end_shape()

    #Forma de corazon 
    py5.begin_shape()
    py5.vertex(600,400)
    py5.bezier_vertex(420,300, 550,150, 600,250)
    py5.bezier_vertex(650,150, 780,300, 600,400) # What goes here?
    py5.end_shape()

    #Moneda china
    py5.fill('#6633FF')
    py5.begin_shape()
    py5.vertex(100,600)
    py5.bezier_vertex(100,545, 145,500, 200,500)
    py5.bezier_vertex(255,500, 300,545, 300,600)
    py5.bezier_vertex(300,655, 255,700, 200,700)
    py5.bezier_vertex(145,700, 100,655, 100,600)
    py5.begin_contour()
    py5.vertex(180,580)
    py5.vertex(180,620)
    py5.vertex(220,620)
    py5.vertex(220,580)
    py5.end_contour()
    py5.end_shape()

if __name__ == '__main__':
    py5.run_sketch()