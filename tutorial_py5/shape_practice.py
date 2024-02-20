"""
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear curvas
"""
import py5

def setup():
    py5.size(800,800)
    py5.begin_record(py5.SVG, "borrar.svg")
    grid = py5.load_image('grid.png')
    beziers = py5.load_image('beziers.png')
    py5.image(grid, 0, 0)
    py5.image(beziers, 0, 0)
    py5.no_fill()
    py5.stroke('#FFFFFF')
    py5.stroke_weight(3)

    py5.begin_shape()
    py5.vertex(180, 120)
    py5.bezier_vertex(120,220, 320, 250, 270, 320)
    py5.end_shape()

    py5.begin_shape()
    py5.vertex(460, 120)
    py5.bezier_vertex(460,280, 700, 280, 650, 130)
    py5.end_shape()

    py5.begin_shape()
    py5.vertex(260, 460)
    py5.bezier_vertex(210, 720, 60,470, 330, 570)
    py5.end_shape()
    py5.end_record()


    py5.begin_shape()
    py5.vertex(480,616)
    py5.bezier_vertex(568, 723, 706, 616, 590, 513 )
    py5.bezier_vertex(481, 413, 654, 383 ,671, 496)
    py5.end_shape()

if __name__ == '__main__':
    py5.run_sketch()