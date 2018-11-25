import numpy
import math
with open('level3_2.in') as f:
    content = f.readlines()
content = [x.strip() for x in content] 
content.pop(0)
l = []

def cubo(x1,y1,x2,y2,dist,r):
    mitad = (dist*r)
    az = int(x2)-int(x1)
    bz = int(y2)-int(y1)
    x = (az * mitad )/dist
    y = (bz * mitad )/dist
    return ((math.trunc(float(y1)+y)) ,(math.trunc(float(x1)+x)) )

puntos = []
for i in content:
    #l.append(i.split(' '))
    l = []
    z = (i.split(' '))
    (y1,x1) = (float(z[0]),float(z[1]))
    (y2,x2) = (float(z[2]),float(z[3]))
    r = 0.0001
    y1 = y1 +0.5
    x1 = x1 +0.5
    y2 = y2 +0.5
    x2 = x2 +0.5
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