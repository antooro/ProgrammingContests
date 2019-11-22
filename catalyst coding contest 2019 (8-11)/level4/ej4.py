from statistics import mean
from math import *
import os 
import numpy
import sys
from collections import defaultdict
from pandas import DataFrame
for archivo in os.listdir("."):
    if not archivo.endswith(".in") or archivo.startswith("out"):
        continue

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
    print(len(n_cuadra))
    def meSalgo(x,y):
        if x <= 0 or y <= 0:
            return True
        if x > len(n_cuadra)-1 or y > len(n_cuadra[0])-1:
            return True
        else:
            return False
    
    casillas = defaultdict(list)
    for i in range(len(origen)):
        o_x, o_y = (origen[i])
        d_x ,d_y = (dire[i])
        
        angulo = atan(int(d_y)/int(d_x))
        #print("PAPAPPA")
        distancia = 0.0001
        x , y = o_x,o_y
        cas = []
        while not meSalgo(x,y):
            distancia += 0.0001
            x = o_x +(distancia * cos(angulo))
            y = o_y +(distancia * sin(angulo))
            
            c_x,c_y = (floor(x),floor(y))
            if (c_x,c_y) not in cas:
                cas.append((floor(x),floor(y)))
        print(cas)      
        '''
        for c in cas:
            for n in c:
                print(n,end=" ")

        print("")
        '''
    exit()
    '''    
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
    
    
    for (x,y), value in numpy.ndenumerate(copia):
        if (y == 0):
            print("")

        print(f"{value}",end=" ")
        if len(value)==1:
            print("",end=" ")
    '''
    