# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# TAREA: APLICACIÓN GUI DE LISTA DE TAREAS PROFESIONAL
# Estudiante: Rosario Chamba.
# Universidad Estatal Amazónica.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import tkinter as tk
from tkinter import messagebox

# --- LÓGICA Y MANEJADORES DE EVENTOS ---

def actualizar_barra_estado(mensaje):
    """
    Actualiza el texto de la barra inferior.
    Muestra un mensaje de acción y el conteo total de tareas.
    """
    total = lista_tareas.size()
    barra_estado.config(text=f" Estado: {mensaje} | Tareas en lista: {total}")


def mostrar_bienvenida():
    """Evento que se dispara al iniciar la aplicación."""
    messagebox.showinfo("¡Bienvenida!", "Hola Rosario, ¿lista para organizar tus tareas hoy?")
    actualizar_barra_estado("Aplicación lista para usar")


def salir_aplicacion():
    """Evento que gestiona el cierre de la ventana principal."""
    if messagebox.askyesno("Salir", "¿Estás segura de que deseas cerrar el programa?"):
        messagebox.showinfo("Despedida", "¡Hasta pronto, Rosario! Éxitos en tus estudios.")
        ventana.destroy()


def añadir_tarea(event=None):
    """
    Añade una nueva tarea a la Listbox.
    Se activa con el botón 'Añadir' o con la tecla 'Enter'.
    """
    tarea = entrada_tarea.get()
    if tarea.strip() != "":
        lista_tareas.insert(tk.END, f"• {tarea}")
        entrada_tarea.delete(0, tk.END)  # Limpia la caja de texto
        actualizar_barra_estado("Tarea añadida con éxito")
    else:
        messagebox.showwarning("Atención", "Por favor, escribe algo en el campo de texto.")
        actualizar_barra_estado("Error: Intento de añadir tarea vacía")


def marcar_completada():
    """
    Cambia visualmente la tarea a color verde y le pone un check.
    Se activa con el botón 'Completada' o con 'Doble Clic' en la lista.
    """
    try:
        indice = lista_tareas.curselection()[0]
        tarea_texto = lista_tareas.get(indice)

        if not tarea_texto.startswith("✔"):
            # Reemplaza el punto inicial por un check
            nueva_tarea = f"✔ {tarea_texto[2:]}"
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, nueva_tarea)
            lista_tareas.itemconfig(indice, fg="green")
            actualizar_barra_estado("¡Tarea marcada como completada!")
    except IndexError:
        messagebox.showwarning("Selección", "Primero selecciona una tarea de la lista.")


def eliminar_tarea():
    """Elimina la tarea seleccionada de la lista."""
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
        actualizar_barra_estado("Tarea eliminada correctamente")
    except IndexError:
        messagebox.showwarning("Selección", "Selecciona qué tarea deseas eliminar.")


# --- CONFIGURACIÓN DE LA INTERFAZ GRÁFICA (GUI) ---

ventana = tk.Tk()
ventana.title("Gestor de Tareas IT - Rosario Chamba")
ventana.geometry("450x600")
ventana.configure(bg="#f4f7f6")

# Vincular la "X" de la ventana con la función de salida
ventana.protocol("WM_DELETE_WINDOW", salir_aplicacion)

# Etiqueta de Título
lbl_titulo = tk.Label(ventana, text="Mi Planificador Diario", font=("Arial", 16, "bold"), bg="#f4f7f6", fg="#2c3e50")
lbl_titulo.pack(pady=20)

# Campo de entrada (Entry)
entrada_tarea = tk.Entry(ventana, font=("Arial", 12), width=30, bd=2, relief="groove")
entrada_tarea.pack(pady=10)
entrada_tarea.focus_set()

# ESCUCHADOR DE EVENTO: Tecla Enter
entrada_tarea.bind('<Return>', añadir_tarea)

# Contenedor de botones
frame_botones = tk.Frame(ventana, bg="#f4f7f6")
frame_botones.pack(pady=10)

btn_add = tk.Button(frame_botones, text="Añadir", command=añadir_tarea, bg="#28a745", fg="white", width=12,
                    font=("Arial", 10, "bold"))
btn_add.grid(row=0, column=0, padx=5)

btn_done = tk.Button(frame_botones, text="Completada", command=marcar_completada, bg="#007bff", fg="white", width=12,
                     font=("Arial", 10, "bold"))
btn_done.grid(row=0, column=1, padx=5)

# Lista de tareas (Listbox)
lista_tareas = tk.Listbox(ventana, font=("Arial", 11), width=45, height=12, bd=1, relief="solid")
lista_tareas.pack(pady=15, padx=20)

# ESCUCHADOR DE EVENTO: Doble clic en la lista
lista_tareas.bind('<Double-Button-1>', lambda e: marcar_completada())

btn_del = tk.Button(ventana, text="Eliminar Seleccionada", command=eliminar_tarea, bg="#dc3545", fg="white", width=30,
                    font=("Arial", 10, "bold"))
btn_del.pack(pady=5)

# --- BARRA DE ESTADO (STATUS BAR) ---
# Se ubica al final (bottom) y se expande en horizontal (fill x)
barra_estado = tk.Label(ventana, text="Iniciando...", bd=1, relief="sunken", anchor="w", font=("Arial", 9, "italic"),
                        bg="#e0e0e0")
barra_estado.pack(side="bottom", fill="x")

# Lanzar saludo de bienvenida después de medio segundo
ventana.after(500, mostrar_bienvenida)

# Mantener la aplicación en escucha de eventos
ventana.mainloop()
