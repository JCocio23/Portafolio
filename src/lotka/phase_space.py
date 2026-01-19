import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})


def Ham(p,d, mu):
    return np.log(d) - d + mu*(np.log(p) - p) #Hamiltoniano

plt.figure(figsize=(15,5)) #Espacio de Fase 1
mu = [0.5, 1, 5]
p,d = np.mgrid[1e-5:5:100j, 1e-5:5:100j]
#plt.suptitle(r"Espacio de fases a distinto $\mu$")
for i in mu:
    H = Ham(p,d,i)
    u = str(i)
    plt.subplot(1,3,mu.index(i)+1)
    plt.contour(p,d,H, levels=100)
    if i==5:
        plt.colorbar(label="Hamiltoniano")
    else:
        plt.colorbar()
    plt.scatter(1,1, color="black")
    plt.xlabel(r"$p$")
    plt.ylabel(r"$d$")
    plt.title(r"$\mu=$" + u)
    ruta_guardado = "../../img/lotka/lotka_phase_space.pdf"
    plt.savefig(ruta_guardado, format="pdf")
##plt.show()

plt.figure(figsize=(15,5)) #Espacio de Fase 1, zoom
mu = [0.5, 1, 5]
p,d = np.mgrid[1e-5:1:100j, 1e-5:1:100j]
#plt.suptitle(r"Espacio de fases a distinto $\mu$")
for i in mu:
    H = Ham(p,d,i)
    u = str(i)
    plt.subplot(1,3,mu.index(i)+1)
    plt.contour(p,d,H, levels=100)
    if i==5:
        plt.colorbar(label="Hamiltoniano")
    else:
        plt.colorbar()
    plt.scatter(1,1, color="black")
    plt.xlabel(r"$p$")
    plt.ylabel(r"$d$")
    plt.title(r"$\mu=$" + u)
    ruta_guardado = "../../img/lotka/lotka_phase_space_zoom.pdf"
    plt.savefig(ruta_guardado, format="pdf")
#plt.show()


k = np.array([1, 4.2, 4, 2])

g = np.array([2, 3.2, 1, 5])

# Creamos una lista de tuplas (p, d) para iterar fácilmente
POINTS_TO_HIGHLIGHT = list(zip(k, g))

# --- Configuración del Plot ---
plt.figure(figsize=(15, 5))
mu_values = [0.5, 1, 5]
# Malla de p y d: p, d ahora van de 1e-5 a 5, como en su código actualizado
p, d = np.mgrid[1e-5:10:100j, 1e-5:10:100j]
#plt.suptitle(r"Espacio de fases a distinto $\mu$")

# --- Bucle Principal de Trazado ---
for i_mu, current_mu in enumerate(mu_values):
    plt.subplot(1, 3, i_mu + 1)
    
    # 1. Calcular el Hamiltoniano en toda la malla
    H_mesh = Ham(p, d, current_mu)
    
    # 2. Calcular los valores de H (niveles) para los puntos iniciales a destacar
    H_levels_to_highlight = []
    for p0, d0 in POINTS_TO_HIGHLIGHT:
        # Puntos (1, 1) son el centro; su H(1,1) = -(mu+1) ya se marca con el scatter.
        # Evitamos calcular H para (1,1) ya que es un punto de silla/máximo.
        if p0 != 1 or d0 != 1:
            H_value = Ham(p0, d0, current_mu)
            H_levels_to_highlight.append(H_value)
    
    # 3. Trazar TODAS las demás trayectorias en GRIS (Fondo)
    # Usamos muchos niveles y baja opacidad para crear el mapa de fase.
    plt.contour(p, d, H_mesh, levels=100, colors='gray', alpha=0.3, linewidths=0.8)
    
    # 4. Trazar las trayectorias destacadas en COLOR
    # Trazamos SOLO los niveles H calculados, con un color y ancho de línea distintivo.
    if H_levels_to_highlight:
        # Usamos 'Reds' para que cada trayectoria destacada tenga un tono distinto si es necesario
        highlight_contour = plt.contour(p, d, H_mesh, levels=sorted(H_levels_to_highlight), colors='red', linewidths=2.0, zorder=3)
    
    # 5. Marcar los puntos críticos y los puntos iniciales
    plt.scatter(1, 1, color="black", marker='o', s=40, label="Centro (1,1)", zorder=4)
    plt.scatter(k, g, color='purple', marker='o', s=40, label="Cond. Iniciales", zorder=5)
    
    # 6. Etiquetas y título
    u_str = str(current_mu)
    plt.xlabel(r"$p$")
    plt.ylabel(r"$d$")
    plt.title(r"$\mu=$" + u_str)
    
    # Añadir barra de color (solo para el último subplot, como pidió)
   # if current_mu == 5:
    #    plt.colorbar(label="Hamiltoniano $H$", orientation="vertical")
    
    # Añadir leyenda
    if i_mu == 0:
        # Creamos handles manuales para la leyenda:
        # Una línea roja para la trayectoria destacada, un punto azul para el inicial
        from matplotlib.lines import Line2D
        custom_lines = [
            Line2D([0], [0], color='gray', lw=1, alpha=0.5),
            Line2D([0], [0], color='red', lw=2),
            Line2D([0], [0], color='black', marker='o', linestyle='None', markersize=6),
            Line2D([0], [0], color='purple', marker='o', linestyle='None', markersize=8)
        ]
        plt.legend(custom_lines, ['Otras Trayectorias', 'Tray. Destacada', 'Centro (1,1)', 'Cond. Iniciales'], loc='upper right', fontsize=8)


# Guardado y Visualización
ruta_guardado = "../../img/lotka/lotka_phase_space_highlighted_final.pdf"
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajustar para el suptitle
plt.savefig(ruta_guardado, format="pdf")

plt.show()
