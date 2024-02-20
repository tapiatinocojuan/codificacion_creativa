"""
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear el antiguo logo de apple
"""
import py5

def setup():
    py5.size(800, 800)
    #py5.begin_record(py5.SVG, f"output.svg")
    grid = py5.load_image('grid.png')
    py5.image(grid, 0, 0)
    py5.no_fill()
    py5.no_stroke()

    py5.fill("#5ebd3e")
    py5.rect(0, 0, py5.width, 280)
    py5.fill("#ffb900")
    py5.rect(0, 280, py5.width, 100)
    py5.fill("#f78200")
    py5.rect(0, 380, py5.width, 100)
    py5.fill("#e23838")
    py5.rect(0, 480, py5.width, 100)
    py5.fill("#973999")
    py5.rect(0, 580, py5.width, 100)
    py5.fill("#009cdf")
    py5.rect(0, 680, py5.width, 120)

    py5.fill(255)
    py5.begin_shape()
    py5.vertex(0,0)
    py5.vertex(0,py5.height)
    py5.vertex(py5.width,py5.height)
    py5.vertex(py5.width,0)
    py5.begin_contour()
    py5.vertex(400,750) # starting (upper) vertex
    py5.bezier_vertex(320,750, 280,830, 180,750)
    py5.bezier_vertex(110,690, 60,560, 50, 480)
    py5.bezier_vertex(30,270, 160,190, 260, 190)
    py5.bezier_vertex(320,190, 320,220, 400, 220)
    py5.bezier_vertex(480,220, 480,190, 540, 190)
    py5.bezier_vertex(640,190, 770,270, 750, 480)
    py5.bezier_vertex(740,560, 690,690, 620,750)
    py5.bezier_vertex(520,830, 480,750, 400,750)
    py5.end_contour()
    py5.end_shape()

    py5.fill(255)
    py5.ellipse(720,410,200,300)

    py5.fill("#5ebd3e")
    py5.begin_shape()
    py5.vertex(380,200)
    py5.bezier_vertex(500, 200, 520, 50, 520, 10)
    py5.bezier_vertex(430, 30, 380, 100, 380, 200)
    py5.end_shape()
    

if __name__ == '__main__':
    py5.run_sketch()