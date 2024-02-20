"""
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para crear texto
"""
import py5

def setup():
    py5.size(500, 500)
    py5.background('#004477')
    py5.fill("#FFFFFF")
    py5.stroke("#0099FF")
    py5.stroke_weight(3)

    razor = "Nunca atribuyas a la malicia a los que adecuadamente descrito por la estupidez"
    #py5.text(razor, 0,5, 100, 1000)

    py5.text(razor, 0, 50)
    py5.text_size(20)
    py5.text(razor, 0, 100)

    #print ( py5.Py5Font.list() ) 
    verdana = py5.create_font("Verdana", 20)
    py5.text_font(verdana)
    py5.text(razor, 0, 150)

    py5.text_leading(10)
    py5.text(razor, 0, 200, 250, 100)

    py5.text_align(py5.CENTER)
    py5.text(razor, 0,250,250,100)

    py5.text_align(py5.LEFT)
    hanlons = "- Hanlon's razor"
    py5.text(hanlons, 250, 350)
    py5.line( 250, 325, 250, 375)
    py5.line( 
        250 + py5.text_width(hanlons), 325, 
        250 + py5.text_width(hanlons), 375
    )

if __name__ == "__main__":
    py5.run_sketch()