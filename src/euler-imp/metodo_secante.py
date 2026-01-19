import numpy as np
import matplotlib.pyplot as plt 
tolerancia = 1e-5
plt.style.use("bmh")

f = lambda x: x**3  - 5*x# Se define la función a utilizar
df = lambda x: 3*x**2 - 5
    # Se define el método de la secante
def met_secante(f,a,b,tolerancia):
    zeros = []
    int = np.linspace(a,b,10)
    print(int)
    for i in range(int.size-1): 

        if f(int[i])*f(int[i+1]) <= 0:
            a,b = int[i:i+2]
            fa,fb = f(a), f(b)
            m = 0
            while (abs(fb*(b-a)/(fb-fa)) >=tolerancia):
                bold=b 
                b = b - fb*(b-a)/(fb-fa) 
                fa=fb 
                a=bold
                fb=f(b) 
                m +=1
            print("Existe un cero",b,"con iteraciones de",m,"veces")
            zeros.append(b)
    return zeros

zeros_secante = met_secante(f,-3,3,tolerancia)

plt.scatter(zeros_secante,np.zeros(3), label="Ceros calculados numéricamente", color="blue")
plt.plot(np.linspace(-3,3,1000), f(np.linspace(-3,3,1000)), label="Función analítica f(x)",color="purple")
plt.xlabel(r'Valor de $x$')
plt.ylabel(r'Valor de la función $f(x)$')
plt.legend()
plt.show()



