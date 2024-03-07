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


def text_to_points(font, letter, size):
    face = Face(font)
    face.set_char_size( size )
    face.load_char(letter)
    slot = face.glyph

    bitmap = face.glyph.bitmap
    width  = face.glyph.bitmap.width
    rows   = face.glyph.bitmap.rows
    pitch  = face.glyph.bitmap.pitch

    data = []
    for i in range(rows):
        data.extend(bitmap.buffer[i*pitch:i*pitch+width])
    Z = numpy.array(data,dtype=numpy.ubyte).reshape(rows, width)

    outline = slot.outline
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

    return VERTS, CODES


def linear_bezier(p0, p1, num_puntos = 5):
    """Calcula una curva berzier de grado 1 entre 2 puntos
    
    B(t) = P0 + t(P1 - P0) = (1-t) P0 + tP1 , 0 < t < 1
    """
    step = 1/num_puntos
    points = []
    for i in range(num_puntos + 1):
        t = step*i
        x = (1-t)* p0[0] + t*p1[0]
        y = (1-t)* p0[1] + t*p1[1]
        points.append((x, y))
    
    return points

def cuadratic_bezier(p0, p1, p2, num_puntos=5):
    """Calcula una curva berzier de grado 2 entre 3 puntos
    
    B(t) = (1-t)**2P0 + 2(1-t)tP1 + t**2P2 , 0 < t < 1
    """
    step = 1/num_puntos
    points = []
    for i in range(num_puntos + 1):
        t = step*i
        x = (1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t**2*p2[0]
        y = (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t**2*p2[1]
        points.append((x, y))
    
    return points

if __name__ == "__main__":
    font_path = "DATA/Roboto-Regular.ttf"
    letter = "B"
    size = 100
    num_puntos = 5 #Num de puntos por seccion
    verts, codes =text_to_points(font_path, letter, size)
    x, y = zip(*verts)
    plt.plot(x, y, "r:*")
    curvas = (
        (verts[2], verts[3], verts[4], num_puntos),
        (verts[4], verts[5], verts[6], num_puntos),
        (verts[6], verts[7], verts[8], num_puntos),
        (verts[8], verts[9], verts[10], num_puntos),
        (verts[10], verts[11], verts[12], num_puntos),
        (verts[12], verts[13], verts[14], num_puntos),
        (verts[14], verts[15], verts[16], num_puntos),
        (verts[16], verts[17], verts[18], num_puntos),
    )
    for values in curvas:
        puntos =  cuadratic_bezier(*values)
        x, y = zip(*puntos)
        plt.plot(x, y, "g:*")

    lineas = (
        (verts[0], verts[1], num_puntos),
        (verts[1], verts[2], num_puntos),
        (verts[18], verts[19], num_puntos),
    )
    for values in lineas:
        puntos =  linear_bezier(*values)
        x, y = zip(*puntos)
        plt.plot(x, y, "g:*")


    plt.show()