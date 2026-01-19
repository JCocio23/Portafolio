import numpy as np
import matplotlib.pyplot as plt
import funciones_utiles as fu
plt.rcParams.update({'font.size': 14})

x = 15
x_eje1=np.arange(x+1)
x_eje2=np.arange(1,x+1)

def Cn(x):
    return 4**x / (x**(3/2) * np.sqrt(np.pi))

y = fu.catalan_numpy(x, dtype=np.float128)

w = Cn(x_eje2) 

plt.figure(figsize=(10,6))
plt.scatter(x_eje1,y, label="Números de Catalán", marker="D", color="red", s=60,)
plt.plot(x_eje2,w, label="Aproximación", color="blue")

plt.yscale("log")
#plt.title("Aproximación de los números de Catalán")
plt.xlabel("Índice N")
plt.ylabel("C_N")
plt.legend(title="Figuras")
ruta_guardado = "../../img/catalan/Cn.pdf"
plt.savefig(ruta_guardado, format="pdf")



