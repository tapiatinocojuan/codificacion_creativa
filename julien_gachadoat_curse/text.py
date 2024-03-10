"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch .
"""

import py5

font = None; puntos = None

def preload():
    global font
    

def setup():
    global font, puntos
    py5.size(800, 500)
    font = py5.create_font("Roboto-Regular.ttf", 400)
    puntos = []
    for letter in "B":
        shape = font.get_shape(letter)
        aux = []
        for vertex_num in range(shape.get_vertex_count()):
            aux.append(shape.get_vertex(vertex_num))
        puntos.append(aux)
    

def draw():
    global puntos, font
    py5.push_style()
    py5.fill(0)
    py5.pop_style()
    for letter in puntos:
        for i, vertex in enumerate(letter):
            py5.circle(vertex.x + 100, vertex.y + py5.height -100, 10)
            try:
                py5.stroke(0)
                py5.line(
                    vertex.x+100, vertex.y + py5.height -100, 
                    letter[i+1].x + 100, letter[i+1].y + py5.height -100
                )
            except:
                print()
    py5.text_font(font)
    py5.fill(0, 50)
    py5.stroke(0)
    py5.text(f"B", 100, py5.height - 100)


    from ttfquery import describe
    import ttfquery.glyph as glyph
    char = "B"
    font_url ="DATA/Roboto-Regular.ttf"
    font = describe.openFont(font_url)
    g = glyph.Glyph(char) # or g = glyph.Glyph(glyphquery.glyphName(font, char))

    contours = g.calculateContours(font) 
    for contour in contours:
        for i, point in enumerate(contour):
            py5.circle(300+point[0][0]/5, 100+point[0][1]/5, 10)
            try:
                py5.stroke(0)
                py5.line(
                    300+point[0][0]/5, 100+point[0][1]/5, 
                    300+contour[i+1][0][0]/5, 100+contour[i+1][0][1]/5
                )
            except:
                print()

    import freetype
    font = freetype.Face(font_url)
    font.set_char_size(400)
    font.load_char("B")
    import pdb;pdb.set_trace()

    py5.no_loop()

if __name__ == "__main__":
    py5.run_sketch()