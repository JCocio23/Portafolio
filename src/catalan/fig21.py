import numpy as np
import matplotlib.pyplot as plt
import funciones_utiles as fu
plt.rcParams.update({'font.size': 14})

x = 14
x_eje = np.arange(x + 1) #Tenemos 15 valores, por lo que se ingresan x+1 a np.arange para un arreglo
                         # de x elementos, todos enteros partiendo desde 0.
y = fu.catalan_numpy(x, dtype=np.int16)
w = fu.catalan_numpy(x, dtype=np.int32) #se evalua la función a distinta presición sobre el arreglo.
u = fu.catalan_numpy(x, dtype=np.int64)

z = fu.catalan_numpy(x, dtype=np.float128)#valor de referencia

plt.figure(figsize=(10,6))

plt.scatter(x_eje, z, label="np.float128 (Referencia)", marker="x", color="black", s=60, zorder=1)
plt.scatter(x_eje, y, label="np.int16", marker="o", color="red", s=40, zorder=2) 
plt.scatter(x_eje, w, label="np.int32", marker="*", color="purple", s=40, zorder=3)
plt.scatter(x_eje, u, label="np.int64", marker="D", color="green", s=40, zorder=4)

plt.yscale('log') #eje vertical semi-logaritmico

#plt.title(r"catalan_numpy(N) a distintas presiciones")
plt.xlabel("Índice N")
plt.ylabel(r"C_N")
plt.legend(title="dtype de catalan_numpy")
ruta_guardado = "../../img/catalan/dtype.pdf"
plt.savefig(ruta_guardado, format="pdf") #guarda el gráfico vectorial en la carpeta img/catalan/ del portafolio
plt.show()
