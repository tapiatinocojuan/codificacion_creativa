edges = [
    (0, 1, {'weight': 143.0821648604144}), 
    (1, 7, {'weight': 161.79248222401569}), 
    (2, 3, {'weight': 152.84195630137984}), 
    (2, 7, {'weight': 186.84454444007116}), 
    (4, 9, {'weight': 204.26890932422714}), 
    (5, 10, {'weight': 107.14350500538056}), 
    (6, 7, {'weight': 125.68834720608363}), 
    (6, 10, {'weight': 154.48711753670656}), 
    (6, 11, {'weight': 103.1634310592026}), 
    (8, 13, {'weight': 106.50207931857611}), 
    (9, 14, {'weight': 113.20965118711737}), 
    (10, 15, {'weight': 143.89668864738465}), 
    (11, 12, {'weight': 143.5732621959276}), 
    (13, 14, {'weight': 78.37812352277092}), 
    (14, 19, {'weight': 174.67495684116813}), 
    (15, 16, {'weight': 158.37274602916432}), 
    (16, 21, {'weight': 148.9172264436178}), 
    (17, 22, {'weight': 69.70775747448883}),
    (17, 23, {'weight': 159.27159108972072}), 
    (18, 19, {'weight': 155.2859566275753}), 
    (18, 23, {'weight': 94.04304969631477}), 
    (20, 21, {'weight': 117.92194577123682}), 
    (21, 22, {'weight': 97.06276503659262}), 
    (23, 24, {'weight': 140.51122168569265})]


from collections import pdb
def buscar_puntos_conectados_a(res, orden, edges, valor):
    puntos = []
    index = []
    for i, (pta, ptb, _) in enumerate(edges):
        if pta == valor:
            puntos.append(ptb)
            index.append(i)
        elif ptb == valor:
            puntos.append(pta)
            index.append(i)

    for i in index[-1::-1]:
        edges.pop(i)
    res[valor] = puntos
    orden.append(puntos)
    for punto in puntos:
        buscar_puntos_conectados_a(res, edges, valor)

    return puntos

res = {}
puntos = buscar_puntos_coenctados_a(edges, 0)

print (puntos)
print (edges)




