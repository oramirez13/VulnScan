from flask import Blueprint, render_template
import psutil
import io
import base64

import matplotlib

# Esta linea obliga a Matplotlib a generar imagenes sin abrir una ventana grafica.
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Este blueprint agrupa las rutas principales de la aplicacion.
bp = Blueprint("app", __name__)


def format_cpu_value(cpu_value):
    # Si el valor viene vacio, devolvemos 0.0 para evitar errores en la vista.
    if cpu_value is None:
        return 0.0

    # Convertimos el valor a float para trabajar siempre con el mismo tipo.
    return float(cpu_value)


def get_processes(top_n=None):
    # Esta lista almacenara los procesos ya preparados para mostrarse en pantalla.
    processes = []

    # Recorremos los procesos del sistema pidiendo solo los datos que necesitamos.
    for process in psutil.process_iter(["pid", "name", "cpu_percent"]):
        # Leemos el PID actual del proceso.
        pid = process.info["pid"]

        # Si el nombre no existe, mostramos un texto simple para mantener la tabla clara.
        name = process.info["name"] or "Proceso sin nombre"

        # Normalizamos el porcentaje de CPU para evitar valores nulos.
        cpu = format_cpu_value(process.info["cpu_percent"])

        # Guardamos cada proceso como una tupla sencilla para que Jinja lo recorra facil.
        processes.append((pid, name, cpu))

    # Ordenamos los procesos desde el mayor consumo de CPU hasta el menor.
    processes.sort(key=lambda item: item[2], reverse=True)

    # Si no se pidio un limite, devolvemos toda la lista ordenada.
    if top_n is None:
        return processes

    # Si se pidio un limite, devolvemos solo esa cantidad de procesos.
    return processes[:top_n]


def build_chart(processes):
    # Extraemos los porcentajes de CPU para usarlos como valores de la grafica.
    cpu_values = [process[2] for process in processes]

    # Construimos las etiquetas combinando nombre del proceso y PID.
    process_names = [f"{process[1]} ({process[0]})" for process in processes]

    # Creamos una figura nueva con un tamano suficiente para que se lean las barras.
    plt.figure(figsize=(10, 5))

    # Dibujamos una grafica horizontal para comparar mejor los procesos.
    plt.barh(process_names, cpu_values, color="orange")

    # Etiquetamos el eje horizontal para indicar la unidad mostrada.
    plt.xlabel("Uso de CPU (%)")

    # Agregamos un titulo breve a la grafica.
    plt.title("Top 10 procesos con mayor uso de CPU")

    # Ajustamos los margenes para que las etiquetas no queden cortadas.
    plt.tight_layout()

    # Creamos un buffer en memoria para guardar la imagen sin escribir archivos temporales.
    image_buffer = io.BytesIO()

    # Guardamos la figura en formato PNG dentro del buffer.
    plt.savefig(image_buffer, format="png")

    # Cerramos la figura para liberar memoria despues de generarla.
    plt.close()

    # Volvemos al inicio del buffer para poder leer su contenido completo.
    image_buffer.seek(0)

    # Convertimos la imagen a base64 para incrustarla directamente en el HTML.
    return base64.b64encode(image_buffer.getvalue()).decode()


@bp.route("/")
def index():
    # Obtenemos solo los 10 procesos principales para el panel principal.
    processes = get_processes(top_n=10)

    # Generamos la grafica a partir de esos procesos.
    graph_url = build_chart(processes)

    # Renderizamos la plantilla principal con la tabla y la grafica.
    return render_template("index.html", processes=processes, graph_url=graph_url)


@bp.route("/reporte")
def reporte():
    # Obtenemos todos los procesos ordenados para el reporte completo.
    processes = get_processes()

    # Mostramos la informacion usando una plantilla separada.
    return render_template("reporte.html", processes=processes)


@bp.route("/grafica")
def solo_grafica():
    # Obtenemos los 10 procesos mas importantes para la vista de solo grafica.
    processes = get_processes(top_n=10)

    # Construimos la imagen que se mostrara en la pagina.
    graph_url = build_chart(processes)

    # Renderizamos la plantilla dedicada a la grafica.
    return render_template("grafica.html", graph_url=graph_url)
