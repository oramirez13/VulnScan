# VulnScan

VulnScan es una aplicación web sencilla en Flask para visualizar el uso de CPU de procesos del sistema.

## Características

- Dashboard `/` con gráfica de los 10 procesos con mayor uso de CPU.
- Ruta `/reporte` con tabla ordenada de procesos y uso de CPU.
- Ruta `/grafica` con la gráfica generada en directo.
- Plantillas HTML separadas para mantener las rutas limpias y fáciles de mantener.

## Requisitos

- Python 3.11+ (recomendado)
- `flask`
- `psutil`
- `matplotlib`

## Instalación

1. Crear un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python app.py
```

Luego abrir en el navegador:

```bash
http://127.0.0.1:5000
```

## Estructura relevante

- `app.py`: punto de entrada de la aplicación.
- `app/__init__.py`: crea la aplicación Flask y registra el blueprint.
- `app/routes.py`: rutas de la aplicación y generación de datos.
- `app/templates/`: plantillas HTML reutilizables.
- `app/static/style.css`: estilos de la interfaz.

## Preparado para GitHub

- El proyecto ya incluye `.gitignore` para excluir `.venv/`, `venv/`, `__pycache__/` y archivos compilados.
- Se recomienda conservar solo un entorno virtual local. En este proyecto la referencia documentada es `.venv/`.
- Antes de publicar, verifica que no queden carpetas del entorno virtual dentro del commit.

## Flujo sugerido para publicar

```bash
cd flask/VulnScan
git init
git add .
git commit -m "Preparar proyecto VulnScan para GitHub"
```
