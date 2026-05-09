# VulnScan

VulnScan es una aplicación web en Flask para visualizar el uso de CPU de procesos del sistema.

## Características

- Dashboard `/` con gráfica de los 10 procesos con mayor uso de CPU.
- Ruta `/reporte` con tabla ordenada de procesos y uso de CPU.
- Ruta `/grafica` con la gráfica generada en directo.
- Plantillas HTML separadas para mantener las rutas limpias y fáciles de mantener.

## Requisitos

- Python 3.11+ (recomendado)
- `pip`

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/oramirez13/VulnScan.git
cd VulnScan
```

2. Crear un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Con el entorno virtual activado, ejecutar:

```bash
python app.py
```

Luego abrir en el navegador:

```bash
http://127.0.0.1:5000
```

## Uso

- `/`: muestra el panel principal con la gráfica y la tabla de los 10 procesos con mayor uso de CPU.
- `/reporte`: muestra un reporte más amplio con la lista ordenada de procesos.
- `/grafica`: muestra únicamente la gráfica generada en tiempo real.

## Estructura relevante

- `app.py`: punto de entrada de la aplicación.
- `app/__init__.py`: crea la aplicación Flask y registra el blueprint.
- `app/routes.py`: rutas de la aplicación y generación de datos.
- `app/templates/`: plantillas HTML reutilizables.
- `app/static/style.css`: estilos de la interfaz.
- `requirements.txt`: dependencias necesarias del proyecto.

## Notas

- El proyecto ya incluye `.gitignore` para excluir `.venv/`, `venv/`, `__pycache__/` y archivos compilados.
- Se recomienda conservar solo un entorno virtual local. En este proyecto la referencia documentada es `.venv/`.
