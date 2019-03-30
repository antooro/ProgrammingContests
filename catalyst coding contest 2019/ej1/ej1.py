import numpy as np
with open('level1_5.in','r') as f:
    output = f.read().splitlines() 

posicion = output[0]

for n in output[:]:
    comandos = (n.strip())

comandos =  comandos.split(" ")

posicion = posicion.split(" ")
x = int(posicion[0])
y = int(posicion[1])

angulo = 0

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

    if (gira):
        angulo = (angulo+int(i)*90)%360
        gira = False

    elif (avanza):
        if angulo==0:
            x = x+ numero
        elif angulo == 90:
            y = y + numero
        elif angulo == 180:
            if (x-numero < 0):
                x = 0
            else:
                x = x - numero
        elif angulo == 270:
            if (y-numero < 0):
                y = 0
            else:
                y = y - numero
        avanza == False

print(x,y)
