import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

def _condiciones_iniciales(t, x0, y0):
    """  
    Función útil para guardar las condiciones iniciales y 
    guardar algunas variables que se ocuparán después
    t = (Iterable) arreglo de números que funciona como tiempo
        da forma al problema
    x0, y0 = (Escalares o iterables) condiciones iniciales 
    """
    x0 = np.asarray(x0)
    y0 = np.asarray(y0)
    x = np.zeros((len(t),) + x0.shape)
    y= np.zeros((len(t),) + y0.shape)
    x[0] = x0
    y[0] = y0
    return x,y

def dy(a):
    """Derivada a utilizar en el método leap-frog
    """
    return (np.exp(a)-1)

def leapfrog(dy, x0, y0, t, mu):
    """ 
    Método del salto de la rana, retorna arreglos (soluciones)
    Está construido sobre el cambio de variables x,y, por lo que
    a los arreglos x[], y[] se les aplica una exponencial para
    retornar las variables normalizadas.
    dy = (función) es la derivada se utiliza en cada paso
    x0,y0 = (escalares o iterables) condiciones iniciales
    t = (iterable) arreglo que hace de tiempo
    mu = parámetro de control del sistema
    """
    dt = np.diff(t) #paso
    x, y = _condiciones_iniciales(t, x0, y0)
    dy0 = dy(x0) 
    for n in range(t.size-1):
        ymedio = y[n] + 0.5 * mu * dt[n] * dy0
        x[n+1] = x[n] + dt[n]*(1- np.exp(ymedio) )
        dy0 = dy(x[n+1])
        y[n+1] = ymedio + 0.5 * mu * dt[n] * dy0
    return  np.exp(x), np.exp(y)

t = np.linspace(0,40,1000)

plt.figure(figsize=(15,5))
#plt.suptitle(r"Dinámica de Depredadores y Presas a distintos $\mu$")
plt.subplot(1,3,1)
p1, d1 = leapfrog(dy, 0, np.log(5), t, 0.5)
plt.plot(t, p1, color="blue", label="Presas")
plt.plot(t,d1, color ="red", label="Depredadores")
plt.title(r"$\mu = 0.5$")
plt.xlabel(r"Tiempo normalizado $\tau$")
plt.ylabel(r"Densidades normalizadas $(p,d)$")
plt.grid(True)
plt.legend()
    
plt.subplot(1,3,2)
p2, d2 = leapfrog(dy, 0, np.log(5), t, 1)
plt.plot(t, p2, color="blue", label="Presas")
plt.plot(t,d2, color ="red", label="Depredadores")
plt.xlabel(r"Tiempo normalizado $\tau$")
plt.ylabel(r"Densidades normalizadas $(p,d)$")
plt.ylim(0,8)
plt.title(r"$\mu = 1$")
plt.grid(True)
plt.legend()

plt.subplot(1,3,3)
p3, d3 = leapfrog(dy, 0, np.log(5), t, 5)
plt.plot(t, p3, color="blue", label="Presas")
plt.plot(t,d3, color ="red", label="Depredadores")
plt.xlabel(r"Tiempo normalizado $\tau$")
plt.ylabel(r"Densidades normalizadas $(p,d)$")
plt.ylim(0,8)
plt.title(r"$\mu = 5$")
plt.grid(True)
plt.legend()

ruta_guardado = "../../img/lotka/lotka_solutions.pdf"
plt.savefig(ruta_guardado, format="pdf")
plt.show()


