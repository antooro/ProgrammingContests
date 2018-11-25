import numpy
import math
with open('level2_3.in') as f:
    content = f.readlines()
content = [x.strip() for x in content] 
content.pop(0)
l = []
for i in content:
    #l.append(i.split(' '))
    z = (i.split(' '))
    (y1,x1) = (float(z[0]),float(z[1]))
    (y2,x2) = (float(z[2]),float(z[3]))
    r = float(z[4])
    y1 = y1 +0.5
    x1 = x1 +0.5
    y2 = y2 +0.5
    x2 = x2 +0.5
    dist = math.sqrt( ((x2) - (x1))**2 + ((y2) - (y1))**2 )
    mitad = (dist*r)
    #print (mitad)
    #print  (math.atan(abs(int(x1)-int(x2)) - abs(int(y1)-int(y2) ))  )
    az = int(x2)-int(x1)
    bz = int(y2)-int(y1)
    x = (az * mitad )/dist
    y = (bz * mitad )/dist
    #print (((float(y1)+y)) ,((float(x1)+x)) )
    print((math.trunc(float(y1)+y)) ,(math.trunc(float(x1)+x)) )