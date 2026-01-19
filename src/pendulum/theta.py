import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")
plt.rcParams.update({'font.size': 20})

def u(theta, beta):
    return np.cos(theta) + beta * (np.sin(theta))**2

t = np.linspace(0, np.pi / 2, 10000)
h = t[1] - t[0] # Paso h

def du_cen(f, x, h, **kwargs):
    """Derivada central para un punto x."""
    return (f(x + h, **kwargs) - f(x - h, **kwargs)) / (2 * h)

def du_ad(f, x, h, **kwargs):
    """Derivada adelantada para un punto x."""
    return (f(x + h, **kwargs) - f(x, **kwargs)) / h

def du_atras(f, x, h, **kwargs):
    """Derivada atrasada para un punto x."""
    return (f(x, **kwargs) - f(x - h, **kwargs)) / h


def calcular_derivada_mixta(f, t_vector, beta):
    """
    Calcula la derivada numérica de f(theta, beta) sobre el vector t.
    Usa la Adelantada en t[0] y t[-1], y Central en el interior.
    """
    N = len(t_vector)
    h_local = t_vector[1] - t_vector[0]
    derivada = np.zeros(N)
    derivada[1:N-1] = du_cen(f, t_vector[1:N-1], h_local, beta=beta)
    derivada[0] = du_ad(f, t_vector[0], h_local, beta=beta)
    derivada[N-1] = du_atras(f, t_vector[N-1], h_local, beta=beta)
    return derivada


b = np.linspace(0, 1, 11)

plt.figure(figsize=(10, 10))
for i in b:
    s = str(round(i, 2))
    derivada_calculada = calcular_derivada_mixta(u, t, i)
    plt.plot(t, derivada_calculada, label=r"$\beta =$" + s)
plt.xlabel(r"$\theta$")
plt.ylabel(r"$u'(\theta)$")
plt.legend(title=r"Parámetro $\beta$")
plt.grid(True, linestyle='--', alpha=0.7)
ruta_guardado = "../../img/pendulum/theta.pdf"
plt.savefig(ruta_guardado, format="pdf")
plt.show()

