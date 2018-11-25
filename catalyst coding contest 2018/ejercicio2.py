import numpy
import math
with open('level2_0.in') as f:
    content = f.readlines()
content = [x.strip() for x in content] 
content.pop(0)
l = []
for i in content:
    #l.append(i.split(' '))
    z = (i.split(' '))
    (x1,y1) = (z[0],z[1])
    (x2,y2) = (z[2],z[3])
    r = float(z[4])
    print (x1,y1,x2,y2,r)
    dist = math.sqrt( (int(x2) - int(x1))**2 + (int(y2) - int(y1))**2 )
    mitad = (dist*r)
    #print  (math.atan(abs(int(x1)-int(x2)) - abs(int(y1)-int(y2) ))  )
    x = mitad * (int(y1)-int(y2))/dist
    y = mitad * (int(x1)-int(x2))/dist
    ao = dist
    ac = int(x2)
    print (ao,ac)
    x3 = ac/ao * dist
    print(int(x3))

    #print (x,y)
    #print(abs(math.trunc(float(x1)+x)) , abs(math.trunc(float(y1)+y)) )