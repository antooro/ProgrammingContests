import numpy
import math
with open('level4_0.in') as f:
    content = f.readlines()
content = [x.strip() for x in content] 
content.pop(0)
l = []

for i in content:
    l.append(i.split(' '))

arry = numpy.array(l)


contador = 0
coords = []
for (x,y), value in numpy.ndenumerate(arry):
    if (int(value) != 0):
        contador+=1
    else:
        if contador>=4:
            coords.append([(x,y) , contador])
        contador = 0

#print (coords)
c = 0
r = 0
i = -1
edif = []
'''for coor in coords:
    #print (coor)
    if c == 0 and r==0:
        i+=1
        c = list(coor[0])[1]
        r =  list(coor[0])[0]
        edif.append([list(coor[0]), i])
    elif list(coor[0])[1] == c and list(coor[0])[0]==r+1:
        edif.append([list(coor[0]), i])
        r =  list(coor[0])[0]
    elif list(coor[0])[1] != c:
        c = list(coor[0])[1]
        r =  list(coor[0])[0]
        i+=1
        edif.append([list(coor[0]), i])
        '''

def getCentro(l):
    prof = len(l)
    anch = l[0][0][1]
    fin = list(l[-1][0][0])[0]
    cosa = fin - math.trunc(anch/2)
    fin = list(l[0][0][0])[1] - math.ceil(anch/2)
    return (cosa,fin)

c = 0
x = 0
i = -1
listaza = []
for coor in coords:
    c = list(coor[0])[1]
    i+=1
    l = []
    for co2 in coords:
        if list(co2[0])[1] == c :
            l.append([co2])
    for n in l:
        if x ==0:
            listo =[]
            x =  (list((n[0])[0])[0])
            listo.append(n)
        elif (list((n[0])[0])[0]) == x+1:
            listo.append(n)
            x =  (list((n[0])[0])[0])
        elif (list((n[0])[0])[0]) != x+1:
            listaza.append(listo)
            listo =[]
            listo.append(n)
            x =  (list((n[0])[0])[0])
    if listo not in listaza:listaza.append(listo)


s = []
for i in listaza:
    if i not in s and len(i)>=4:
        s.append(i)
cont = 0
for n in (s):
    a = (list((getCentro(n))))
    print (cont , a[0] ,a[1], end=' ')
    cont+=1