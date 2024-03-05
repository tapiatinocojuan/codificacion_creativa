"""Curso "Intro to Creative Coding: Create Graphic Objects"

Impatido por Julien Gachadoat


Juan Tapia Tinoco 
tapiatinocojuan@gmail.com

Crea archivo vlw para un tipo de letra .
"""

import py5

font = "Great Vibes"; 
puntos = None

for size in [10, 12, 15, 20]:
    py5.create_font_file(font, size, f'{font.replace(" ", "_")}_{size}.vlw', pause=False)