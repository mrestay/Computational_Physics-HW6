#!/usr/bin/python
#encoding: UTF-8

import numpy as np
import matplotlib.pyplot as plt


"""
Carga el archivo con posiciones en un arreglo de numpy.
Input: archivo con posiciones iniciales.
Output: numpy array con todos los datos.
"""
def cargar_datos(file):
 
    #Carga los datos del archivo de entrada en dos arrays, uno con posición en X y otro con posición en Y.
    pos_x= np.loadtxt(file, unpack=True, usecols=[1])
    pos_y = np.loadtxt(file, unpack=True, usecols=[2])
   
    return pos_x, pos_y

"""
Grafica los datos del arreglo cargado en el metodo cargar_datos.
Input: Vector de posiciones en X, Vector de posiciones Y.
Output: Gráficas.
"""

def make_plot(x, y):
    

    plt.plot(x[0],y[0],'ko')
    plt.plot(x[1:],y[1:], 'k*', color='b')
    plt.xlabel('$Pos_X$', size=24)
    plt.ylabel('$Pos_Y$',size=24)
    plt.title('$Condiciones-Iniciales$', size=30)
    plt.axes().set_aspect('equal', 'datalim')
    plt.savefig('gráfica1.png')
    
#Nombre del archivo para graficar.
filename = 'condiciones_iniciales.dat'
x,y= cargar_datos(filename)
    
cargar_datos(filename)
make_plot(x, y)