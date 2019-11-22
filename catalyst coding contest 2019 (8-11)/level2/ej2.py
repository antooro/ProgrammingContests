from statistics import mean
from math import floor
import os 
import numpy
import sys
from collections import defaultdict
from pandas import DataFrame
for archivo in os.listdir("."):
    if not archivo.endswith(".in") or archivo.startswith("out"):
        continue
    with open(archivo) as f:
        lineas = f.read().splitlines()

    
    datos = lineas[1:]
    print(archivo)
    numeros = []
    array = []
    max_len = 0
    for l in datos:
        nums = l.split()
        filt_lst = []

        for i in range(len(nums)):
            if i%2!=0:
                filt_lst.append(nums[i])
        #print(filt_lst)
        max_len = len(filt_lst)
        array.append(filt_lst)
    tocho = numpy.array(array)  
    
    copia = numpy.array(tocho, copy=True)
    fronter = defaultdict(lambda :0)
    for (x,y), value in numpy.ndenumerate(tocho):
        #print(x,y,value)
        value = tocho[x][y]
        if x == 0 or y == 0 or x == len(tocho)-1 or y == len(tocho[0])-1:
            fronter[value] += 1
            copia[x][y] = "@"
            
        elif tocho[x+1][y] != value or tocho[x-1][y] != value or tocho[x][y+1] != value or tocho[x][y-1] != value:
            fronter[value] += 1
            copia[x][y] = "@"
    
    #print(dict(fronter))
    sol = ""
    elements = [int(i) for i in fronter.keys()]
    for k in sorted(elements):
        #print(k, fronter[k])
        sol += f"{fronter[str(k)]}\n"
    
    
    
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
    