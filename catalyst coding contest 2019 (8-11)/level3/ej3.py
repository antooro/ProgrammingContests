from statistics import mean
from math import floor,sqrt
import os 
import numpy
import sys
from collections import defaultdict
from pandas import DataFrame
for archivo in os.listdir("."):
    if not archivo.endswith(".in") or archivo.startswith("out"):
        continue

    #archivo = "level3_example.in"
    with open(archivo) as f:
        lineas = f.read().splitlines()

    
    datos = lineas[1:]
    print(archivo)
    numeros = []
    array = []
    for l in datos:
        nums = l.split()
        filt_lst = []

        for i in range(len(nums)):
            if i%2!=0:
                filt_lst.append(nums[i])
        #print(filt_lst)
        array.append(filt_lst)
    tocho = numpy.array(array) 
    
    copia = numpy.array(tocho, copy=True)
    datos = defaultdict(list)
    fronter = defaultdict(lambda :0)
    #print(tocho)
    for (x,y), value in numpy.ndenumerate(tocho):
        #print(x,y,value)
        value = tocho[x][y]
        if x == 0 or y == 0 or x == len(tocho)-1 or y == len(tocho[0])-1:
            fronter[value] += 1
            copia[x][y] = "@"
            datos[value].append((x,y,True))
            
        elif tocho[x+1][y] != value or tocho[x-1][y] != value or tocho[x][y+1] != value or tocho[x][y-1] != value:
            fronter[value] += 1
            copia[x][y] = "@"
            datos[value].append((x,y,True))
        else:
            datos[value].append((x,y,False))

    posiciones = defaultdict(list)
    for k,v in datos.items():
        x = [i[0] for i in v]
        y = [i[1] for i in v]
        
        min_x,max_x,min_y,max_y = min(x),max(x),min(y),max(y)
        posiciones[k].append((floor(mean(x)),floor(mean(y))))
    #print(posiciones)

    def getNearPos(x,y,k):
        dat = [item for item in datos[k] if item[2] == False]
        lista_min = []
        min = 9999999999
        min_x = 99999999
        min_y = 99999999
        for item in dat:
            x2,y2 = item[:2]
            dist = sqrt((x-x2)**2 + (y-y2)**2)
            #print(dist)

            if dist ==  min:
                lista_min.append((x2,y2))

            if dist < min:
                lista_min = [(x2,y2)]
                min_x = x2 
                min_y= y2
                min = dist
            if len(lista_min)>1:
                if x2 < min_x:
                    min_x = x2 

                if y2 < min_x:
                    min_y= y2

        if len(lista_min)>1:
            print(lista_min, min_x)
            lista_min = [ i for i in lista_min if i[0] <= min_x] 
            print(lista_min)
        if len(lista_min)>1:
            lista_min = [ i for i in lista_min if i[1] <= min_y] 

        return(lista_min[0])

    final = defaultdict(list)
    for k,v in posiciones.items():
        for coord in v:
            x,y = coord
            if tocho[x][y]==k:
                for item in datos[k]:
                    if item[0] == int(x) and item[1] == int(y):
                        if (item[2]):
                            final[k].append(getNearPos(x,y,k))
                            #print(f"Print si está en el pais y es frontera")

                        else:
                            #print(f"Print si está en el pais y no es frontera")
                            #print((x,y))
                            final[k].append((x,y))

            else:
                final[k].append(getNearPos(x,y,k))
                #print("No está en el país")    
                        
    #print(final)
    
    
    #print(dict(fronter))
    sol = ""
    elements = [int(i) for i in final.keys()]
    for k in sorted(elements):
        #print(k, fronter[k])
        x,y = (final[str(k)][0])
        sol += f"{y} {x}\n"
    #print(sol)
    
    
    
    with open(archivo.replace("level","out"),"w+") as f:
        f.write(sol)
    
    '''    
    for (x,y), value in numpy.ndenumerate(copia):
        if (y == 0):
            print("")

        print(f"{value}",end=" ")
        if len(value)==1:
            print("",end=" ")
    '''
    