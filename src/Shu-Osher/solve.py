import numpy as np
import matplotlib.pyplot as plt
from shuosher import RK_gen #Importamos el método del archivo en el que se define

plt.rcParams.update({'font.size': 13})

#Usamos esta tabla de Butcher para utilizar el método de Shu-Osher
butcher = np.array([[0, 0, 0, 0],
                   [1, 1, 0, 0],
                   [0.5, 0.25, 0.25, 0],
                   [0, 1/6, 1/6, 2/3]])


def fullvec(t, x, mu):
    posx, posy, velx, vely = x
    mag = np.hypot(velx, vely)  
    return np.array([velx, vely, -mu*mag*velx, -1-mu*mag*vely])

def caso(mu, alpha): #Definimos una solución genérica para iterar con distintos valores de mu y alpha.
    pos0x = 0
    pos0y = 0
    vel0x = np.cos(alpha)
    vel0y = np.sin(alpha)

    t, X = RK_gen(fullvec, x0 = [pos0x, pos0y,vel0x, vel0y], tmax = 2, dt = 0.001, butch = butcher, mu = mu)

    posx, posy, velx, vely = X[:, 0], X[:, 1], X[:, 2], X[:, 3]

    posytrue = posy[posy > 0]
    posxtrue = posx[:posytrue.size]

    return posxtrue, posytrue


for mu in np.linspace(0, 1, 7): #Graficamos para distintos valores de mu
    x, y = caso(mu, np.pi/4)


    plt.xlabel("$x(t)$ (Posición en $x$)")
    plt.ylabel("$y(t)$ (Posición en $y$)")
    plt.plot(x, y, label =f"$\\mu = ${"%.1f"%mu}")

plt.legend()
plt.savefig("../../img/Shu_Osher/mu.pdf")

#plt.show()
plt.close()

for alpha in np.linspace(0, np.pi/2, 7): #Graficamos para distintos valores de alpha
    x, y = caso(0.6, alpha)

    plt.xlabel("$x(t)$ (Posición en $x$)")
    plt.ylabel("$y(t)$ (Posición en $y$)")
    plt.plot(x, y, label =f"$\\alpha = ${"%.3f"%alpha}")

plt.legend()
#plt.show()
plt.savefig("../../img/Shu_Osher/alpha.pdf")

plt.close()

for alpha in np.linspace(0, np.pi/2, 7): #Graficamos para distintos valores de alpha en condiciones ideales
    x, y = caso(0, alpha)

    plt.xlabel("$x(t)$ (Posición en $x$)")
    plt.ylabel("$y(t)$ (Posición en $y$)")
    plt.plot(x, y, label =f"$\\alpha = ${"%.3f"%alpha}")


plt.legend()
#plt.show()
plt.savefig("../../img/Shu_Osher/ideal.pdf")


plt.show()
