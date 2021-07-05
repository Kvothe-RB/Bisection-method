import numpy as np
import matplotlib.pylab as plt

# Intervalo de solución
xmin = -1.0
xmax =  1.0

N = 40         #Número de iteraciones

#%% Importamos las funciones que van a describir la ecuación y el método de bisección
import funciones

#%% Código principal, imprimimos la solución y el intervalo donde se halla
x=np.linspace(xmin,xmax,N+1)
y=funciones.funcion(x)
n=0

precision=1e-6

#Listas donde almacenamos las coordenadas de las raíces de la ecuación
xs=[]
ys=[]

for i in range (0,N):
    if y[i]*y[i+1] < 0:
        print ("Hay una raíz:")
        n+=1
        print ('Raíz x_%d: en el intervalo (%f,%f)' % (n,x[i],x[i+1]))
        
     
        sol= funciones.biseccion(funciones.funcion,x[i],x[i+1],precision)
        xs.append(sol[0])
        ys.append(sol[1])
        print ('Raíz en x = %.10f ; f(x)= %.10f' % (xs[n-1],ys[n-1]))

#%%Gráficas
x=np.linspace(xmin,xmax,1000)
y=funciones.funcion(x)

plt.plot(x,y)
plt.hlines(0,xmin,xmax)
for i in range(n):
    plt.plot(xs[i],ys[i],'yo')
plt.xlabel('x')
plt.ylabel('y')
plt.title('f(x)')
plt.show()


