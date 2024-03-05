"""Curso de codificación creativa con python.

Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Sketch para imprimir los reconocimientos de jornadas.
"""
import py5

concursos = (
   ('Emprendedores Bachi', 'ACADÉMICO', "", ""),
   ('Evaluación Transversal de los Aprendizajes de Trayectoria (Etat)', 'ACADÉMICO', "", ""),
   ('Carrera de Robots', 'ACADÉMICO', "ROBOTICOBAEM", ""),
   ('Seguidores de Línea', 'ACADÉMICO', "ROBOTICOBAEM", ""),
   ('Lucha de Sumo de Robots', 'ACADÉMICO', "ROBOTICOBAEM", ""),
   ('Ciencias Naturales, Exactas y Experimentales', 'ACADÉMICO', "INNOVBACHI", ""),
   ('Ciencias Sociales y Humanidades', 'ACADÉMICO',  "INNOVBACHI", ""),
   ('Pensamiento Matemático I y II', 'ACADÉMICO', "CIENTÍFICOS EN FORMACIÓN", "SEGUNDO SEMESTRE"),
   ('La Materia y sus Interacciones', 'ACADÉMICO', "CIENTÍFICOS EN FORMACIÓN", "SEGUNDO SEMESTRE"),
   ('Matemáticas III y IV (Avanzado)', 'ACADÉMICO', "CIENTÍFICOS EN FORMACIÓN", "CUARTO SEMESTRE"),
   ('Física I y II (Básico)', 'ACADÉMICO', "CIENTÍFICOS EN FORMACIÓN", "CUARTO SEMESTRE"),
   ('Biología I y II (Básico)', 'ACADÉMICO', "CIENTÍFICOS EN FORMACIÓN", "CUARTO SEMESTRE"),
   ('Temas Selectos de Física I y II (Avanzado)', 'ACADÉMICO', "CIENTÍFICOS EN FORMACIÓN", "SEXTO SEMESTRE"),
   ('Biología, Ecología y Medio Ambiente', 'ACADÉMICO', "CIENTÍFICOS EN FORMACIÓN", "SEXTO SEMESTRE"),
   ('Embajadores Bachilleres', 'CULTURAL', "", ""),
   ('Poesía', 'CULTURAL', "", ""),
   ('Cuento', 'CULTURAL', "", ""),
   ('Declamación', 'CULTURAL', "", ""),
   ('Oratoria', 'CULTURAL', "", ""),
   ('Teatro', 'CULTURAL', "", ""),
   ('A jedrez', 'CULTURAL', "", ""),
   ('Pintura', 'CULTURAL', "", ""),
   ('Fotografía Amateur', 'CULTURAL', "", ""),
   ('Escultura', 'CULTURAL', "", ""),
   ('Danza Regional de Michoacán', 'CULTURAL', "", ""),
   ('Baile Regional', 'CULTURAL', "", ""),
   ('Baile Moderno', 'CULTURAL', "", ""),
   ('Cantautores', 'CULTURAL', "", ""),
   ('Canto Individual', 'CULTURAL', "", ""),
   ('Canto por Grupo', 'CULTURAL', "", ""),
   ('Rondallas', 'CULTURAL', "", ""),
   ('Bachirap', 'CULTURAL', "", ""),
   ('Cortometraje Amateur', 'CULTURAL', "", ""),
   ('Señorita Cobaem 2024', 'CULTURAL', "", ""),
   ('Escoltas', 'CÍVICO', "", ""),
   ('Bandas de Guerra', 'CÍVICO', "", ""),
)

def setup():
    py5.size(3506, 2478)
    for concurso, tipo, subtipo, semestre in concursos:
        # if tipo in ["CÍVICO", "CULTURAL"]:
        #     continue
        for lugar in range(1, 4):
            nombre = concurso.lower().replace(" ", "_")
            #if formato == 1:
            #    py5.begin_record(py5.SVG, f"DATA/diplomas/{nombre}_{lugar}.svg")
            grid = py5.load_image('reconocimiento_bachilleres.png')
            py5.image(grid, 0, 0)
            
            if lugar == 3:
                merry = py5.create_font("Merriweather", 275)
                y = 1180
            else:
                merry = py5.create_font("Merriweather", 330)
                y = 1220
            py5.text_font(merry)
            py5.fill(0)
            py5.stroke(0)
            py5.text_align(py5.CENTER)
            py5.text(lugar, 1500, y)


            poppins = py5.create_font("Poppins", 70)
            py5.text_font(poppins)
            py5.fill(0)
            py5.stroke(0)
            py5.text_align(py5.CENTER)
            py5.text(f"EN EL EVENTO {tipo} {subtipo}", 2050, 1350)
            letra = "Great Vibes2"
            if concurso in ["Canto Individual", "La Materia y sus Interacciones"]:
                letra = "Great Vibes"
            great_vibes = calcular_letra(
                concurso, letra, 250, ancho_permitido=2800
            )
            py5.fill(221,172,0)
            py5.stroke(0)
            py5.text_align(py5.CENTER)
            if semestre:
                if semestre.upper() == "SEGUNDO SEMESTRE":
                    py5.text(concurso, 2050, 1730)
                else:
                    py5.text(concurso, 2050, 1710)
            else:
                py5.text(concurso, 2050, 1650)

            great_vibes = calcular_letra(
                semestre.title(), letra, 100, ancho_permitido=2800
            )
            #py5.text(semestre.title(), 2050, 1800)
            py5.text(semestre.title(), 2050, 1480)
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




    

py5.run_sketch()