🎯 Organizador de Tareas con Priorización Automática
📌 Descripción
Organizador de Tareas con Priorización Automática es una aplicación de escritorio que te ayuda a gestionar tus tareas de manera eficiente. El software calcula automáticamente la prioridad de cada tarea en función de su plazo y importancia, permitiéndote enfocarte en lo más urgente e importante.

🚀 Características
Priorización automática: Calcula la prioridad de las tareas en función del plazo y la importancia.

Interfaz gráfica intuitiva: Usa Tkinter para una experiencia de usuario sencilla y amigable.

Base de datos SQLite: Almacena las tareas de manera persistente.

Funcionalidades avanzadas:

Añadir, editar y eliminar tareas.

Marcar tareas como completadas.

Ver tareas pendientes y completadas en tablas separadas.

Eliminar tareas completadas individualmente o borrar toda la lista.

🛠️ Cómo Funciona
1️⃣ Captura de Datos
El usuario ingresa los siguientes datos para cada tarea:

Nombre: Nombre de la tarea.

Descripción: Detalles adicionales sobre la tarea.

Plazo: Fecha límite en formato YYYY-MM-DD.

Importancia: Nivel de importancia de la tarea (del 1 al 10).

2️⃣ Cálculo de Prioridad
La prioridad de cada tarea se calcula automáticamente usando la siguiente fórmula:

Copy
prioridad = importancia * 10 - días_restantes
Importancia: Nivel de importancia de la tarea (del 1 al 10).

Días restantes: Diferencia entre la fecha actual y el plazo de la tarea.

Ejemplo:

Si una tarea tiene una importancia de 8 y faltan 5 días para su plazo:

Copy
prioridad = 8 * 10 - 5 = 75
3️⃣ Almacenamiento en Base de Datos
Las tareas se almacenan en una base de datos SQLite (tareas.db) con la siguiente estructura:

Columna	Tipo	Descripción
id	INTEGER	Identificador único de la tarea.
nombre	TEXT	Nombre de la tarea.
descripcion	TEXT	Descripción de la tarea.
plazo	TEXT	Fecha límite de la tarea (YYYY-MM-DD).
importancia	INTEGER	Nivel de importancia (1-10).
prioridad	INTEGER	Prioridad calculada automáticamente.
completada	INTEGER	Estado de la tarea (0: pendiente, 1: completada).
4️⃣ Interfaz Gráfica
La interfaz gráfica está dividida en dos secciones principales:

Tareas Pendientes: Muestra las tareas ordenadas por prioridad (de mayor a menor).

Tareas Completadas: Muestra las tareas que han sido marcadas como completadas.

📥 Instalación
1️⃣ Requisitos
Python 3.x

Biblioteca tkinter (viene por defecto con Python).

Biblioteca sqlite3 (viene por defecto con Python).

2️⃣ Clonar el repositorio
bash
Copy
git clone https://github.com/tuusuario/organizador-tareas.git
cd organizador-tareas
3️⃣ Ejecutar el programa
bash
Copy
python main.py
⚙️ Configuración
El programa no requiere configuración adicional. Sin embargo, puedes modificar el archivo main.py para personalizar:

Colores de la interfaz.

Nombres de las columnas en la tabla de tareas.

🛠️ Funcionalidades
Añadir una Tarea
Ingresa el nombre, descripción, plazo e importancia de la tarea.

Haz clic en Añadir Tarea.

Editar una Tarea
Selecciona una tarea en la tabla de tareas pendientes.

Haz clic en Editar Tarea.

Modifica los campos y guarda los cambios.

Marcar como Completada
Selecciona una tarea en la tabla de tareas pendientes.

Haz clic en Marcar como Completada.

Eliminar una Tarea
Selecciona una tarea en la tabla de tareas pendientes o completadas.

Haz clic en Eliminar Tarea.

Borrar Todas las Tareas Completadas
Haz clic en Borrar Todas las Completadas.

📌 Futuras Mejoras
✅ Integración con calendarios: Sincronizar tareas con Google Calendar o Outlook.

✅ Notificaciones: Recordatorios para tareas próximas a su plazo.

✅ Exportación de tareas: Exportar la lista de tareas a un archivo CSV o PDF.

🤝 Contribuir
¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, sigue estos pasos:

Haz un fork del repositorio.

Crea una rama con tu nueva funcionalidad (git checkout -b nueva-funcionalidad).

Realiza tus cambios y haz commit (git commit -m "Añade nueva funcionalidad").

Haz push a la rama (git push origin nueva-funcionalidad).

Abre un Pull Request en GitHub.

📄 Licencia
Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.

📧 Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

Email: tuemail@example.com

GitHub: tuusuario

¡Gracias por usar Organizador de Tareas con Priorización Automática! 😊