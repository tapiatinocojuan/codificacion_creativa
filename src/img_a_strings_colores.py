""""Codigo para remplazar pixeles con glifos en imagenes
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""
import py5
from PIL import Image
import numpy as np
import colorsys
imagen_path = 'DATA/hierbe_elagua.jpg'
im = Image.open(imagen_path)
factor_escala = 0.1 #Imagenes grande
#factor_escala = 0.2
import sys
from os import path
sys.path.append(path.abspath(path.join(__file__, '../../src')))
RUTA = path.abspath(path.join(__file__, '../DATA/animacion'))

#tipo de letra hughlove
simbolos = [
        (46, 0.039562560308780956),
        (39, 0.05435831457060148),
        (44, 0.05467996140238019),
        (45, 0.06046960437439692),
        (96, 0.06239948536506915),
        (58, 0.0784818269540045),
        (95, 0.08009006111289803),
        (43, 0.0874879382438083),
        (59, 0.09456416854293985),
        (61, 0.10324863300096493),
        (34, 0.1106465101318752),
        (42, 0.1157928594403345),
        (94, 0.13284014152460602),
        (126, 0.15792859440334514),
        (105, 0.2434866516564812),
        (62, 0.26214216789964623),
        (60, 0.263428755226761),
        (33, 0.2721132196847861),
        (114, 0.2811193309745899),
        (108, 0.3255065937600514),
        (115, 0.3367642328723062),
        (49, 0.35188163396590544),
        (124, 0.35541974911547125),
        (122, 0.3608877452557092),
        (73, 0.37021550337729175),
        (47, 0.37471855902219364),
        (92, 0.37536185268575106),
        (118, 0.377613380508202),
        (120, 0.38243808298488263),
        (106, 0.4097780636860728),
        (99, 0.43229334191058216),
        (110, 0.43229334191058216),
        (102, 0.4342232229012544),
        (101, 0.4377613380508202),
        (125, 0.43936957220971373),
        (123, 0.44001286587327115),
        (116, 0.44129945320038594),
        (40, 0.4509488581537472),
        (41, 0.45159215181730455),
        (76, 0.45673850112576386),
        (117, 0.47089096172402706),
        (55, 0.4747507237053716),
        (93, 0.4747507237053716),
        (91, 0.4750723705371502),
        (52, 0.4808620135091669),
        (89, 0.5040205853972338),
        (97, 0.5075587005467996),
        (63, 0.5123834030234802),
        (51, 0.5255709231264072),
        (70, 0.5284657446124156),
        (111, 0.5323255065937601),
        (50, 0.5326471534255387),
        (98, 0.5422965583789),
        (107, 0.5461563203602444),
        (88, 0.5577356063042779),
        (104, 0.5599871341267288),
        (84, 0.5689932454165327),
        (53, 0.5738179478932133),
        (37, 0.5767127693792216),
        (67, 0.5767127693792216),
        (100, 0.5905435831457061),
        (113, 0.5985847539401736),
        (86, 0.6108073335477646),
        (112, 0.6236732068189128),
        (35, 0.6243165004824702),
        (54, 0.624638147314249),
        (119, 0.6400771952396269),
        (57, 0.6522997748472178),
        (80, 0.6551945963332261),
        (48, 0.6622708266323577),
        (109, 0.6648440012865873),
        (36, 0.6664522354454808),
        (56, 0.675136699903506),
        (74, 0.6793181087166291),
        (69, 0.680604696043744),
        (90, 0.6867159858475393),
        (103, 0.6950788034737858),
        (75, 0.6954004503055645),
        (83, 0.706979736249598),
        (121, 0.7076230299131554),
        (79, 0.7391444194274687),
        (65, 0.7413959472499196),
        (68, 0.7420392409134771),
        (78, 0.7616596976519782),
        (85, 0.7690575747828884),
        (66, 0.7873914441942748),
        (38, 0.8163396590543583),
        (82, 0.8263107108394983),
        (72, 0.8337085879704085),
        (81, 0.8394982309424253),
        (77, 0.8861370215503378),
        (71, 0.9376005146349308),
        (87, 0.9723383724670313),
        (64, 1.0),
]

def setup():
    global img, pixeles, font, pixeles_colors_h,pixeles_colors_s, pixeles_colors_v, pixeles_no_print
    py5.size(im.size[0], im.size[1])
    img = py5.load_image(imagen_path)
    #img.apply_filter(py5.GRAY)
    #img.apply_filter(py5.THRESHOLD, 0.9)
    img.load_np_pixels()
    pixels = img.np_pixels
    font = py5.create_font(r"Huglove", 1)
    pixeles = np.zeros((py5.width, py5.height))
    pixeles_colors_h = np.zeros((py5.width, py5.height))
    pixeles_colors_s = np.zeros((py5.width, py5.height))
    pixeles_colors_v = np.zeros((py5.width, py5.height))
    pixeles_no_print = np.ones((py5.width, py5.height))
    for i, row in enumerate(pixels):
        for j, cell in enumerate(row):
            alpha, red, green, blue  = cell
            lum = 0.2126*red/255 + 0.7152*green/255 + 0.0722*blue/255
            lum = lum*alpha/255
            pixeles[j][i] = (1-lum)
            h, s, v = colorsys.rgb_to_hsv(red/255, green/255, blue/255)
            pixeles_colors_h[j][i] = h
            pixeles_colors_s[j][i] = s
            pixeles_colors_v[j][i] = v
            if alpha == 0:
                pixeles_no_print[j][i] = 0
    pixeles = promediar_matriz(pixeles, factor_escala)
    pixeles_colors_h = promediar_matriz(pixeles_colors_h, factor_escala)
    pixeles_colors_s = promediar_matriz(pixeles_colors_s, factor_escala)
    pixeles_colors_v = promediar_matriz(pixeles_colors_v, factor_escala)
    pixeles_no_print = promediar_matriz(pixeles_no_print, factor_escala)
    #print()

def draw():
    global img, pixeles, pixeles_colors_h,pixeles_colors_s, pixeles_colors_v, pixeles_no_print, font
    py5.begin_record(py5.SVG, f"DATA/{path.basename(imagen_path).split(".")[0]}.svg")
    py5.background(255)
    py5.text_font(font)
    py5.scale(1/factor_escala)
    py5.text_align(py5.CENTER)
    py5.no_stroke()
    py5.fill("#3AD400")
    for i, renglon in enumerate(pixeles):
        for j, cell in enumerate(renglon):        
            py5.text_align(py5.CENTER, py5.CENTER)
            try:
                if pixeles_no_print[i][j] <= 0.5:
                    continue
                r, g, b = colorsys.hsv_to_rgb(
                    pixeles_colors_h[i][j],
                    pixeles_colors_s[i][j],
                    pixeles_colors_v[i][j],
                )
                py5.stroke(int(r*255), int(g*255), int(b*255))
                py5.fill(r*255, g*255, b*255)
                py5.stroke_weight(cell*0.25)
                py5.line(i, j, i-1, j+1)
                py5.line(i, j, i-1, j)
                py5.line(i, j, i-1, j-1)
                py5.line(i, j, i, j-1)
                py5.line(i, j, i, j+1)
                py5.line(i, j, i+1, j+1)
                py5.line(i, j, i+1, j)
                py5.line(i, j, i+1, j-1)
            except:
                import pdb; pdb.set_trace()
    py5.end_record()
    py5.save_frame(f"{RUTA}/{py5.frame_count:05d}.png")
    py5.no_loop()

def get_gliph(valor):
    global simbolos
    
    if valor <= simbolos[0][1]:
        return chr(simbolos[0][0])
    if valor >= simbolos[-1][1]:
        return chr(simbolos[-1][0])
    for i, ( _, threshold) in enumerate(simbolos):
        if valor < threshold:
            return chr(simbolos[i-1][0])


def promediar_matriz(matriz, factor):
    x_size = len(matriz)
    y_size = len(matriz[0])
    paso_x = int(1/factor)
    paso_y = int(1/factor)
    new_size_x = x_size//paso_x
    new_size_y = y_size//paso_y
    new_matriz = np.zeros((new_size_x, new_size_y))
    for i in range(new_size_x):
        for j in range(new_size_y):
            new_matriz[i][j] = np.average(matriz[paso_x*i:paso_x*(i+1), paso_y*j:paso_y*(j+1)])
    return new_matriz


if __name__ == "__main__":
    py5.run_sketch()    


