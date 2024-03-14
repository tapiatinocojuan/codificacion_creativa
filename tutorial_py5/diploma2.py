"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para imprimir los reconocimientos de jornadas.
"""
import py5

concursos = (
   ('Huaniqueo'),
   ('Coeneo'),
   ('Quiroga'),
   ('Zacapu'),
   ('CEM Pátzcuaro'),
   ('Cuanajo'),
   ('Sta. Maria Huiramangaro'),
   ('San Fco. Pichátaro'),
   ('Santa Clara del Cobre'),
   ('Ario de Rosales'),
   ('Huiramba'),
   (''),
   
)

def setup():
    py5.size(3506, 2478)
    evento = "Mujeres Cobaem: Voces que Construyen Cambios"
    for plantel in concursos:
        nombre = plantel.lower().replace(" ", "_")
        grid = py5.load_image('reconocimiento_bachilleres_2.png')
        py5.image(grid, 0, 0)
        

        if plantel:
            texto1 = f"A LA MUJER COBAEM DEL PLANTEL {plantel.upper()}"
            texto2 = f"POR SU DESTACADA PARTICIPACIÓN"
            texto3 = f"EN EL EVENTO CULTURAL"
        else:
            texto1 = f"A LA MUJER COBAEM REPRESENTANTE DE LA"
            texto2 = f"COORDINACIÓN SECTORIAL 04 PÁTZCUARO"
            texto3 = f"EN EL EVENTO CULTURAL"
        letra = "Merriweather"
        
        merriweather = calcular_letra(
            texto1, letra, 70, ancho_permitido=1800
        )
        py5.text_font(merriweather)
        py5.fill(0)
        py5.stroke(0)
        py5.text_align(py5.CENTER)
        py5.text(texto1, 2050, 1100)

        merriweather = calcular_letra(
            texto2, letra, 70, ancho_permitido=1800
        )
        py5.text_font(merriweather)
        py5.fill(0)
        py5.stroke(0)
        py5.text_align(py5.CENTER)
        py5.text(texto2, 2050, 1200)


        poppins = py5.create_font("Poppins", 70)
        py5.text_font(poppins)
        py5.fill(0)
        py5.stroke(0)
        py5.text_align(py5.CENTER)
        py5.text(texto3, 2050, 1350)
        
        
        letra = "Great Vibes"
        great_vibes = calcular_letra(
            evento, letra, 250, ancho_permitido=2800
        )
        py5.fill(221,172,0)
        py5.stroke(0)
        py5.text_align(py5.CENTER)
        py5.text(evento, 2050, 1650)

        if nombre:
            py5.save_frame(f"DATA/diplomas/{nombre}.jpg")
        else:
            py5.save_frame(f"DATA/diplomas/ganador.jpg")

def calcular_letra(titulo, fuente, tamanio_original, ancho_permitido=2000):
    great_vibes = py5.create_font(fuente, tamanio_original)
    py5.text_font(great_vibes)
    tam = py5.text_width(titulo)
    while (tam > ancho_permitido):
        tamanio_original -= 1
        great_vibes = py5.create_font(fuente, tamanio_original)
        py5.text_font(great_vibes)
        tam = py5.text_width(titulo)
    return great_vibes




    

py5.run_sketch()