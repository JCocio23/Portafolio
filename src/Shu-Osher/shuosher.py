import numpy as np
import matplotlib.pyplot as plt

#0  |
#1  |1
#1/2|1/4  1/4
#------------------
#   |1/6  1/6  2/3

#aqui, 
#c1 = 0, c2 = 1, c3 = 1/2
#a21 = 1, a31=1/4, a32=1/4
#b1 = 1/6, b2 = 1/6, b3 = 2/3

#Implementamos la tabla de butcher del problema como un arreglo de (s+1)*(s+1) elementos.

shu_butcher = np.array([[0, 0, 0, 0],
                   [1, 1, 0, 0],
                   [0.5, 0.25, 0.25, 0],
                   [0, 1/6, 1/6, 2/3]])
#Donde ci = butcher[i, 0], bi = butcher[3, i]





def RK_gen(f, x0, tmax, dt, butch, t0 = 0, **kwargs):
    """
    Método de Runge-Kutta genérico para cualquier tabla de butcher. Retorna la solución numerica a la ecuación diferencial dx/dt = f(x, t) con condicion incial x(t0) = x0.

    Parámetros:
    -----------
    f       : Llamable, función de al menos dos argumentos f(x, t) asociada a la ecuación diferencial a resolver. los "kwargs" son pasados a este elemento.
    x0      : Condiciones iniciales del sistema.
    tmax    : Límite superior del intervalo de tiempo a considerar
    dt      :
    butch   : Tabla de butcher a considerar, se entrega como arreglo de (s+1)*(s+1) donde s es la cantidad de etapas del Runge-Kutta a utilizar.
    t0      : Condición inicial de tiempo
    """
    x0 = np.asarray(x0) #Considera el caso en que x0 es un escalar, y lo convierte en arreglo

    t = np.arange(t0, tmax, dt) #Arreglo de tiempo
    x = np.zeros((*t.shape, *x0.shape)) #Se desempaquetan los iterables
    x[0] = x0  #Definimos la condición inical 

    shape = np.shape(butch) 

    #Obtenemos los pesos y nodos temporales para aplicar el metodo de RK
    a = butch[0:shape[0]-1, 1:] 
    b = butch[shape[0] - 1, 1:]
    c = butch[:, 0]
    
    #Aplicamos la forma general para el metodo de RK
    for i in range(t.size - 1):
        K = np.zeros((np.size(b), *x0.shape)) #Creamos un arreglo para almacenar los K
        sum = 0
        for k in range(0, np.size(b)):
            K[k] = dt*f(t[i] + c[k]*dt, x[i] + sum, **kwargs)
            for j in range(1, k):
                sum = sum + a[k-1, j-1]*K[j+1]
            
        sum2 = 0

        for p in range(1, np.size(b)+1):
            sum2 = sum2 + b[p-1]*K[p-1]

        x[i+1] = x[i] + sum2
        if x[i+1][1]  <=0:
            return t,x

    return t, x

def shu_osher_exp(f, x0, tmax, dt, t0 = 0, **kwargs):
    """
    Método de Shu y Osher aplicado explicitamente. Retorna la solución numerica a la ecuación diferencial dx/dt = f(x, t) con condicion incial x(t0) = x0.

    Parámetros:
    -----------
    f       : Llamable, función de al menos dos argumentos f(x, t) asociada a la ecuación diferencial a resolver. los "kwargs" son pasados a este elemento.
    x0      : Condiciones iniciales del sistema.
    tmax    : Límite superior del intervalo de tiempo a considerar
    dt      :
    t0      : Condición inicial de tiempo
    """

    x0 = np.asarray(x0)#Considera el caso en que x0 es un escalar, y lo convierte en arreglo

    t = np.arange(t0, tmax, dt)#Arreglo de tiempo
    x = np.zeros((*t.shape, *x0.shape))#Se desempaquetan los iterables
    x[0] = x0 
    
    #Se aplica explicitamente el método de Shu-Osher.
    for i in range(t.size - 1):
        K1 = dt*f(t[i], x[i], **kwargs)
        K2 = dt*f(t[i] + 1*dt, x[i] + 1*K1)
        K3 = dt*f(t[i] + 0.5*dt, x[i] + 0.25*K1 + 0.25*K2)
        x[i+1] = x[i] + ((1/6)*K1 + (1/6)*K2 + (2/3)*K3)
    return t, x
