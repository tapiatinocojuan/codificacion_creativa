"""
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear curvas
"""
import py5

def setup():
    py5.size(1000, 1000)
    grid = py5.load_image('grid.png')
    py5.image(grid, 0, 0)
    py5.no_fill()
    py5.stroke_weight(3)

    py5.stroke('#0099FF') # pale blue
    #line(100,100, 400,400)
    py5.curve(0,0, 100,100, 400,400, 500,500)

    py5.stroke('#FFFF00') # yellow
    py5.curve(0,250, 100,100, 400,400, 500,250)

    py5.stroke('#FF9900') # orange
    # control point 1:
    py5.curve(0,250, 0,250, 100,100, 400,400)
    # control point 2:
    py5.curve(100,100, 400,400, 500,250, 500,250)

    py5.stroke('#11CC88') # mint green
    # ellipses at the control points for our yellow curve! 
    py5.ellipse(0, 250, 20, 20)
    py5.ellipse(500, 250, 20, 20)

    step = 0.1
    tighteness = -5
    for i in range(int(10/step)):
        if tighteness < 0:
            py5.stroke('#00FF00') #green
        else:
            py5.stroke('#0000FF') #blue
        py5.curve_tightness(tighteness)
        py5.curve(100,100, 300,500, 600,600, 500,250)
        tighteness += step 

if __name__ == '__main__':
    py5.run_sketch()