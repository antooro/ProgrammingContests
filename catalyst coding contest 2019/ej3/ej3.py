import numpy as np
import math
with open('level3_5.in','r') as f:
    output = f.read().splitlines()

limites = output[0]
posicion = output[1]

limites = limites.split(" ")
limx = int(limites[0])
limy = int(limites[1])

comandos = output[2]

speed = float(output[3])

n_aliens = int(output[4])

spawns = {}
for n in range(0,n_aliens):
    spawns[str(n)] = output[5+n]

queries = []
n_queries = int(output[5+n_aliens])
for n in range(6+n_aliens, 6+n_aliens+n_queries):
    linea = output[n].split(" ")
    queries.append((linea[0],linea[1]))
'''
print("Speed {}".format(speed))
print("Nº aliens {}".format(n_aliens))
print(queries)
print(spawns)'''




comandos =  comandos.split(" ")

posicion = posicion.split(" ")
x = int(posicion[0])
y = int(posicion[1])

angulo = 0


pasos = []

pasos.append((x,y))
gira = False
avanza = False
for i in comandos:
    if i=="F":
        avanza = True
        continue
    if i=="T":
        gira = True
        continue

    numero = int(i)
    basex = x
    basey = y
    if (gira):
        angulo = (angulo+int(i)*90)%360
        gira = False

    elif (avanza):
        paso = 0
        while (paso<numero):
            if angulo==0:
                x=x+1
            if angulo==90:
                y=y+1
            if angulo==180:
                x=x-1
            if angulo==270:
                y=y-1
            paso=paso+1
            pasos.append((x,y))


        #print "posicion"


        #print(basex,x)
        #print(basey,y)
        
        avanza == False



for q in queries:
    tick = int(q[0])
    al_num = q[1]
    spw = int(spawns[al_num])
    position = (tick-spw)*speed
    index = 0
    if position> len(pasos):
        index = len(pasos)-1
    else:
        index = math.floor(position)
    sitio = pasos[index]

    print(tick,al_num,sitio[0],sitio[1])

