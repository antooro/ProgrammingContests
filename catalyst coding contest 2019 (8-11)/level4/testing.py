import numpy
import math


archivo = "level4_example.in"
with open(archivo) as f:
    lineas = f.read().splitlines()

rows,cols = lineas[0].split()
n_queries = lineas[1]
datos = lineas[2:]
print(archivo)
origen = []
dire = []
array = []
for i in range(len(datos)):
    l = datos[i]
    nums = l.split()
    origen.append([int(i)+.5 for i in nums[:2]])
    dire.append(nums[2:4])

    array.append(nums)
tocho = numpy.array(array) 
n_cuadra = numpy.zeros((int(rows),int(cols)))
print(origen)
print(dire)

def cubo(x1,y1,x2,y2,dist,r):
    mitad = (dist*r)
    az = int(x2)-int(x1)
    bz = int(y2)-int(y1)
    x = (az * mitad )/dist
    y = (bz * mitad )/dist
    return ((math.trunc(float(y1)+y)) ,(math.trunc(float(x1)+x)) )

puntos = []
for i in datos:
    #l.append(i.split(' '))
    l = []
    z = (i.split(' '))
    (y1,x1) = (float(z[0]),float(z[1])) #origen
    (y2,x2) = (float(z[2]),float(z[3])) #direccion
    r = 0.0001
    y1 = y1 +0.5
    x1 = x1 +0.5
    
    dist = math.sqrt( ((x2) - (x1))**2 + ((y2) - (y1))**2 )
    while (r<1):
        casilla = cubo(x1,y1,x2,y2,dist,r)
        if  casilla not in l:
            l.append(casilla)
        r = r+0.0001

    puntos.append(l)
for i in puntos:
    for n in i:
        for a in n:
            print (a,end=' ')
    print ("")