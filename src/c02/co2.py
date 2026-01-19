import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14}) 
# Lectura de datos
years, values = np.genfromtxt(
    "datos.txt",
    comments="#",
    usecols=(2, 3),
    unpack=True
)
plt.figure(figsize=(8,6))
plt.scatter(years, values, color="green", label="Datos", s=10, marker="o")
plt.xlabel("Años")
plt.ylabel(r"Concentración promedio de CO$_2$ (ppm)")
plt.grid(True)
ruta_guardado = "../../img/co2/keeling.pdf"
plt.savefig(ruta_guardado, format="pdf")
plt.show()

def fil_norm(t, y, t_min, t_max):
    mask = (t >= t_min) & (t <= t_max)
    t_sel = t[mask]
    y_sel = y[mask]

    t_centro = 0.5 * (t_sel.min() + t_sel.max())
    ancho = t_sel.max() - t_sel.min()
    tau = 2 * (t_sel - t_centro) / ancho

    return t_sel, y_sel, tau, t_centro, ancho



t_sel, y_sel, tau, t0, L = fil_norm(years, values, years.max()-5, years.max())

# Definición del modelo
grado = 3
m = len(tau)
n = 1 + 3 * grado

# Matriz de diseño
B = np.zeros((m, n))
B[:, 0] = 1.0

for j in range(1, grado + 1):
    idx = 1 + 3 * (j - 1)
    B[:, idx]     = tau ** j
    B[:, idx + 1] = np.cos(2 * np.pi * j * tau)
    B[:, idx + 2] = np.sin(2 * np.pi * j * tau)

# Ajuste por mínimos cuadrados (ecuaciones normales)
BT = B.T
coef_fit = np.linalg.inv(BT @ B) @ (BT @ y_sel)

# Función del modelo
def modelo_tau(tau, coef):
    f = coef[0]
    k = 1
    for j in range(1, 4):
        f += coef[k]     * tau**j
        f += coef[k + 1] * np.cos(2 * np.pi * j * tau)
        f += coef[k + 2] * np.sin(2 * np.pi * j * tau)
        k += 3
    return f

# Evaluación y error
y_fit = modelo_tau(tau, coef_fit)
mse_value = np.mean((y_sel - y_fit) ** 2)
print(coef_fit)





# Gráfico
t_plot = np.linspace(-1, 1, 1000)
print(np.std(y_fit))
residuos = y_sel - y_fit

fig, axs = plt.subplots(1, 2, figsize=(14,6), sharex=False)

# --- Panel izquierdo: datos + ajuste ---
axs[0].plot(tau, y_sel, 'o', label="Datos", color="green")
axs[0].plot(t_plot, modelo_tau(t_plot, coef_fit), '-', label="Ajuste", color="red")
axs[0].set_xlabel(r'$\tau$')
axs[0].set_ylabel(r'Concentración de niveles de CO$_2$ (ppm)')
axs[0].grid(True)
axs[0].legend()

# --- Panel derecho: residuos ---
axs[1].scatter(tau, residuos, color="green", marker="o", s=40)
axs[1].axhline(0, color='black', linestyle='--', linewidth=1)
axs[1].set_xlabel(r"$\tau$")
axs[1].set_ylabel(r"Residuos (ppm)")
axs[1].grid(True)

plt.tight_layout()
ruta_guardado = "../../img/co2/ajuste_residuos_5.pdf"
plt.savefig(ruta_guardado, format="pdf")
plt.show()


#extrapolacion

year_back = 1970
mask_back = years >= year_back
years_back = years[mask_back]
values_back = values[mask_back]

# tau asociado (MISMA normalización del ajuste)
tau_back = 2 * (years_back - t0) / L
tau_model = np.linspace(tau_back.min(), tau.max(), 1500)
y_model = modelo_tau(tau_model, coef_fit)
plt.figure(figsize=(10,6))

# Datos reales (solo hasta el año elegido)
plt.scatter(
    tau_back, values_back,
    s=10, color="green", label="Datos reales", marker="o"
)

# Modelo ajustado + extrapolación
plt.plot(
    tau_model, y_model,
    color="red", linewidth=2, label="Modelo (extrapolación)"
)
plt.xlabel(r"Tiempo normalizado $\tau$")
plt.ylabel(r"Concentración promedio de CO$_2$ (ppm)")
plt.legend()
plt.grid(True)
ruta_guardado = "../../img/co2/extrapolacion.pdf"
plt.savefig(ruta_guardado, format="pdf")
plt.show()



