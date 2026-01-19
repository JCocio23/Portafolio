import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

N=  10

def dx_numerica(x,f):
    f = f(x)
    y = np.zeros(len(x))
    for i in range(1,len(x)-1):
        h_k = x[i] - x[i-1]
        h_k_1 = x[i+1] - x[i]
        df_1 = h_k_1/(h_k + h_k_1) * (f[i] - f[i-1])/h_k
        df_2 = h_k/(h_k + h_k_1) * (f[i+1] - f[i])/h_k_1
        y[i] = df_1 + df_2


    return x[1:-1], y[1:-1]

def cos(a):
    return np.cos(np.pi*a)

def gauss_chebyshev(N):
    x = np.zeros(N)
    print(N)
    for i in range(N):
        x[i] = np.cos((2*(i+1) -1)/(2*(N)) * np.pi)
    return x

def dx_analitica(x):
    return -np.sin(np.pi*x)*np.pi

x = gauss_chebyshev(N)
x_gen, y_gen = dx_numerica(x,cos)

x_prueba = np.linspace(-1,1,100)
y = dx_analitica(x_prueba)

print(len(x_gen))
plt.plot(x_gen, y_gen, color="green", label="Derivada Numérica")
plt.plot(x_prueba,y, color="red", label="Derivada Analítica")
plt.xlabel(r"Valores $x$ para evaluar la función")
plt.ylabel(r"Valores $f(x)$ para evaluar la función")
plt.legend()
plt.show()
