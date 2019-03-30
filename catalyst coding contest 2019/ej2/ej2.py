import numpy as np
with open('level2_5.in','r') as f:
    output = f.read().splitlines()

limites = output[0]
posicion = output[1]

limites = limites.split(" ")
limx = int(limites[0])
limy = int(limites[1])

for n in output[:]:
    comandos = (n.strip())

comandos =  comandos.split(" ")

posicion = posicion.split(" ")
x = int(posicion[0])
y = int(posicion[1])

angulo = 0
print x,y
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
            print x,y


        #print "posicion"


        #print(basex,x)
        #print(basey,y)
        '''if (basex < x):
            for num in range(basex,x+1):
                print num,y
        elif (basex > x):
            for num in range(x,basex+1):
                print num,y
        elif (basey <  y):
            for num in range(basey,y+1):
                print x, num
        elif (basey >  y):
            for num in range(y,basey+1):
                print x, num
                '''
        avanza == False

#print x,y
