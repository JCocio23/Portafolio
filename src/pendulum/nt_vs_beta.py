import numpy as np
import matplotlib.pyplot as plt
from thetant import bis
plt.style.use("bmh")
plt.rcParams.update({'font.size': 20})

b = np.linspace(0.6,1,5)
##b_2 = np.linspace()

b2 = np.linspace(0.50001, 1, 1000)

def u(theta, beta):
    return np.cos(theta) + beta * (np.sin(theta))**2

def du_cen(f, x, h=1e-5, **kwargs):
    return (f(x + h, **kwargs) - f(x - h, **kwargs)) / (2*h)

def du_ad(f,x, h=1e-5, **kwargs):
    return (f(x+h, **kwargs) - f(x)) / h
def u_cen_wrapper(x, **kwargs):
    return du_cen(u, x, **kwargs)

# 1. Definir el vector de betas
betas = np.linspace(0.51, 1, 1000)

# 2. Lista para almacenar los ceros encontrados
ceros_no_triviales = []

# 3. Bucle para calcular el cero de la derivada para cada beta
for b_val in betas:
    # Usamos u_cen_wrapper porque bis necesita una función f(x, **kwargs)
    # Buscamos en el intervalo [0.1, 2.0] para evitar el cero trivial en theta=0
    raiz = bis(u_cen_wrapper, a=0.1, b=2.0, beta=b_val)
    ceros_no_triviales.append(raiz)

# Convertir a array de numpy para facilitar su manejo
ceros_no_triviales = np.array(ceros_no_triviales)

# 4. Visualización rápida de los resultados
plt.figure(figsize=(10, 6))
plt.plot(betas, ceros_no_triviales, label=r'Raíz no trivial $\theta_{nt}$', color="red")
for i in b:
    if i == 0.6:
        plt.plot(i, bis(u_cen_wrapper, 0.5, 1.1, beta=i), label="Valores conocidos", marker="D", color="blue")
    else:
        plt.plot(i,  bis(u_cen_wrapper, 0.5, 1.1, beta=i),marker="D", color="blue")
plt.xlabel(r'$\beta$')
plt.ylabel(r'$\theta_{nt}$ (rad)')
plt.grid(True)
plt.legend()
ruta_guardado = "../../img/pendulum/nt_vs_beta.pdf"
plt.savefig(ruta_guardado, format="pdf")
plt.show()
