# Ciclo de vida del dato (5b)

## ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?

- **Generación:** Los datos se generan cuando el usuario ingresa una nueva tarea a través de la interfaz gráfica. Los campos incluyen nombre, descripción, plazo e importancia.
- **Almacenamiento:** Los datos se almacenan en una base de datos SQLite (`tareas.db`) en una tabla llamada `tareas`. Cada tarea tiene un identificador único (`id`), y se calcula automáticamente su prioridad.
- **Procesamiento:** La prioridad de cada tarea se recalcula automáticamente en función de la importancia y los días restantes hasta el plazo.
- **Consulta:** Los datos se consultan para mostrar las tareas pendientes y completadas en las tablas correspondientes.
- **Eliminación:** Las tareas se pueden eliminar individualmente o en grupo (por ejemplo, todas las tareas completadas). La eliminación se realiza mediante consultas SQL que borran registros de la base de datos.

## ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?

- **Validación de datos:** Se validan los campos de entrada (nombre, plazo, importancia) para asegurar que no estén vacíos y que los valores sean correctos (por ejemplo, la importancia debe ser un número entre 1 y 10).
- **Actualización automática:** La prioridad de las tareas se recalcula automáticamente cada vez que se añade o edita una tarea, lo que garantiza que los datos estén siempre actualizados.
- **Transacciones SQLite:** Se utilizan transacciones para garantizar que las operaciones de base de datos (inserción, actualización, eliminación) se completen correctamente y no dejen la base de datos en un estado inconsistente.

## Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?

En este proyecto ya se trabaja con datos, pero si no fuera el caso, se podría implementar una base de datos local (como SQLite) o un sistema de archivos estructurado (JSON, CSV) para almacenar y gestionar la información de manera eficiente.

# Almacenamiento en la nube (5f)

## Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?

Actualmente, el proyecto utiliza SQLite, que es una base de datos local. Sin embargo, si se migrara a la nube, se podrían implementar las siguientes medidas:

- **Cifrado:** Usar cifrado tanto en tránsito (TLS/SSL) como en reposo para proteger los datos.
- **Autenticación y autorización:** Implementar sistemas de autenticación robustos (OAuth, API keys) para controlar el acceso a los datos.
- **Copias de seguridad:** Configurar copias de seguridad automáticas en la nube para garantizar la disponibilidad de los datos en caso de fallos.

## ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?

- **SQLite:** Se eligió SQLite porque es una base de datos ligera, fácil de integrar en aplicaciones de escritorio y no requiere configuración adicional. Es ideal para proyectos pequeños o medianos que no necesitan escalabilidad masiva.
- **Alternativas:** Otras opciones podrían ser MySQL, PostgreSQL o servicios en la nube como Firebase o AWS DynamoDB. Sin embargo, estas opciones son más complejas de configurar y no son necesarias para el alcance actual del proyecto.

## Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?

Se podría migrar la base de datos a un servicio en la nube como Firebase Realtime Database o AWS RDS. Esto permitiría acceder a las tareas desde múltiples dispositivos y mejorar la escalabilidad. Además, se podrían implementar funciones de sincronización en tiempo real.

# Seguridad y regulación (5i)

## ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?

- **Validación de entradas:** Se valida que los datos ingresados por el usuario sean correctos y estén dentro de los rangos esperados.
- **Protección de la base de datos:** Aunque SQLite es local, se asegura que la base de datos no sea accesible directamente por usuarios no autorizados.
- **Cálculo automático de prioridades:** Se evita la manipulación manual de la prioridad, lo que reduce el riesgo de errores o inconsistencias.

## ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?

- **GDPR:** Si el software se utiliza en la Unión Europea o maneja datos de ciudadanos europeos, se debe cumplir con el Reglamento General de Protección de Datos (GDPR). Esto incluye:
  - **Consentimiento:** Informar al usuario sobre cómo se utilizan sus datos.
  - **Derecho al olvido:** Permitir que los usuarios eliminen sus datos de forma permanente.
  - **Acceso y portabilidad:** Permitir que los usuarios exporten sus datos en un formato estándar.
- En este proyecto, aunque los datos son locales, se podría implementar una funcionalidad para exportar/eliminar datos de manera sencilla.

## Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?

- **Riesgos:** Manipulación de datos, acceso no autorizado a la base de datos, o pérdida de datos por fallos en el sistema.
- **Medidas futuras:** Implementar cifrado de la base de datos, autenticación de usuarios, y copias de seguridad automáticas.

# Implicación de las THD en negocio y planta (2e)

## ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?

- **Negocio:** El software podría mejorar la productividad al ayudar a los empleados a priorizar tareas y gestionar su tiempo de manera más eficiente.
- **Planta industrial:** Podría utilizarse para gestionar tareas de mantenimiento, asignando prioridades en función de la urgencia y la importancia.

## ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?

Al automatizar la priorización de tareas, el software permite a los usuarios enfocarse en las actividades más críticas, mejorando la eficiencia y reduciendo el riesgo de olvidar tareas importantes.

## Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?

- **Educación:** Estudiantes y profesores podrían usarlo para gestionar tareas académicas.
- **Salud:** Personal médico podría priorizar tareas en función de la urgencia de los casos.

# Mejoras en IT y OT (2f)

## ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?

El software podría integrarse con sistemas de gestión de tareas en entornos OT (Operational Technology) para priorizar actividades de mantenimiento o producción en función de su urgencia e importancia.

## ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?

- **Mantenimiento preventivo:** Priorizar tareas de mantenimiento en función de la criticidad de los equipos.
- **Gestión de proyectos:** Automatizar la asignación de prioridades en proyectos complejos.

## Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?

Se podría adaptar para gestionar tareas en desarrollo de software, priorizando bugs o features en función de su impacto y urgencia.

# Tecnologías Habilitadoras Digitales (2g)

## ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?

- **Tecnologías actuales:** SQLite (base de datos), Tkinter (interfaz gráfica).
- **Tecnologías futuras:** Integración con APIs de calendarios (Google Calendar, Outlook), uso de machine learning para mejorar la priorización automática, o migración a la nube (Firebase, AWS).

## ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?

- **SQLite:** Proporciona un almacenamiento persistente y eficiente.
- **Tkinter:** Permite una interfaz gráfica intuitiva y fácil de usar.
- **APIs de calendarios:** Mejorarían la integración con otras herramientas de productividad.
- **Machine learning:** Podría mejorar la precisión de la priorización automática.

## Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?

Se podrían integrar tecnologías como IA para analizar patrones de uso y sugerir mejoras en la priorización, o blockchain para garantizar la integridad y trazabilidad de las tareas.

---

# Análisis de Utilidad y Aplicación - Fase 2

## Criterio 6a) Objetivos estratégicos

**¿Qué objetivos estratégicos específicos de la empresa aborda tu software?**
- El software ayuda a gestionar mejor el tiempo del equipo, automatizando la organización de tareas según su urgencia e importancia. Además, digitaliza procesos que antes se hacían manualmente con listas en papel o Excel.

**¿Cómo se alinea el software con la estrategia general de digitalización?**
- Forma parte de la transformación digital al eliminar métodos analógicos, centralizando toda la planificación en un sistema accesible que además genera datos para mejorar la productividad.

## Criterio 6b) Áreas de negocio y comunicaciones

**¿Qué áreas de la empresa (producción, negocio, comunicaciones) se ven más beneficiadas con tu software?**
- Las áreas más beneficiadas son producción (para organizar tareas operativas), negocio (para gestionar proyectos) y comunicaciones (para coordinar entre departamentos), ya que todas necesitan priorizar trabajo diario.

**¿Qué impacto operativo esperas en las operaciones diarias?**
- Se reducirá el tiempo perdido en planificación y se evitarán olvidos de tareas importantes, haciendo el flujo de trabajo más ágil y confiable.

## Criterio 6c) Áreas susceptibles de digitalización

**¿Qué áreas de la empresa son más susceptibles de ser digitalizadas con tu software?**
- La gestión de proyectos entre equipos, el plan de mantenimiento de equipos y el seguimiento de objetivos por empleado son ideales para digitalizar con esta herramienta.

**¿Cómo mejorará la digitalización las operaciones en esas áreas?**
- Al digitalizarse, habrá menos errores al priorizar, se podrá acceder a las tareas desde cualquier lugar y quedará registro de todo lo completado.

## Criterio 6d) Encaje de áreas digitalizadas (AD)

**¿Cómo interactúan las áreas digitalizadas con las no digitalizadas?**
- El software genera informes imprimibles para quienes prefieren papel y envía notificaciones por email, funcionando como puente entre ambos formatos de trabajo.

**¿Qué soluciones o mejoras propondrías para integrar estas áreas?**
- Podría añadirse sincronización con calendarios físicos y pantallas en zonas comunes que muestren las tareas prioritarias del día.

## Criterio 6e) Necesidades presentes y futuras

**¿Qué necesidades actuales de la empresa resuelve tu software?**
- Resuelve la falta de un sistema centralizado para organizar tareas, la dificultad para priorizar objetivamente y el problema de medir la carga real de trabajo.

## Criterio 6f) Relación con tecnologías

**¿Qué tecnologías habilitadoras has empleado y cómo impactan en las áreas de la empresa?**
- Usamos SQLite para guardar los datos localmente, Tkinter para una interfaz simple y Python que permite fácil integración. Esto hace el sistema accesible, sin costes adicionales y compatible con cualquier equipo.

**¿Qué beneficios específicos aporta la implantación de estas tecnologías?**
- No requiere licencias, funciona en cualquier ordenador y es fácil de mantener, ideal para empresas que inician su digitalización.

## Criterio 6g) Brechas de seguridad

**¿Qué posibles brechas de seguridad podrían surgir al implementar tu software?**
- Principalmente acceso no autorizado a la base de datos local o pérdida de información por fallos técnicos, al ser un sistema que trabaja con datos locales.

**¿Qué medidas concretas propondrías para mitigarlas?**
- Implementar cifrado del archivo de base de datos, hacer copias de seguridad automáticas y llevar registro de cambios importantes en las tareas.

## Criterio 6h) Tratamiento de datos y análisis

**¿Cómo se gestionan los datos en tu software y qué metodologías utilizas?**
- Los datos se validan al ingresarse, se almacenan ordenadamente en SQLite y los cálculos de prioridad son automáticos para evitar inconsistencias.

**¿Qué haces para garantizar la calidad y consistencia de los datos?**
- El sistema verifica la integridad de los datos al iniciar, tiene pruebas para las funciones clave y permite recuperar información si hay problemas.
