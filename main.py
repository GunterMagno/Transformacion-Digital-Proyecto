"""
Task Organizer with Auto-Prioritization

A Python application that automatically prioritizes tasks based on:
- Deadline urgency
- User-defined importance

Key Components:
1. Tkinter GUI Interface
2. SQLite Database
3. Priority Calculation Engine

Author: YourName
License: MIT
Version: 1.0
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
from datetime import datetime

# Conectar a la base de datos (se crea si no existe)
def conectar_db():
    return sqlite3.connect("tareas.db")

# Crear las tablas si no existen
def crear_tablas():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            plazo TEXT NOT NULL,
            importancia INTEGER NOT NULL,
            prioridad INTEGER,
            completada INTEGER DEFAULT 0
        )
    """)
    # Añadir la columna "completada" si no existe
    cursor.execute("PRAGMA table_info(tareas)")
    columnas = cursor.fetchall()
    columnas_existentes = [columna[1] for columna in columnas]
    if "completada" not in columnas_existentes:
        cursor.execute("ALTER TABLE tareas ADD COLUMN completada INTEGER DEFAULT 0")
    conexion.commit()
    conexion.close()

# Añadir una nueva tarea
def añadir_tarea_db(nombre, descripcion, plazo, importancia):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO tareas (nombre, descripcion, plazo, importancia)
        VALUES (?, ?, ?, ?)
    """, (nombre, descripcion, plazo, importancia))
    conexion.commit()
    conexion.close()
    actualizar_prioridades()

# Obtener todas las tareas no completadas ordenadas por prioridad
def obtener_tareas():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tareas WHERE completada = 0 ORDER BY prioridad DESC")
    tareas = cursor.fetchall()
    conexion.close()
    return tareas

# Obtener todas las tareas completadas
def obtener_tareas_completadas():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tareas WHERE completada = 1 ORDER BY plazo DESC")
    tareas = cursor.fetchall()
    conexion.close()
    return tareas

# Calcular la prioridad de una tarea
def calcular_prioridad(plazo, importancia):
    """
    Calculates dynamic task priority score
    
    Args:
        deadline (str): YYYY-MM-DD format
        importance (int): 1-10 scale
    
    Returns:
        int: Priority score (higher = more urgent)
    
    Example:
        >>> calculate_priority("2024-12-31", 5)
        25
    """
    hoy = datetime.now().date()
    plazo = datetime.strptime(plazo, "%Y-%m-%d").date()
    dias_restantes = (plazo - hoy).days
    return importancia * 10 - dias_restantes

# Actualizar las prioridades de todas las tareas
def actualizar_prioridades():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, plazo, importancia FROM tareas WHERE completada = 0")
    tareas = cursor.fetchall()
    for tarea in tareas:
        id_tarea, plazo, importancia = tarea
        prioridad = calcular_prioridad(plazo, importancia)
        cursor.execute("""
            UPDATE tareas
            SET prioridad = ?
            WHERE id = ?
        """, (prioridad, id_tarea))
    conexion.commit()
    conexion.close()

# Marcar una tarea como completada
def marcar_completada(id_tarea):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE tareas
        SET completada = 1
        WHERE id = ?
    """, (id_tarea,))
    conexion.commit()
    conexion.close()

# Eliminar una tarea
def eliminar_tarea(id_tarea):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = ?", (id_tarea,))
    conexion.commit()
    conexion.close()

# Editar una tarea
def editar_tarea(id_tarea, nombre, descripcion, plazo, importancia):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE tareas
        SET nombre = ?, descripcion = ?, plazo = ?, importancia = ?
        WHERE id = ?
    """, (nombre, descripcion, plazo, importancia, id_tarea))
    conexion.commit()
    conexion.close()
    actualizar_prioridades()

# Función para añadir una tarea desde la interfaz
def añadir_tarea_ui():
    nombre = entry_nombre.get().strip()
    descripcion = entry_descripcion.get().strip()
    plazo = entry_plazo.get().strip()
    importancia = entry_importancia.get().strip()

    if nombre and plazo and importancia:
        try:
            importancia = int(importancia)
            if 1 <= importancia <= 10:
                añadir_tarea_db(nombre, descripcion, plazo, importancia)
                mostrar_tareas()
                entry_nombre.delete(0, tk.END)
                entry_descripcion.delete(0, tk.END)
                entry_plazo.delete(0, tk.END)
                entry_importancia.delete(0, tk.END)
            else:
                messagebox.showwarning("Error", "La importancia debe ser un número entre 1 y 10.")
        except ValueError:
            messagebox.showwarning("Error", "La importancia debe ser un número.")
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios.")

# Función para mostrar las tareas en la tabla
def mostrar_tareas():
    # Limpiar la tabla
    for row in tree_tareas.get_children():
        tree_tareas.delete(row)
    
    # Obtener las tareas y mostrarlas en la tabla
    tareas = obtener_tareas()
    for tarea in tareas:
        tree_tareas.insert("", "end", values=(tarea[1], tarea[2], tarea[5]))

# Función para mostrar las tareas completadas
def mostrar_tareas_completadas():
    # Limpiar la tabla de tareas completadas
    for row in tree_completadas.get_children():
        tree_completadas.delete(row)
    
    # Obtener las tareas completadas y mostrarlas en la tabla
    tareas = obtener_tareas_completadas()
    for tarea in tareas:
        tree_completadas.insert("", "end", values=(tarea[1], tarea[2], tarea[5]))

# Función para editar una tarea seleccionada
def editar_tarea_ui():
    seleccion = tree_tareas.selection()
    if seleccion:
        item_id = seleccion[0]
        valores = tree_tareas.item(item_id, "values")
        nombre = valores[0]
        
        tareas = obtener_tareas()
        for tarea in tareas:
            if tarea[1] == nombre:
                id_tarea = tarea[0]
                nombre = simpledialog.askstring("Editar Tarea", "Nombre:", initialvalue=tarea[1])
                descripcion = simpledialog.askstring("Editar Tarea", "Descripción:", initialvalue=tarea[2])
                plazo = simpledialog.askstring("Editar Tarea", "Plazo (YYYY-MM-DD):", initialvalue=tarea[3])
                importancia = simpledialog.askstring("Editar Tarea", "Importancia (1-10):", initialvalue=tarea[4])
                if nombre and plazo and importancia:
                    try:
                        importancia = int(importancia)
                        if 1 <= importancia <= 10:
                            editar_tarea(id_tarea, nombre, descripcion, plazo, importancia)
                            mostrar_tareas()
                        else:
                            messagebox.showwarning("Error", "La importancia debe ser un número entre 1 y 10.")
                    except ValueError:
                        messagebox.showwarning("Error", "La importancia debe ser un número.")
                break
    else:
        messagebox.showwarning("Error", "Selecciona una tarea para editar.")

# Función para marcar una tarea como completada
def completar_tarea_ui():
    seleccion = tree_tareas.selection()
    if seleccion:
        item_id = seleccion[0]
        valores = tree_tareas.item(item_id, "values")
        nombre = valores[0]
        
        tareas = obtener_tareas()
        for tarea in tareas:
            if tarea[1] == nombre:
                id_tarea = tarea[0]
                marcar_completada(id_tarea)
                mostrar_tareas()
                mostrar_tareas_completadas()
                break
    else:
        messagebox.showwarning("Error", "Selecciona una tarea para marcar como completada.")

# Función para eliminar una tarea seleccionada
def eliminar_tarea_ui():
    seleccion = tree_tareas.selection()
    if seleccion:
        item_id = seleccion[0]
        valores = tree_tareas.item(item_id, "values")
        nombre = valores[0]
        
        tareas = obtener_tareas()
        for tarea in tareas:
            if tarea[1] == nombre:
                id_tarea = tarea[0]
                eliminar_tarea(id_tarea)
                mostrar_tareas()
                break
    else:
        messagebox.showwarning("Error", "Selecciona una tarea para eliminar.")

# Función para eliminar una tarea completada seleccionada
def eliminar_tarea_completada_ui():
    seleccion = tree_completadas.selection()
    if seleccion:
        item_id = seleccion[0]
        valores = tree_completadas.item(item_id, "values")
        nombre = valores[0]
        
        tareas = obtener_tareas_completadas()
        for tarea in tareas:
            if tarea[1] == nombre:
                id_tarea = tarea[0]
                eliminar_tarea(id_tarea)
                mostrar_tareas_completadas()
                break
    else:
        messagebox.showwarning("Error", "Selecciona una tarea completada para eliminar.")

# Función para borrar todas las tareas completadas
def borrar_tareas_completadas_ui():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM tareas WHERE completada = 1")
    conexion.commit()
    conexion.close()
    mostrar_tareas_completadas()

# Función para deseleccionar una tarea
def deseleccionar_tarea(event):
    # Verificar si el clic fue fuera de la tabla
    if not tree_tareas.identify_row(event.y):
        tree_tareas.selection_remove(tree_tareas.selection())

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Organizador de Tareas")
ventana.geometry("800x600")

# Campos de entrada
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

label_nombre = tk.Label(frame_entrada, text="Nombre de la tarea:")
label_nombre.grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_entrada)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

label_descripcion = tk.Label(frame_entrada, text="Descripción:")
label_descripcion.grid(row=1, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=1, column=1, padx=5, pady=5)

label_plazo = tk.Label(frame_entrada, text="Plazo (YYYY-MM-DD):")
label_plazo.grid(row=2, column=0, padx=5, pady=5)
entry_plazo = tk.Entry(frame_entrada)
entry_plazo.grid(row=2, column=1, padx=5, pady=5)

label_importancia = tk.Label(frame_entrada, text="Importancia (1-10):")
label_importancia.grid(row=3, column=0, padx=5, pady=5)
entry_importancia = tk.Entry(frame_entrada)
entry_importancia.grid(row=3, column=1, padx=5, pady=5)

# Botones de acciones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton_añadir = tk.Button(frame_botones, text="Añadir Tarea", command=añadir_tarea_ui)
boton_añadir.grid(row=0, column=0, padx=5)

boton_editar = tk.Button(frame_botones, text="Editar Tarea", command=editar_tarea_ui)
boton_editar.grid(row=0, column=1, padx=5)

boton_completar = tk.Button(frame_botones, text="Marcar como Completada", command=completar_tarea_ui)
boton_completar.grid(row=0, column=2, padx=5)

boton_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea_ui)
boton_eliminar.grid(row=0, column=3, padx=5)

# Tabla de tareas pendientes
frame_tareas = tk.Frame(ventana)
frame_tareas.pack(pady=10)

label_tareas = tk.Label(frame_tareas, text="Tareas Pendientes:")
label_tareas.pack()

# Crear Treeview para tareas pendientes
tree_tareas = ttk.Treeview(frame_tareas, columns=("Nombre", "Descripción", "Prioridad"), show="headings", selectmode="browse")
tree_tareas.heading("Nombre", text="Nombre")
tree_tareas.heading("Descripción", text="Descripción")
tree_tareas.heading("Prioridad", text="Prioridad")
tree_tareas.pack()

# Asignar evento para deseleccionar filas
tree_tareas.bind("<Button-1>", deseleccionar_tarea)

# Tabla de tareas completadas
frame_completadas = tk.Frame(ventana)
frame_completadas.pack(pady=10)

label_completadas = tk.Label(frame_completadas, text="Tareas Completadas:")
label_completadas.pack()

# Crear Treeview para tareas completadas
tree_completadas = ttk.Treeview(frame_completadas, columns=("Nombre", "Descripción", "Prioridad"), show="headings", selectmode="browse")
tree_completadas.heading("Nombre", text="Nombre")
tree_completadas.heading("Descripción", text="Descripción")
tree_completadas.heading("Prioridad", text="Prioridad")
tree_completadas.pack()

# Botones para tareas completadas
frame_botones_completadas = tk.Frame(ventana)
frame_botones_completadas.pack(pady=10)

boton_eliminar_completada = tk.Button(frame_botones_completadas, text="Eliminar Tarea Completada", command=eliminar_tarea_completada_ui)
boton_eliminar_completada.grid(row=0, column=0, padx=5)

boton_borrar_completadas = tk.Button(frame_botones_completadas, text="Borrar Todas las Completadas", command=borrar_tareas_completadas_ui)
boton_borrar_completadas.grid(row=0, column=1, padx=5)

# Inicialización de la base de datos y muestra de tareas
crear_tablas()
mostrar_tareas()
mostrar_tareas_completadas()

# Ejecutar la aplicación
ventana.mainloop()
