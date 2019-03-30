import numpy as np
import math
with open('level4_1.in','r') as f:
    output = f.read().splitlines()

limites = output[0]
posicion = output[1]

limites = limites.split(" ")
limx = int(limites[0])
limy = int(limites[1])

comandos = output[2]

speed = output[3].split(' ')
health = float(speed[0])
speed = float(speed[1])

n_aliens = int(output[4])

spawns = {}
for n in range(0,n_aliens):
    spawns[str(n)] = output[5+n]




dano = output[5+n_aliens].split(" ")
damage = float(dano[0])
rango = float(dano[1])
ntorres = int(output[6+n_aliens])

posTorre = {}
i = 0
for n in range(7+n_aliens,7+n_aliens+ntorres):
    linea = output[n].split(" ")
    posTorre[str(i)]= (int(linea[0]),int(linea[1]))
    i+=1
print("Speed {} Health {}".format(speed,health))
print("Nº aliens {}".format(n_aliens))
print("Nº torres {} \n".format(ntorres))
print(spawns)
print(posTorre)

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


'''
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
'''

max_tick = max(spawns.values())
min_tick = min(spawns.values())
tot_ticks = len(pasos) * speed + float(max_tick)
print(pasos)
print(tot_ticks)
al_pos = {}

torre_data = {}
for key,value in posTorre.items():
    torre_data[key] = -1


alien_data = {}
for key,value in spawns.items():
    alien_data[key] = health

pasofin = 0
ganamos = True
ha_terminado = False
for t in range(int(tot_ticks)):
    if (not ha_terminado):
        for key,value in spawns.items():
            if (not ha_terminado and alien_data[key]>0):
                al_num = key
                spw = int(spawns[al_num])
                if spw <= t:
                    position = (t-spw)*speed
                    index = 0
                    if position>= len(pasos):
                        index = len(pasos)-1
                    else:
                        index = math.floor(position)
                    sitio = pasos[index]
                    al_pos[al_num] = (sitio[0],sitio[1])
                    if (sitio == pasos[-1]):
                        ha_terminado = True
                        ganamos = False
                        pasofin = t

        for key,value in posTorre.items():
            if int(min_tick) <= int(t):
                mas_cercano = 9999999
                id_cercano = 999999

                if torre_data[key] != -1:
                    posi = al_pos[torre_data[key]]
                    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(posi, value)]))
                    if (distance > rango ):
                        torre_data[key] = -1

                if torre_data[key] != -1 and alien_data[torre_data[key]] <= 0:
                    torre_data[key] = -1

                if torre_data[key] == -1:
                    for clave,valor in al_pos.items():
                        if(alien_data[clave]>=0):
                            distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(valor, value)]))
                            if (distance < mas_cercano):
                                mas_cercano = distance
                                id_cercano = clave
                        torre_data[key] = id_cercano
                
                
                if torre_data[key] != -1:
                    alien_data[torre_data[key]]-=damage
                for x,y in alien_data.items():
                    print(x,y)
                if (all(y <= 0 for x,y in alien_data.items())):
                    ha_terminado = True
                    pasofin = t


print(pasofin)
print(ganamos)


