# 🎯 **Organizador de Tareas con Priorización Automática**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-orange)

**Organizador de Tareas con Priorización Automática** es una aplicación de escritorio que te ayuda a gestionar tus tareas de manera eficiente. El software calcula automáticamente la prioridad de cada tarea en función de su **plazo** y **importancia**, permitiéndote enfocarte en lo más urgente e importante.

---

## 🚀 **Características Principales**

- ✅ **Priorización automática**: Calcula la prioridad de las tareas en función del plazo y la importancia.
- ✅ **Interfaz gráfica intuitiva**: Usa `Tkinter` para una experiencia de usuario sencilla y amigable.
- ✅ **Base de datos SQLite**: Almacena las tareas de manera persistente.
- ✅ **Funcionalidades avanzadas**:
  - Añadir, editar y eliminar tareas.
  - Marcar tareas como completadas.
  - Ver tareas pendientes y completadas en tablas separadas.
  - Eliminar tareas completadas individualmente o borrar toda la lista.

---

## 🛠️ **Cómo Funciona**

### 1️⃣ **Captura de Datos**
El usuario ingresa los siguientes datos para cada tarea:
- **Nombre**: Nombre de la tarea.
- **Descripción**: Detalles adicionales sobre la tarea.
- **Plazo**: Fecha límite en formato `YYYY-MM-DD`.
- **Importancia**: Nivel de importancia de la tarea (del 1 al 10).

### 2️⃣ **Cálculo de Prioridad**
La prioridad de cada tarea se calcula automáticamente usando la siguiente fórmula:
prioridad = importancia * 10 - días_restantes

- **Importancia**: Nivel de importancia de la tarea (del 1 al 10).
- **Días restantes**: Diferencia entre la fecha actual y el plazo de la tarea.

**Ejemplo**:
- Si una tarea tiene una importancia de `8` y faltan `5` días para su plazo: prioridad = ``8 * 10 - 5 = 75``

### 3️⃣ **Almacenamiento en Base de Datos**
Las tareas se almacenan en una base de datos SQLite (`tareas.db`) con la siguiente estructura:

| Columna      | Tipo        | Descripción                              |
|--------------|-------------|------------------------------------------|
| `id`         | INTEGER     | Identificador único de la tarea.         |
| `nombre`     | TEXT        | Nombre de la tarea.                      |
| `descripcion`| TEXT        | Descripción de la tarea.                 |
| `plazo`      | TEXT        | Fecha límite de la tarea (`YYYY-MM-DD`). |
| `importancia`| INTEGER     | Nivel de importancia (1-10).             |
| `prioridad`  | INTEGER     | Prioridad calculada automáticamente.     |
| `completada` | INTEGER     | Estado de la tarea (0: pendiente, 1: completada). |

### 4️⃣ **Interfaz Gráfica**
La interfaz gráfica está dividida en dos secciones principales:
- **Tareas Pendientes**: Muestra las tareas ordenadas por prioridad (de mayor a menor).
- **Tareas Completadas**: Muestra las tareas que han sido marcadas como completadas.

---

## 📥 **Instalación**

### 1️⃣ **Requisitos**
- Python 3.x
- Biblioteca `tkinter` (viene por defecto con Python).
- Biblioteca `sqlite3` (viene por defecto con Python).

### 2️⃣ **Clonar el Repositorio**
```bash
git clone https://github.com/tuusuario/organizador-tareas.git
cd organizador-tareas
```

3️⃣ Ejecutar el Programa
```bash
python main.py
```