""""Codigo de importación de archivo svg
Juan Tapia Tinoco 
tapiatinocojuan@gmail.com
"""


import py5
s1 = None

def setup():
    global s1, rutas
    py5.size(500,500)
    s1, rutas = get_point_from_svg(r"DATA/monito.svg", 0.01, py5.width)
    
def draw():
    global s1, rutas
    py5.background(255)
    py5.shape(s1,0,0, s1.width, s1.height )
    py5.fill(255, 0, 0)
    py5.stroke(255, 0, 0)
    for ruta in rutas:
        for punto in ruta:
            py5.circle(punto[0], punto[1], 2)
    py5.no_loop()

def get_point_from_svg(ruta, t, size, layer="layer1"):
    s1 = py5.load_shape(ruta)
    rutas = []
    for child in s1.get_children():
        if child.get_name() != layer:
            continue
        for figure in child.get_children():
            puntos = []
            if figure.get_vertex_count() == 0:
                continue
            for i in range(figure.get_vertex_count()):
                point = figure.get_vertex(i)
                puntos.append(point)
                if i+1 >= figure.get_vertex_count():
                    continue 
            pts = get_points(puntos, figure.get_vertex_codes(), t, size)
            rutas.append(pts)
    return s1, rutas

def get_points(verts, codes, t, size):
    """Convierte curvas vectorizadas a una serie de puntos"""
    i = 0
    puntos = []
    try:
        for j, _ in enumerate(codes[:-1]):
            if codes[j+1] == py5.VERTEX :
                puntos.extend(
                    linear_bezier(verts[i], verts[i+1], t, size=size)
                )
            elif codes[j+1] == py5.QUADRATIC_VERTEX:
                puntos.extend(
                    cuadratic_bezier(verts[i], verts[i+1], verts[i+2], t, size=size)
                )
                i += 1
            elif py5.BEZIER_VERTEX:
                puntos.extend(
                    cubic_bezier(verts[i], verts[i+1], verts[i+2], verts[i+3], t, size=size)
                )
                i += 2
            i += 1
    except:
        pass
    return puntos

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
        y = ((1-t)* p0[1] + t*p1[1])
        points.append((x, y))
        t += st
    if flag:
        distancia = calcular_segmento(points)
        step = step*size/distancia
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
        y = ((1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t**2*p2[1])
        points.append((x, y))
        t += st
    if flag:
        distancia = calcular_segmento(points)
        step = step*size/distancia
        points = cuadratic_bezier(p0, p1,p2, step, 0)

    return points

def cubic_bezier(p0, p1, p2, p3, step=1, flag=1, size=100):
    """Calcula una curva berzier de grado 3 entre 4 puntos
    
    B(t) = (1-t)**3P0 + 3(1-t)**2tP1 + 3(1-t)t**2P2 + t**3P3 , 0 < t < 1
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
        x = (1-t)**3*p0[0] + 3*(1-t)**2*t*p1[0] + 3*(1-t)*t**2*p2[0] + t**3*p3[0]
        y = (1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t**2*p2[1] + t**3*p3[1]
        points.append((x, y))
        t += st
    if flag:
        distancia = calcular_segmento(points)
        step = step*size/distancia
        points = cubic_bezier(p0, p1, p2, p3, step, 0)

    return points

if __name__ == "__main__":
    py5.run_sketch()