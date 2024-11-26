import tkinter as tk  # Importar la librería Tkinter para la interfaz gráfica
from tkinter import messagebox  # Importar para mostrar mensajes emergentes

# Clase Gasto: Representa un gasto con una categoría y un monto
class Gasto:
    def __init__(self, categoria, monto):
        # Inicialización de los atributos de la clase
        self.categoria = categoria  # La categoría del gasto (por ejemplo, 'Alimentos')
        self.monto = monto  # El monto del gasto (por ejemplo, 100.0)

# Clase ControlDeGastos: Controla los gastos registrados y calcula el total
class ControlDeGastos:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los objetos Gasto
        self.gastos = []

    def agregar_gasto(self, gasto):
        # Agrega un gasto a la lista de gastosP
        self.gastos.append(gasto)

    def calcular_total(self):
        # Calcula el total de los gastos sumando el monto de cada uno
        return sum(gasto.monto for gasto in self.gastos)

# Clase AplicacionGastos: Maneja la interfaz gráfica y las interacciones del usuario
class AplicacionGastos:
    def __init__(self, ventana):
        # Inicialización de los atributos de la clase
        self.controlador = ControlDeGastos()  # Crear un objeto ControlDeGastos
        self.ventana = ventana  # Asignar la ventana principal
        self.ventana.title("Control de Gastos")  # Título de la ventana

        # Crear y colocar etiquetas y campos de entrada para la categoría
        tk.Label(ventana, text="Categoría:").grid(row=0, column=0, padx=10, pady=5)
        self.campo_categoria = tk.Entry(ventana)  # Campo para ingresar la categoría
        self.campo_categoria.grid(row=0, column=1, padx=10, pady=5)

        # Crear y colocar etiquetas y campos de entrada para el monto
        tk.Label(ventana, text="Monto:").grid(row=1, column=0, padx=10, pady=5)
        self.campo_monto = tk.Entry(ventana)  # Campo para ingresar el monto
        self.campo_monto.grid(row=1, column=1, padx=10, pady=5)

        # Botón para agregar un nuevo gasto
        self.boton_agregar = tk.Button(ventana, text="Agregar Gasto", command=self.agregar_gasto)
        self.boton_agregar.grid(row=2, column=0, columnspan=2, pady=10)

        # Crear una lista para mostrar los gastos registrados
        self.lista_gastos = tk.Listbox(ventana, width=40, height=10)
        self.lista_gastos.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        # Botón para calcular y mostrar el total de los gastos
        self.boton_total = tk.Button(ventana, text="Mostrar Total", command=self.mostrar_total)
        self.boton_total.grid(row=4, column=0, columnspan=2, pady=10)

    # Método para agregar un gasto
    def agregar_gasto(self):
        categoria = self.campo_categoria.get()  # Obtener la categoría ingresada
        monto = self.campo_monto.get()  # Obtener el monto ingresado

        # Verificar si los campos están vacíos
        if not categoria or not monto:
            messagebox.showwarning("Advertencia", "Por favor completa todos los campos.")
            return

        # Intentar convertir el monto a un número flotante
        try:
            monto = float(monto)  # Convertir el monto a un número decimal
            gasto = Gasto(categoria, monto)  # Crear un nuevo objeto Gasto
            self.controlador.agregar_gasto(gasto)  # Agregar el gasto al controlador
            self.lista_gastos.insert(tk.END, f"{categoria}: ${monto:.2f}")  # Mostrar el gasto en la lista
            self.campo_categoria.delete(0, tk.END)  # Limpiar el campo de categoría
            self.campo_monto.delete(0, tk.END)  # Limpiar el campo de monto
        except ValueError:
            # Si no se puede convertir el monto a un número válido, mostrar un error
            messagebox.showerror("Error", "El monto debe ser un número válido.")

    # Método para mostrar el total de los gastos
    def mostrar_total(self):
        total = self.controlador.calcular_total()  # Calcular el total de los gastos
        # Mostrar el total en un cuadro de mensaje
        messagebox.showinfo("Total de Gastos", f"El total de gastos es: ${total:.2f}")


# Código principal para ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()  # Crear la ventana principal
    app = AplicacionGastos(ventana)  # Crear la aplicación
    ventana.mainloop()  # Ejecutar el bucle principal de Tkinter para mostrar la interfaz gráfica
