# Transformacion-Digital-Proyecto

# 🎵 Mood Light Sync - Sincroniza Todas tus Luces RGB con el Sonido

## 📌 Descripción
**Mood Light Sync** es un software Open Source que sincroniza las luces RGB de tu PC con el sonido ambiente, la música o la voz en Discord. Funciona con:

- ✅ **Logitech G Hub** (Teclados, ratones y auriculares Logitech)
- ✅ **Corsair iCUE** (RAM, ventiladores y periféricos Corsair)
- ✅ **RGB Fusion (Gigabyte)** (Placas base y GPU con OpenRGB)
- ✅ **OpenRGB** (Para controlar cualquier otro hardware RGB compatible)

Este software analiza el audio en tiempo real y ajusta los colores de tus luces para crear una experiencia visual envolvente.

---

## 🚀 Características
- **Captura y análisis de audio** en tiempo real.
- **Sincronización de iluminación RGB** en múltiples plataformas.
- **Compatibilidad con Logitech, Corsair, Gigabyte y OpenRGB**.
- **Modos de iluminación personalizables**.
- **Integración con Discord** (opcional) para cambiar colores según la voz.
- **Interfaz gráfica interactiva con PyQt6** para personalizar efectos y configuraciones.

---

## 🛠️ Cómo Funciona

- 1️⃣ **Captura de Audio**: El programa usa `pyaudio` para escuchar el sonido en tu PC.
- 2️⃣ **Análisis de Frecuencia**: Se procesa la señal usando FFT para detectar tonos graves, medios y agudos.
- 3️⃣ **Asignación de Colores**: Según la frecuencia detectada, se establecen colores específicos.
- 4️⃣ **Sincronización de Hardware**: Se envían los valores RGB a Logitech G Hub, Corsair iCUE y OpenRGB.
- 5️⃣ **Interacción en Discord** *(opcional)*: Se pueden cambiar colores al hablar en un canal de voz.
- 6️⃣ **Control desde Interfaz Gráfica**: Permite seleccionar modos, ajustar brillo y cambiar configuraciones en tiempo real.

## 📱 Aplicaciones utilizadas

- PyAudio -> Escucha el sonido
- Logitech led illumination sdk -> Integracion de logitech
- iCue sdk -> Integracion de corsair
- RGB Fusion / OpenRGB -> Se envían comandos REST a OpenRGB, integracion de placas gigabyte

## ⚙️ Configuración
Puedes editar el archivo `config.json` para personalizar:
- **Modo de sincronización** (Spotify,Youtube Music ,Discord)
- **Colores según frecuencia**
- **Dispositivos compatibles**

También puedes usar la **interfaz gráfica** para ajustar estos parámetros sin editar el archivo manualmente.

---

## 📌 Futuras Mejoras
- ✅ Integración con más hardwares.
- ✅ Soporte para efectos avanzados con shaders.

---

## 📥 Instalación
### 1️⃣ Requisitos
- Python 3.x
- OpenRGB instalado y en modo servidor (`openrgb --server`)
- Logitech G Hub con SDK activado
- Corsair iCUE con integración habilitada
- Pip y las siguientes librerías:
  ```bash
  pip install pyaudio numpy requests pyqt6
  ```

### 2️⃣ Clonar el repositorio
```bash
git clone https://github.com/tuusuario/mood-light-sync.git
cd mood-light-sync
```

### 3️⃣ Ejecutar el programa
```bash
python mood_light_sync.py
```
