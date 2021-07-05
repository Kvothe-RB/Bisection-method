import numpy as np

#%% Ecuación principal del método
def funcion(x):
    y = x**3 + np.exp(-x) - 1.5
    return y


#%% Función que calcula la solución con una precisión dada
#   f: funcion(x)
#   a: límite inferior del intervalo
#   b: límite superior del intervalo
#   Error: precisión del método

def biseccion(f,a,b,error):
    #print (a,b)
    fa=f(a)
    fc=error+1
    while np.abs(fc)>error:
         c=(a+b)/2.
         fc=f(c)
         if np.sign(fc)==np.sign(fa):
             a, fa=c, fc
         else:
             b=c
    return c, fc
   
