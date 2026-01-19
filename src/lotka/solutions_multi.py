import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})

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

mu=np.array([0.5, 1.0, 5.0])

u = np.log(np.array([1, 4.2, 4, 2]))

v = np.log(np.array([2, 3.2, 1 , 5]))

plt.figure(figsize=(15,15))
for i in range(1, 13):
    plt.subplot(4, 3, i)
    if i <= 3:
        p, d = leapfrog(dy, u[0], v[0], t, mu[i-1])
        p0 = np.exp(u[0])
        d0 = np.exp(v[0])
        mu0 = mu[i-1]
        plt.title(r"$\mu = $" + str(mu0))

    elif i <= 6:
        p, d = leapfrog(dy, u[1], v[1], t, mu[i-4])
        p0 = np.exp(u[1])
        d0 = np.exp(v[1])
        mu0 = mu[i-4]

    elif i <= 9:
        p, d = leapfrog(dy, u[2], v[2], t, mu[i-7])
        p0 = np.exp(u[2])
        d0 = np.exp(v[2])
        mu0 = mu[i-7]

    else:
        p, d = leapfrog(dy, u[3], v[3], t, mu[i-10])
        p0 = np.exp(u[3])
        d0 = np.exp(v[3])
        mu0 = mu[i-10]

    plt.plot(t, p, color="blue", label=rf"Presas, $p_0={p0}$")
    plt.plot(t, d, color="red", label=rf"Depredadores, $d_0={d0}$")
    plt.xlabel(r"Tiempo normalizado $\tau$")
    plt.grid(True)
    plt.ylabel("$p,d$")
    if (i-1) % 3 == 0: 
        plt.legend(
                    fontsize=8,        
                    markerscale=0.6,   
                    handlelength=1,    
                    borderpad=0.2,                      
                    framealpha=0.8     
                  )
ruta_guardado = "../../img/lotka/lotka_solutions_multi.pdf"
plt.savefig(ruta_guardado, format="pdf")
plt.show()


