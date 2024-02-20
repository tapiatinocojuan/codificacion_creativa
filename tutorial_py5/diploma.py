"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para imprimir los reconocimientos de jornadas.
"""
import py5

concursos = (
   ('Emprendedores Bachi', 'ACADEMICO', 0),
   ('Evaluación Transversal de los Aprendizajes de Trayectoria (Etat)', 'ACADEMICO', 0),
   ('Carrera de Robots', 'ACADEMICO', 0),
   ('Seguidores de Línea', 'ACADEMICO', 0),
   ('Lucha de Sumo de Robots', 'ACADEMICO', 0),
   ('Ciencias Naturales, Exactas y Experimentales', 'ACADEMICO', 0),
   ('Ciencias Sociales y Humanidades', 'ACADEMICO', 0),
   ('Pensamiento Matematico I y II', 'ACADEMICO', 1),
   ('La Materia y sus Interacciones', 'ACADEMICO', 0),
   ('Matemáticas III y IV (Avanzado)', 'ACADEMICO', 1),
   ('Fisica I y II (Básico)', 'ACADEMICO', 1),
   ('Biología I y II (Básico)', 'ACADEMICO', 1),
   ('Temas Selectos de Física I y II (Avanzado)', 'ACADEMICO', 1),
   ('Biología, Ecología y Medio Ambiente', 'ACADEMICO', 0),
   ('Embajadores Bachilleres', 'CULTURAL', 0),
   ('Poesía', 'CULTURAL', 0),
   ('Cuento', 'CULTURAL', 0),
   ('Declamación', 'CULTURAL', 0),
   ('Oratoria', 'CULTURAL', 0),
   ('Teatro', 'CULTURAL', 0),
   ('Ajedrez', 'CULTURAL', 0),
   ('Pintura', 'CULTURAL', 0),
   ('Fotografía Amateur', 'CULTURAL', 0),
   ('Escultura', 'CULTURAL', 0),
   ('Danza Regional de Michoacán', 'CULTURAL', 0),
   ('Baile Regional', 'CULTURAL', 0),
   ('Baile Moderno', 'CULTURAL', 0),
   ('Cantautores', 'CULTURAL', 0),
   ('Canto Individual', 'CULTURAL', 0),
   ('Canto por Grupo', 'CULTURAL', 0),
   ('Rondallas', 'CULTURAL', 0),
   ('Bachirap', 'CULTURAL', 0),
   ('Cortometraje Amateur', 'CULTURAL', 0),
   ('Señorita Cobaem 2024', 'CULTURAL', 0),
   ('Escoltas', 'CÍVICO', 0),
   ('Bandas de Guerra', 'CÍVICO', 0),

)

def setup():
    py5.size(3506, 2478)
    for concurso, tipo, formato in concursos:
        for lugar in range(1, 4):
            nombre = concurso.lower().replace(" ", "_")
            #if formato == 1:
            #    py5.begin_record(py5.SVG, f"DATA/diplomas/{nombre}_{lugar}.svg")
            grid = py5.load_image('reconocimiento_bachilleres.png')
            py5.image(grid, 0, 0)
            merry = py5.create_font("Merriweather", 330)
            py5.text_font(merry)
            py5.fill(0)
            py5.stroke(0)
            py5.text_align(py5.CENTER)
            py5.text(lugar, 1500, 1220)
            poppins = py5.create_font("Poppins", 70)
            py5.text_font(poppins)
            py5.fill(0)
            py5.stroke(0)
            py5.text_align(py5.CENTER)
            py5.text(f"EN EL EVENTO {tipo}", 2050, 1400)
            letra = "Great Vibes2"
            if concurso in ["Canto Individual", "La Materia y sus Interacciones"]:
                letra = "Great Vibes"
            great_vibes = calcular_letra(
                concurso, letra, 250, ancho_permitido=2800
            )
            py5.fill(221,172,0)
            py5.stroke(0)
            py5.text_align(py5.CENTER)
            py5.text(concurso, 2050, 1700)
            #if formato == 1:
            #    py5.end_record()
            #else:
            py5.save_frame(f"DATA/diplomas/{nombre}_{lugar}.jpg")
    

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


for concurso, tipo, _ in concursos:
    print (f"   ('{concurso.title()}', '{tipo}'),")


    

py5.run_sketch()