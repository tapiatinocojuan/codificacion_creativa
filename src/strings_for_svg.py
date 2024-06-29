"""Script que trata de emular gotas de agua cayendo"""

import py5
from paleta_colores import colores_purpura_rosa as colores
from os import path
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))
from utilidades import create_video, remove_png

FPS = 30
periodo = 1/FPS
num_puntos = 1000
num_strings_x_color = FPS * 1
puntos = []
margen_porcentual = 10
idx = 0
conteo = 0
num_conteos = 0

COLOR_X_CAPA = 0
TODOS_COLORES_X_CAPA = 1

modo = COLOR_X_CAPA

numeros_primos = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 
    83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 
    179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 
    271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 
    379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 
    479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 
    599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 
    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 
    823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 
    941, 947, 953, 967, 971, 977, 983, 991, 997
)
#numeros_primos2 = (503, 479, 419, 349, 233, 127, 97)
numeros_primos2 = (719, 613, 983, 149, 467, 347, 433)

def setup():
    global puntos, idx, index_incremento, font
    py5.size(720, 1280)
    py5.frame_rate(FPS)
    py5.background(0)
    font = py5.create_font("Impact", 50)
    radio = (py5.width - margen_porcentual/100*py5.width)/2
    delta_angulo = py5.TAU/num_puntos
    angulo = 0
    px = py5.width/2
    py = py5.height/2
    for i in range(num_puntos):
        y = py + py5.sin(angulo)*radio
        x = px + py5.cos(angulo)*radio
        puntos.append((x, y))
        angulo += delta_angulo
    py5.fill(255)
    for punto in puntos:
        py5.circle(punto[0], punto[1], 2)

    idx = py5.random_int(0, num_puntos-1)
    #index_incremento = py5.random_choice(numeros_primos)
    index_incremento = numeros_primos2[0]
    print (index_incremento)

def draw():
    global idx, num_puntos, index_incremento, conteo, font, num_conteos
    py5.begin_record(py5.SVG, "DATA/strings.svg")
    iteraciones = num_strings_x_color*len(colores)*len(numeros_primos2)
    for i in range(iteraciones):
        if modo == TODOS_COLORES_X_CAPA:
            idx_color = (conteo/num_strings_x_color).__floor__()
            if idx_color >= len(colores):
                num_conteos += 1
                if num_conteos == len(numeros_primos2):
                    py5.no_loop()
                    print("Termino de la ejecucion")
                    return
                idx_color = 0
                #index_incremento = py5.random_choice(numeros_primos)
                index_incremento = numeros_primos2[num_conteos]
                conteo = 0
        elif modo == COLOR_X_CAPA:
            idx_color = num_conteos
            if conteo >= num_strings_x_color*len(colores):
                num_conteos += 1
                if num_conteos == len(numeros_primos2) or num_conteos == len(colores):
                    py5.no_loop()
                    print("Termino de la ejecucion")
                    return
                idx_color = num_conteos
                #index_incremento = py5.random_choice(numeros_primos)
                index_incremento = numeros_primos2[num_conteos]
                conteo = 0

        
        py5.stroke(colores[idx_color])
        new_idx = (idx + index_incremento) % num_puntos 

        py5.line(
            puntos[idx][0], puntos[idx][1],
            puntos[new_idx][0], puntos[new_idx][1],
        )
        idx = new_idx
        conteo += 1
    py5.end_record()
    py5.no_loop()
    #py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")

if __name__ == "__main__":
    py5.run_sketch()
    #create_video(RUTA, FPS, f"strings")
    #remove_png(RUTA)

