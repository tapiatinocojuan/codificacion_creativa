"""
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear curvas
"""
import py5

def setup():
    py5.size(800, 800)
    grid = py5.load_image('grid.png')
    py5.image(grid, 0, 0)
    py5.no_fill()
    py5.stroke_weight(3)

    py5.stroke('#FF99FF') # pink
    cp1x = 250
    cp1y = 150 # pulled up slightly...
    cp2x = 300
    cp2y = 350
    py5.bezier(400,100, cp1x,cp1y, cp2x,cp2y, 100,400)

    py5.stroke('#11CC88') # mint green
    # ellipses at the control points for our Bézier curve! 
    py5.ellipse(cp1x, cp1y, 20, 20)
    py5.ellipse(cp2x, cp2y, 20, 20)

    py5.stroke('#FF0000') # red
    # line connecting a control point to the first vertex of the curve!
    py5.line(400,100, cp1x,cp1y)
    py5.line(100,400, cp2x,cp2y)

if __name__ == '__main__':
    py5.run_sketch()