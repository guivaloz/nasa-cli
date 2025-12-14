"""
APOD: Astronomy Picture of the Day
"""

from datetime import date
from pathlib import Path

import requests
from rich.console import Console
from rich.table import Table
from typer import Typer, Option
from unidecode import unidecode

from .settings import get_settings

app = Typer()

HOY = date.today().strftime("%Y-%m-%d")


@app.command()
def bajar(
    fecha: str = Option(HOY, help="Fecha de la foto"),
):
    """Bajar el Astronomy Picture of the Day"""
    console = Console()
    console.print(f"Bajar el [blue]Astronomy Picture of the Day[/blue] de [green]{fecha}[/green]")

    # Cargar configuración
    settings = get_settings()

    # Mostrar la URL de la foto
    try:
        url = f"{settings.BASE_URL}?api_key={settings.API_KEY}&date={fecha}"
        respuesta = requests.get(url, timeout=settings.TIMEOUT)
        datos = respuesta.json()
    except requests.exceptions.HTTPError as error:
        console.print(f"[red]Error {error.response.status_code}[/red]")
        console.print(error.response.text)
    except requests.exceptions.RequestException as error:
        console.print("[red]Error[/red]")
        console.print(error)

    # Si es una imagen
    if datos["media_type"] == "image":

        # Definir el nombre del archivo
        nombre = unidecode(datos["title"].lower().replace(" ", "_"))
        extension = datos["url"].split(".")[-1]
        archivo = Path(f"{nombre}.{extension}")

        # Si ya existe el archivo, no hacer nada
        if archivo.exists():
            console.print(f"El archivo [yellow]{archivo}[/yellow] ya existe")
            return

        # Bajar la imagen
        try:
            respuesta = requests.get(datos["url"], timeout=settings.TIMEOUT)
            with open(archivo, "wb") as f:
                f.write(respuesta.content)
            console.print(f"Archivo [green]{archivo}[/green] guardado")
        except requests.exceptions.HTTPError as error:
            console.print(f"[red]Error {error.response.status_code}[/red]")
            console.print(error.response.text)
        except requests.exceptions.RequestException as error:
            console.print("[red]Error[/red]")
            console.print(error)


@app.command()
def bajar_rango(
    desde: str = Option(HOY, help="Fecha de inicio AAAA-MM-DD"),
    hasta: str = Option(HOY, help="Fecha de termino AAAA-MM-DD"),
):
    """Bajar un rango de imagenes del Astronomy Picture of the Day"""
    console = Console()
    console.print(f"Bajar las imagenes [blue]Astronomy Picture of the Day[/blue] del [green]{desde}[/green] al [green]{hasta}[/green]")

    # Cargar configuración
    settings = get_settings()

    # Definir los parametros para la solicitud
    parametros = {
        "api_key": settings.API_KEY,
        "start_date": desde,
        "end_date": hasta,
    }

    # Solicitar a la API las imagenes
    try:
        respuesta = requests.get(settings.BASE_URL, params=parametros, timeout=settings.TIMEOUT)
        respuesta.raise_for_status()
        datos = respuesta.json()
    except requests.exceptions.HTTPError as error:
        console.print(f"[red]Error {error.response.status_code}[/red]")
        console.print(error.response.text)
    except requests.exceptions.RequestException as error:
        console.print("[red]Error[/red]")
        console.print(error)

    # Elaborar tabla
    tabla = Table()
    tabla.add_column("Fecha", justify="center")
    tabla.add_column("Titulo", justify="left")
    tabla.add_column("Media", justify="left")
    tabla.add_column("URL", justify="left")

    # Bucle en los datos de la respuesta de la API
    for dato in datos:

        # Si es una imagen
        if dato["media_type"] == "image":

            # Definir el nombre del archivo
            nombre = unidecode(dato["title"].lower().replace(" ", "_"))
            extension = dato["url"].split(".")[-1]
            archivo = Path(f"{nombre}.{extension}")

            # Si ya existe el archivo, no hacer nada
            if archivo.exists():
                console.print(f"El archivo [yellow]{archivo}[/yellow] ya existe")
                continue

            # Bajar la imagen
            try:
                respuesta = requests.get(dato["url"], timeout=settings.TIMEOUT)
                respuesta.raise_for_status()
                with open(archivo, "wb") as f:
                    f.write(respuesta.content)
                console.print(f"Archivo [green]{archivo}[/green] guardado...")
            except requests.exceptions.HTTPError as error:
                console.print(f"[red]Error {error.response.status_code}[/red]")
                console.print(error.response.text)
            except requests.exceptions.RequestException as error:
                console.print("[red]Error[/red]")
                console.print(error)

        # Agregar renglon a la tabla
        tabla.add_row(
            dato["date"],
            dato["title"],
            dato["media_type"],
            dato["url"],
        )

    # Mostrar tabla
    console.print(tabla)
