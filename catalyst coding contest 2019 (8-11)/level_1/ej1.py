from statistics import mean
from math import floor
import os 

for archivo in os.listdir("."):
    if not archivo.endswith(".in"):
        continue
    with open(archivo) as f:
        lineas = f.read().splitlines()



    datos = lineas[1:]

    numeros = []
    for l in datos:
        nums = l.split()
        for n in nums:
            numeros.append(int(n))

    with open(archivo.replace("level","out"),"w+") as f:
        sol = str(min(numeros)) + " " +str(max(numeros))+" "+str(floor(mean(numeros)))
        print(sol)
        f.write(sol)

