"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear el simbolo iluminati.
"""
import py5



def setup():
    py5.size(600, 740)
    py5.background('#004477')
    py5.no_fill()
    py5.stroke('#FFFFFF')
    py5.stroke_weight(3)

    xco = 400
    yco = 440
    py5.line(py5.width/2,py5.height/3, xco,yco)
    """Draw a centred ellipse with a width that’s an eleventh of 
    the display window width, and a height that’s a fourteenth 
    of the window height.
    """
    py5.ellipse(py5.width/2, py5.height/2, py5.width/11, py5.height/14)
    """Draw a centred ellipse with a width that’s a nineteenth of 
    the display window width, and a height that’s a twenty-second 
    of the window height.
    """
    py5.ellipse(py5.width/2, py5.height/2, py5.width/19, py5.height/22)
    """Draw a line beginning at an x/y-coordinate equal to xco & yco 
    respectively. The endpoint must have an x-coordinate of the display 
    window width minus xco, and a y-coordinate equal to yco.
    """
    py5.line(xco,yco, py5.width-xco, yco)
    """Draw a line beginning at an x-coordinate of the display window width 
    minus xco, and y-coordinate equal to yco. The endpoint must have an 
    x-coordinate of half the display window width, and a y-coordinate of a 
    third of the window height."""
    py5.line(py5.width-xco, yco, py5.width/2, py5.height/3)
    """Draw a centred ellipse with a width that’s a fifth of the display 
    window width, and height that’s a twelfth of the display window height.
    """
    py5.ellipse(py5.width/2, py5.height/2, py5.width/5, py5.height/12)
    
if __name__ == "__main__":
    py5.run_sketch()