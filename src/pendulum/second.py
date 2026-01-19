import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")
from thetant import bis, u, du_cen, u_cen_wrapper
plt.rcParams.update({'font.size': 20})

t = np.linspace(0, np.pi / 2, 10000)
h = t[1] - t[0] # Paso h
def d2u_ad(f, x, h, **kwargs):
    """
    Segunda Derivada Adelantada.
    f''(x) approx (f(x) - 2f(x+h) + f(x+2h)) / h^2
    """
    
    return (f(x, **kwargs) - 2 * f(x + h, **kwargs) + f(x + 2 * h, **kwargs)) / (h**2)

def d2u_cen(f,x,h,**kwargs):
    return (f(x-h,**kwargs) - 2*f(x,**kwargs) + f(x + h, **kwargs)) / h**2

b = np.linspace(0, 1, 11)

l = np.linspace(0.50001, 1.2, 1000)

def mi_funcion(b, l):
    o = []
    for i in b:
        if i > 0.5:
            c = bis(u_cen_wrapper, 0.5, 1.1, beta=i)
            o.append(c)
    return np.array(o)
resultados = mi_funcion(b,l)
print(resultados)   
b_filtrados = b[b > 0.5]
plt.figure(figsize=(10,10))

betas = np.array(b)
deriv_0 = np.array([d2u_ad(u, 0, h, beta=i) for i in b])
plt.scatter(betas, deriv_0, s=80, 
            label=r"$u''(0)$", marker="o", color="red")
plt.plot(betas, deriv_0, linestyle='-', alpha=1, color="red")


betas_nt = np.array(b_filtrados)
deriv_nt = np.array([d2u_cen(u, resultados[idx], h, beta=beta_val) 
                for idx, beta_val in enumerate(b_filtrados)])
plt.scatter(betas_nt, deriv_nt, s=80, 
            label=r"$u''(\theta_{nt})$", marker="D")
plt.plot(betas_nt, deriv_nt, linestyle='-', alpha=1, color="blue")
plt.xlabel(r"$\beta$")
plt.ylabel(r"Segunda derivada")
plt.grid(True)
plt.legend()
ruta_guardado = "../../img/pendulum/second.pdf"
plt.savefig(ruta_guardado, format="pdf")
plt.show()


    

