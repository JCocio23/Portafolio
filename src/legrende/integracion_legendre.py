"""
Hola!

El Código evalua los polinomios de Legendre, en concreto, realiza ciertas funciones descritas a continuación

- Polinomios_Legendre(n,g,f,w) : Evalua una cantidad w de elementos en la función de Legendre de grado desde 1 hasta n, para luego graficarlos a la vez, esta función se compone de:

> n: Grado del Polinomio
> g: Método de Integración preferido (Por defecto Metodo_Simpson_1_3)
> f: Función integrando que se encuentra dentro de la integral

- Interpolar_Legendre(n,m,w) : Evalua el polinomio de grado n en una cantidad m de nodos, para luego interpolar estos en curvas compuestas por w puntos, finalmente, muestra el resutado de la interpolación en una gráfica.

> n: Grado del Polinomio 
> m: Cantidad de nodos para utilizar (debe ser siempre +1 del grado)
> w: Cantidad de puntos para interpolar en la curva 

- Comparar_Coef_Interp(n,c,m,sigma) : Función que muestra los coeficientes pertenecientes los polinomios de Legendre de grado n calculados haciendo uso de la función integral, para luego interpolarlos y aprovechar de curve_fit para obtener los valores estimados, finalmente, se imprime a su vez los valores obtenidos de la propia función de Legendre del Scipy.

> n : Grado del Polinomio (por defecto n = 1)
> c : Cantidada de puntos para interpolar (por defecto, c=100)
> m : Cantidad de nodos con los que realizar la interpolación (por defecto m=2, recordar que debe ser siempre mayor al grado del polinomio)
> sigma : Indica el peso que deben conllevar los datos (por defecto está en None)

IMPORTANTE: La función Comparar_Coef_Interp() lleva dentro la función que Curve_fit analiza para encontrar coeficientes, a día de hoy no formulo una expresión que pueda generar la función pedida de forma coherente, por lo que esta debe ser ajustada manualmente antes de usarse, por defecto lleva un polinomio n =5

+ Agradecimientos al Repositorio de la Ayudantía de FC II (Diaz Amaro, Mella Fernanda) y Álvaro Osses por el código de la interpolación de Lagrange 
"""

import numpy as np 
import matplotlib.pyplot as plt 
import scipy as scp
from scipy.optimize import curve_fit
plt.style.use("bmh")

def integrado(x, n, phi):
    return (x + np.sqrt( 1 - x**2)*np.cos(phi)*1j )**n 

def Metodo_Simpson_1_3(f,n,x,c=13, **kwargs):
    sum_impar, sum_par = 0,0
    phi = np.linspace(0,2*np.pi, c)
    h = phi[1] - phi[0]

    for i in range(2,c-2,2):
        sum_par += f(x, n,phi[i], **kwargs)

    for i in range(1,c-1,2):
        sum_impar += f(x,n,phi[i], **kwargs)

    return h/3 * ( f(x,n,phi[0], **kwargs) + f(x,n,phi[-1], **kwargs) + 4 * sum_impar  +  2 * sum_par )



def Legendre_n(x,g,n,f, **kwargs):
    return 1/(2*np.pi) * g(f,n,x, **kwargs).real 

def Polinomios_Legendre(n, w):
    t = np.linspace(-1,1,w)
    for i in range(1,n+1):
        y = (Legendre_n(x =np.linspace(-1,1,w),n=i,g=Metodo_Simpson_1_3, f=integrado))
        plt.plot(t,y,label=f'N ={i}')
    plt.xlabel(r"Valores $x_i$")
    plt.ylabel(r"Valores $P(x_i)$")
    plt.legend()
    plt.show()

def Interpol_Lagrange(int, x, y):
    k = len(x) - 1
    sum = 0
    for i in range(k + 1):
        prod = y[i]
        for j in range(k + 1):
            if i != j:
                prod = prod*(int - x[j])/(x[i] - x[j])
        sum = sum + prod
    return sum

def Interpolar_Legendre(n,m, w): 
    data= np.linspace(-1,1,w)
    data_m = np.linspace(-1,1,m)
    s = Legendre_n(x =data_m,n=n,g=Metodo_Simpson_1_3, f=integrado)
    l = (Legendre_n(x =data,n=n,g=Metodo_Simpson_1_3, f=integrado))

    plt.scatter(data,Interpol_Lagrange(data,data_m,s), label="Puntos Interpolados", color="red", s=20)
    plt.scatter(data_m, s, s=45, marker="D", color="green", label="Nodos iniciales")
    plt.plot(data, l, label="Polinomio de Lagrange")
    plt.xlabel(r"Valores $x_i$")
    plt.ylabel(r"Valores $P(x_i)$ e Interpolados")
    plt.legend()
    plt.show()



def Coeficientes_Interpolados(n):
    w = n+1
    x = np.linspace(-1,1,w)
    y = Legendre_n(x =x,n=n,g=Metodo_Simpson_1_3, f=integrado)
    matriz_vander = np.vander(x)
    Coeficientes = np.linalg.solve(matriz_vander, y)
    
    legendre_coef = np.array(scp.special.legendre(n))
    print("Los valores del Polinomio de Legendre de grado", n,"son:")
    print(legendre_coef)
    print("Los coeficientes calculados son:")
    print(Coeficientes)
    print("El error absoluto entre los coeficientes es: ")
    print(np.abs(legendre_coef - Coeficientes))



Coeficientes_Interpolados(6)


