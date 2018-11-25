#-*- coding: utf-8 -*-

from time import time

def inicio():
    
    mat = rellena(leerFichero())
    
    iteraciones = pedirIteraciones()
    '''
    tInicial guarda el tiempo a 
    partir de que son pedidas las iteraciones
    '''
    tInicial = time() 
    matN = ajustaMatriz(itera(ampliaMat(ampliaMat(mat)) , iteraciones))
    
    print iteraciones , ' iteraciones'
    print vivasTotales(matN) , ' celdas vivas'
    print 'Dimensiones: ', len(matN) , ' x ' , len(matN[0])
    print round(time() - tInicial,2), 'segundos'

    guardarFichero(matrizAString(matN),matN)
    
    return None

'''
Funcion que devuelve como resultado una matriz a la que se la 
ha aplicado las iteraciones correspondientes del algoritmo.

Parametros:
- matriz --> Matriz sobre la que se aplican las iteraciones.
- iteraciones --> Numero de iteraciones.
'''
def itera(matriz , iteraciones):
    matN = creaMatriz(len(matriz) , len(matriz[0]))
    while iteraciones != 0:
        for i in range(1 ,len(matriz) - 1):
            for j in range(1 , len(matriz[0])-1):
                viv = compruebaViva(i , j , matriz)
                if viv == True:
                    matN[i][j] = 'X'
                else:
                    matN[i][j] = '.'
        matriz = copiaMatriz(matN)
        if(comprueba_crecimiento(matriz)):
            matriz = copiaMatriz(ampliaMat(matriz))
            matN = creaMatriz(len(matriz) , len(matriz[0]))
        iteraciones -= 1
    return matriz

'''
Funcion que devuelve un numero entero que se corresponde con el numero
de celdas vivas alrededor de una celda.

Parametros:
-x --> posicion x de la celda evaluada.
-y --> posicion y de la celda evaluada.
- matriz --> matriz sobre la que se hace la comprobacion.
'''
def compruebaViva(x , y , matriz):
    celdasVivas = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1,y + 2):
            if i != x or j!= y:
                if matriz[i][j] == 'X':
                    celdasVivas += 1
    if matriz[x][y] == 'X':
        viva = True
    else:
        viva = False

    if viva == True:
        if celdasVivas < 2 or celdasVivas > 3:
            viva = False # Muere
    else:
        if celdasVivas == 3:
            viva = True # Pasa a vivir

    return viva

'''
Funcion que devuelve un valor boolean. Se comprobara 
si en los bordes exteriores hay alguna celda viva, en ese caso el valor resultado
sera True --> Se debera ampliar la matriz.
En caso contrario, False --> la matriz mantendra su estado.

Parametros:
- matriz --> matriz sobre la que se realiza la comprobacion.
'''
def comprueba_crecimiento(matriz):
    crece = False
    for i in range(1 , len(matriz) - 2): #Este dos era un uno antes
        if matriz[i][1] == 'X' or matriz[i][len(matriz[0]) - 2] == 'X': #Falta [0]
            crece = True
    for j in range(1 , len(matriz[1]) - 2): #Este dos era un uno antes
        if matriz[1][j] == 'X' or matriz[len(matriz) - 2][j] == 'X': #Ponia matriz[len(matriz[1]) - 2][j] == 'X'
            crece = True
    return crece

'''
Funcion que devuelve la matriz definitiva, despues de realizar todas la itereaciones.
Se van comprobando todos los bordes exteriores con celdas muertas, hasta
encontrarse con un celda viva, donde se termina de ajustar la matriz.

El resultado sera la matriz ajustada si hay 1 o mas celdas vivas, 
en caso contrario se devolvera una matriz 1x1 con celdas muertas.

Parametros:
- matriz --> matriz sobre la que se realiza el ajuste.
'''
def ajustaMatriz(matriz):
    if vivasTotales(matriz)!= 0:
        iMin = -1
        iMax = -1
        jMin = -1
        jMax = -1
        i = 0
        while iMin == -1:
            for j in range(len(matriz[0])):
                if matriz[i][j] == 'X':
                    iMin = i
            i+=1
        i=len(matriz)-1            
        while iMax == -1:
            for j in range(len(matriz[0])):
                if matriz[i][j] == 'X':
                    iMax = i
            i-=1
        j=0
        while jMin == -1:
            for i in range(len(matriz)):
                if matriz[i][j] == 'X':
                    jMin=j
            j+=1
        
        j=len(matriz[0])-1
        while jMax == -1:
            for i in range(len(matriz)):
                if matriz[i][j]=='X':
                    jMax = j
            j-=1
                    
        #print iMin, iMax
        #print jMin, jMax
        
        matN = creaMatriz(iMax-iMin+1, jMax-jMin+1)
        for i in range(iMin, iMax+1):
            for j in range(jMin, jMax+1):
                matN[i-iMin][j-jMin]=matriz[i][j]
        return matN
    else:
        return creaMatriz(1, 1)


'''
Funcion que devuelve un numero entero, que se corresponde con el numero de 
celdas vivas totales de la matriz.

Parametros:
- matriz --> matriz sobre la que se realiza el recuento.
'''
def vivasTotales(matriz):
    vivasTotales = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 'X':
                vivasTotales+=1
    return vivasTotales
    
    
'''
Ficheros + Entrada/Salida de datos
'''
'''
Lectura de fichero: se devuelve el fichero una vez leido.
'''
def leerFichero():
    entradaValida = False
    while entradaValida == False:
        fichero_entrada = raw_input('Fichero de entrada: ')
        try:
            fich = open (fichero_entrada)
            infor = fich.readlines()
            entradaValida = True

        except:
            print 'No se encuentra el fichero.'
    return infor

'''
Funcion que pide donde se desea guardar el fichero y procede a su almacenamiento.

Parametros:
- cadena --> la matriz resultado de todo el proceso, transformada en una cadena.
- matriz --> Es utilizada para guardar el tamaño de la matriz.
'''
def guardarFichero(cadena,matriz):
    entradaValida = False
    while entradaValida == False:
        fichero_salida = raw_input('Fichero de salida: ')
        try:
            with open(fichero_salida,'w') as fichero:
                fichero.write(str(len(matriz)))
                fichero.write('\n')
                fichero.write(str(len(matriz[0])))
                fichero.write('\n')
                fichero.write(cadena)
                fichero.flush()
                entradaValida = True
        except:
            print 'Entrada de datos vacia. No se guardara el resultado'
            entradaValida = True
    return None

'''
Funcion que pide el numero de iteraciones que el usuario quiere realizar.
'''
def pedirIteraciones():
    entradaValida = False
    while entradaValida == False :
        entrada = raw_input( 'Escriba el numero de iteraciones que desea realizar: ')
        try:
            iteraciones = int(entrada)
            if iteraciones >= 0:
                entradaValida = True
            else:
                entradaValida = False
                print 'Entrada de datos erronea: no puede ser negativo'
        except:
            entradaValida = False
            print 'Entrada de datos erronea: ha de ser un entero'
    return iteraciones
'''
Funciones de Matrices
'''
'''
Funcion que crea una matriz entera de celdas muertas.

Parametros:
- filas 
- columnas
'''
def creaMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append('.')
    return matriz
'''
Funcion que rellena la matriz creada anteriormente con las datos
leidos del fichero.

Parametros:
- infor: datos leidos del fichero
'''
def rellena (infor):
    mat = creaMatriz(int(infor[0]),int(infor[1]))
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat [i][j] = infor[i+2][j]
    return mat
'''
Funcion que amplia la matriz por sus bordes exteriores. Crea dos filas y dos columnas mas
llenas de celdas muertas.

Parametros:
- matriz --> matriz sobre la que se realiza la ampliacion
'''
def ampliaMat(matriz):
    matN = creaMatriz(len(matriz) + 2, len(matriz[0]) + 2)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matN[i + 1][j + 1] = matriz[i][j]
    return matN
'''
Funcion que copia una matriz en otra

Parametros:
- matriz --> matriz que va a ser copiada
'''
def copiaMatriz(matriz):
    matN = creaMatriz(len(matriz) , len(matriz[0]))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matN[i][j] = matriz[i][j]
    return matN
'''
Funcion que guarda todos los datos de una matriz en una cadena.

Parametroa:
- matriz --> matriz que va a ser copiada en una cadena.
'''
def matrizAString(matriz):
    s = ''
    for i in range (len(matriz)):
        for j in range(len(matriz[0])):
            s = s + matriz[i][j]
        s = s + '\n'
        
    return s
            
'''
Ejecucion
'''
if __name__ == '__main__':
    inicio()