import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("400x300")

# Crear un Entry (campo de texto)
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Crear un Label (etiqueta para mostrar texto)
etiqueta = tk.Label(ventana, text="Escribe algo y presiona el botón")
etiqueta.pack(pady=10)

# Función que se ejecuta al hacer clic en el botón
def mostrar_texto():
    texto = entrada.get()  # Obtener el texto del Entry
    etiqueta.config(text=f"Escribiste: {texto}")  # Mostrarlo en el Label

# Crear un Button (botón)
boton = tk.Button(ventana, text="Mostrar texto", command=mostrar_texto)
boton.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()
