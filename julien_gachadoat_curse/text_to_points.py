""" Codigo base tomado de : 

https://github.com/rougier/freetype-py/blob/master/examples/glyph-vector.py

freetype-py is licensed under the terms of the new or revised BSD license, as
follows:

Copyright (c) 2011-2014, Nicolas P. Rougier
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.

Neither the name of the freetype-py Development Team nor the names of its
contributors may be used to endorse or promote products derived from this
software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from freetype import *
import numpy
from matplotlib import pyplot as plt
import py5

def text_to_points(x0, y0, text, font, size, t, espaciado=0.1):
    """Obtiene una serie de puntos del contorno del string en text"""
    puntos = []
    for letter in text:
        verts, codes, width = get_verts_and_codes(font, letter, size)
        pts = get_points(verts, codes, t, size)
        xs, ys = zip(*pts)
        x_min = min(xs)
        x_max = max(xs)
        y_min = min(ys)
        puntos.extend([(x+x0, y+y0) for x, y in pts])
        x0 = x0 + width + espaciado
        print (width, x_max - x_min)
    
    return puntos



def get_points(verts, codes, t, size):
    i = 0
    puntos = []
    while (i < len(codes)):
        code = codes[i]
        if code == 2:
            puntos.extend(linear_bezier(verts[i-1], verts[i], t, size))
        elif code == 3:
            puntos.extend(cuadratic_bezier(verts[i-1], verts[i], verts[i+1], t, size))
            i += 1
        i += 1
    return puntos
        
def get_verts_and_codes(font, letter, size):
    face = Face(font)
    face.set_char_size( size )
    face.load_char(letter)
    slot = face.glyph
    advance = face.get_advance(face.get_char_index(letter), face.face_flags)
    outline = slot.outline
    bbox = outline.get_bbox()
    width = bbox.xMax - bbox.xMin
    start, end = 0, 0

    VERTS, CODES = [], []
    for i in range(len(outline.contours)):
        end    = outline.contours[i]
        points = outline.points[start:end+1]
        points.append(points[0])
        tags   = outline.tags[start:end+1]
        tags.append(tags[0])

        segments = [ [points[0],], ]
        for j in range(1, len(points) ):
            segments[-1].append(points[j])
            if tags[j] & (1 << 0) and j < (len(points)-1):
                segments.append( [points[j],] )
        verts = [points[0], ]
        codes = [1,]
        for segment in segments:
            if len(segment) == 2:
                verts.extend(segment[1:])
                codes.extend([2])
            elif len(segment) == 3:
                verts.extend(segment[1:])
                codes.extend([3, 3])
            else:
                verts.append(segment[1])
                codes.append(3)
                for i in range(1,len(segment)-2):
                    A,B = segment[i], segment[i+1]
                    C = ((A[0]+B[0])/2.0, (A[1]+B[1])/2.0)
                    verts.extend([ C, B ])
                    codes.extend([ 3, 3])
                verts.append(segment[-1])
                codes.append(3)
        VERTS.extend(verts)
        CODES.extend(codes)
        start = end+1

    return VERTS, CODES, width


def calcular_segmento(points):
    """Calcula el tamaño de un segmento a partir de la distancia entre sus puntos"""
    distancia = 0
    for i, point in enumerate(points[:-2]):
        distancia += py5.dist(point[0], point[1], points[i+1][0], points[i+1][1])
    return distancia

def linear_bezier(p0, p1, step = 1, flag=1, size=100):
    """Calcula una curva berzier de grado 1 entre 2 puntos
    
    B(t) = P0 + t(P1 - P0) = (1-t) P0 + tP1 , 0 < t < 1
    """
    if flag:
        st = 0.01
    else:
        if step < 0:
            st = 0.000001
        elif step > 1:
            st = 1 
        else:
            st = step
    points = []
    t = 0
    while (t < 1):
        x = (1-t)* p0[0] + t*p1[0]
        y = -((1-t)* p0[1] + t*p1[1])
        points.append((x, y))
        t += st
    if flag:
        distancia = calcular_segmento(points)
        step = step*size/distancia
        print (f"{distancia}, {step}, {1/step}")
        points = linear_bezier(p0, p1, step, 0)
    
    return points

def cuadratic_bezier(p0, p1, p2, step=1, flag=1, size=100):
    """Calcula una curva berzier de grado 2 entre 3 puntos
    
    B(t) = (1-t)**2P0 + 2(1-t)tP1 + t**2P2 , 0 < t < 1
    """
    if flag:
        st = 0.01
    else:
        if step < 0:
            st = 0.000001
        elif step > 1:
            st = 1 
        else:
            st = step
    points = []
    t = 0
    while (t < 1):
        x = (1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t**2*p2[0]
        y = -((1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t**2*p2[1])
        points.append((x, y))
        t += st
    if flag:
        distancia = calcular_segmento(points)
        step = step*size/distancia
        print (f"{distancia}, {step}, {1/step}")
        points = cuadratic_bezier(p0, p1,p2, step, 0)

    return points

if __name__ == "__main__":
    font_path = "DATA/GreatVibes-Regular.ttf"
    letter = "A"
    size = 100
    t = 0.1 
    puntos = text_to_points(100, 100,letter,font_path,size, 0.05, 0)
    x, y = zip(*puntos)
    plt.plot(x, y, "g:*")
    plt.grid()
    plt.show()

