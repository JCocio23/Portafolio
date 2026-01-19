import numpy as np
import matplotlib.pyplot as plt

def u(theta, beta):
    return np.cos(theta) + beta * (np.sin(theta))**2

def du_cen(f, x, h=1e-5, **kwargs):
    return (f(x + h, **kwargs) - f(x - h, **kwargs)) / (2*h)

def du_ad(f,x, h=1e-5, **kwargs):
    return (f(x+h, **kwargs) - f(x)) / h
def u_cen_wrapper(x, **kwargs):
    return du_cen(u, x, **kwargs)

def bis(f, a, b, tol=1e-10, iter=100, **kwargs):
    """
    Método de la bisección, encuentra raíces dividiendo 
    el intervalo [a,b] por mitades.
    
    Argumentos
    ----------
    f: función f(x, **kwargs)
    a,b : escalares, límites del intervalo
    beta: parámetro que se decide incluir explícitamente
    tol: tolerancia del método
    iter: Iteraciones máximas
    **kwargs: parámetros extras
    """
    iter_count = 0

    while iter_count < iter:
        c = 0.5 * (a + b)

        if abs(f(c, **kwargs)) < tol or abs(b - a) < tol:
            return c

        if f(a, **kwargs) * f(c, **kwargs) < 0:
            b = c
        else: 
            a = c
        iter_count += 1

b = np.linspace(0.6,1,5)


t = np.linspace(0,np.pi/2, 10000)

for i in b:
    print("beta =", i)
    print("cero =", bis(u_cen_wrapper, 0.5, 1.1, beta=i))

