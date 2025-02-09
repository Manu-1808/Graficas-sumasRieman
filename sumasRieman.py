import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import re

# Función para graficar
def graficar():
    try:
        # Obtener valores de la interfaz
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = int(entry_n.get())
        rectangles_above = var_rectangles.get() == "above"
        funcion = entry_funcion.get()

        # Validar la función ingresada
        if not re.match(r'^[0-9x+\-*/ ().]+$', funcion):
            raise ValueError("La función contiene caracteres no permitidos.")

        # Definir la función dinámicamente
        def f(x):
            return eval(funcion)

        # Crear datos para la función
        x = np.linspace(-2, 4, 400)
        y = f(x)

        # Limpiar la gráfica anterior
        ax.clear()

        # Graficar la función
        ax.plot(x, y, label=f'f(x) = {funcion}', color='blue')

        # Calcular el ancho de cada rectángulo
        dx = (b - a) / n

        # Dibujar los rectángulos
        for i in range(n):
            xi = a + i * dx  # Punto inicial del rectángulo
            if rectangles_above:
                # Rectángulos por encima (usando el punto final del intervalo)
                yi = f(xi + dx)
            else:
                # Rectángulos por debajo (usando el punto inicial del intervalo)
                yi = f(xi)
            
            # Añadir el rectángulo
            ax.add_patch(
                plt.Rectangle((xi, 0), dx, yi, edgecolor='red', facecolor='purple', alpha=0.5)
            )

        # Configuraciones adicionales
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title(f'Gráfica de f(x) con rectángulos {"por izquierda" if rectangles_above else "por derecha"}')
        ax.axhline(0, color='black', linewidth=0.5)  # Eje x
        ax.axvline(0, color='black', linewidth=0.5)  # Eje y
        ax.grid(True)
        ax.legend()

        # Redibujar el canvas
        canvas.draw()

    except Exception as e:
        # Mostrar mensaje de error en caso de problemas
        tk.messagebox.showerror("Error", f"Error al graficar: {str(e)}")

# Crear la ventana principal
root = tk.Tk()
root.title("Gráfica de Rectángulos")

# Marco para los controles
frame_controles = ttk.Frame(root, padding="10")
frame_controles.grid(row=0, column=0, sticky="ew")

# Etiquetas y entradas para los parámetros
ttk.Label(frame_controles, text="Límite inferior (a):").grid(row=0, column=0, sticky="w")
entry_a = ttk.Entry(frame_controles)
entry_a.insert(0, "1")  # Valor por defecto
entry_a.grid(row=0, column=1, sticky="ew")

ttk.Label(frame_controles, text="Límite superior (b):").grid(row=1, column=0, sticky="w")
entry_b = ttk.Entry(frame_controles)
entry_b.insert(0, "3")  # Valor por defecto
entry_b.grid(row=1, column=1, sticky="ew")

ttk.Label(frame_controles, text="Número de rectángulos (n):").grid(row=2, column=0, sticky="w")
entry_n = ttk.Entry(frame_controles)
entry_n.insert(0, "8")  # Valor por defecto
entry_n.grid(row=2, column=1, sticky="ew")

# Entrada para la función
ttk.Label(frame_controles, text="Función (f(x)):").grid(row=3, column=0, sticky="w")
entry_funcion = ttk.Entry(frame_controles)
entry_funcion.insert(0, "4*x + 1/2")  # Valor por defecto
entry_funcion.grid(row=3, column=1, sticky="ew")

# Radio buttons para seleccionar la posición de los rectángulos
var_rectangles = tk.StringVar(value="below")
ttk.Label(frame_controles, text="Posición de los rectángulos:").grid(row=4, column=0, sticky="w")
ttk.Radiobutton(frame_controles, text="Por derecha", variable=var_rectangles, value="below").grid(row=4, column=1, sticky="w")
ttk.Radiobutton(frame_controles, text="Por izquierda", variable=var_rectangles, value="above").grid(row=5, column=1, sticky="w")

# Botón para graficar
boton_graficar = ttk.Button(frame_controles, text="Graficar", command=graficar)
boton_graficar.grid(row=6, column=0, columnspan=2, pady=10)

# Marco para la gráfica
frame_grafica = ttk.Frame(root, padding="10")
frame_grafica.grid(row=1, column=0, sticky="nsew")

# Crear la figura de matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Ejecutar la aplicación
root.mainloop()