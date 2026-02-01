# Automatizador de búsquedas para Microsoft Edge

Este script prueba automatización de búsquedas en Microsoft Edge utilizando temas aleatorios de la API de Wikipedia.

---

## Requisitos Previos

Para ejecutar este automatizador, es necesario contar con:

* **Python 3.10 o superior:** [Página Oficial](https://www.python.org/downloads/)
* **Conexión a Internet:** Necesaria para las consultas a la API de Wikipedia y el registro de navegación.

## Configuración del Entorno

### 1. Crear el entorno virtual

```powershell
python -m venv env
```

### 2. Activar el entorno

```powershell
.\env\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```powershell
pip install -r requirements.txt
```

---

## Configuración Inicial

### Verificar ruta de Microsoft Edge

Antes de ejecutar el script, **verificar que la ruta de Edge sea correcta** en tu sistema:

**Ruta por defecto en el script:**

`C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`

**Rutas alternativas comunes:**

* `C:\Program Files\Microsoft\Edge\Application\msedge.exe` (versión 64 bits)

* `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` (versión 32 bits)

Para verificar tu ruta:

1. Abrir el Explorador de Archivos
2. Navegar a `C:\Program Files` o `C:\Program Files (x86)`
3. Buscar la carpeta `Microsoft\Edge\Application`
4. Si la ruta es diferente, editar la variable `ruta_edge` en `main.py` (línea 24)

---

## Uso y Ejecución

Se puede correr el programa de dos maneras:

* **Directo:** `python main.py` (asegurándote de tener el entorno activo)

* **Lanzador:** Ejecutando el archivo `CorrerBusquedas.bat`

### Cómo detener el script

Para cancelar las búsquedas en cualquier momento:

-Presionar **Ctrl + C** en la terminal
-O simplemente cerrar la ventana de la consola/terminal

---

## Lanzador Automático (.bat)

Como el archivo `.bat` está incluido en el `.gitignore` por seguridad de rutas, se debe crear localmente para ejecutar el script con un solo click:

### Pasos

1. Crear un archivo llamado `CorrerBusquedas.bat` en la raíz del proyecto
2. Pegar el siguiente código:

```batch
@echo off
title Lanzador de Busquedas Edge
cd /d "%~dp0"
echo Activando entorno virtual...
call .\env\Scripts\activate.bat
echo Iniciando script de Python...
python main.py
pause
```

> **Nota:** El comando `%~dp0` permite que el archivo funcione de forma portátil, detectando automáticamente la carpeta donde esté guardado el proyecto.

---

## Funcionamiento del Script

### Características de seguridad

* **Búsquedas aleatorias:** Utiliza la API de Wikipedia para obtener 30 temas aleatorios reales
* **Intervalos variables:** Espera entre 8-17 segundos entre búsquedas para simular comportamiento humano
* **Pausas de seguridad:** Cada 10 búsquedas hace una pausa larga de 25-60 segundos
* **IDs únicos:** Genera un identificador de sesión único (CVID) para cada búsqueda
* **User-Agent real:** Simula un navegador Chrome para evitar bloqueos de API

### Navegación Interactiva

El script ejecuta un ciclo de **30 consultas automatizadas**, permitiendo al usuario monitorear y detener el proceso en cualquier momento. A diferencia de otros automatizadores, este mantiene la visibilidad de las pestañas a medida que se abren, permitiendo la exploración inmediata de los resultados y la interacción directa con el contenido generado en cada paso.

---

## Notas de Mantenimiento

* **Errores de API:** Si el script no conecta a la API de Wikipedia (error de conexión, SSL o timeout), verificá tu conexión a internet. El script tiene un respaldo que generará búsquedas genéricas automáticamente.

* **Error: 'python' no se reconoce como un comando interno:** Esto sucede si Python no fue agregado a las variables de entorno durante la instalación. Para solucionarlo:
  * Busca "Editar las variables de entorno del sistema" en Windows.
  * En Variables de entorno, busca la variable Path y asegurate de que incluya la ruta a tu carpeta de Python y a la carpeta Scripts.
  * Reinicia la terminal para que los cambios surtan efecto.

---

## Solución de Problemas

### El script no inicia Edge

* Verificar que la ruta de Edge sea correcta (ver sección "Configuración Inicial")
* Asegurarte de que Edge esté instalado en tu sistema

### Si la actividad de navegación no aparece en el historial

* Sincronización de sesión: Si bien el script funciona de forma independiente, para que el historial se sincronice con una cuenta específica, asegurate de que el perfil de Edge esté activo.
* Intervalos de seguridad: Si el motor de búsqueda no procesa alguna consulta, es recomendable aumentar los tiempos de espera en main.py (líneas 45-51). Esto asegura que la navegación sea interpretada correctamente por los servidores de destino.
* Respuesta del servidor: En caso de latencia alta, el script utilizará automáticamente el sistema de respaldo para completar el ciclo de 30 consultas.
