"""
APOD: Astronomy Picture of the Day
"""
from datetime import date
from pathlib import Path

import requests
import rich
import typer
from unidecode import unidecode

from .settings import get_settings

app = typer.Typer()

HOY = date.today().strftime("%Y-%m-%d")


@app.command()
def bajar(
    fecha: str = typer.Option(HOY, help="Fecha de la foto"),
):
    """Bajar el Astronomy Picture of the Day"""
    rich.print(f"Bajar el [blue]Astronomy Picture of the Day[/blue] de [green]{fecha}[/green]")

    # Cargar configuración
    settings = get_settings()

    # Mostrar la URL de la foto
    try:
        url = f"{settings.base_url}?api_key={settings.api_key}&date={fecha}"
        respuesta = requests.get(url, timeout=settings.timeout)
        datos = respuesta.json()
    except requests.exceptions.HTTPError as error:
        rich.print(f"[red]Error {error.response.status_code}[/red]")
        rich.print(error.response.text)
    except requests.exceptions.RequestException as error:
        rich.print("[red]Error[/red]")
        rich.print(error)

    # Si es una imagen
    if datos["media_type"] == "image":

        # Definir el nombre del archivo
        nombre = unidecode(datos["title"].lower().replace(" ", "_"))
        extension = datos["url"].split(".")[-1]
        archivo = Path(f"{nombre}.{extension}")

        # Si ya existe el archivo, no hacer nada
        if archivo.exists():
            rich.print(f"El archivo [yellow]{archivo}[/yellow] ya existe")
            typer.Exit(0)

        # Bajar la imagen
        try:
            respuesta = requests.get(datos["url"], timeout=settings.timeout)
            with open(archivo, "wb") as f:
                f.write(respuesta.content)
            rich.print(f"Archivo [green]{archivo}[/green] guardado")
        except requests.exceptions.HTTPError as error:
            rich.print(f"[red]Error {error.response.status_code}[/red]")
            rich.print(error.response.text)
        except requests.exceptions.RequestException as error:
            rich.print("[red]Error[/red]")
            rich.print(error)


@app.command()
def bajar_rango(
    desde: str = typer.Option(HOY, help="Fecha de inicio AAAA-MM-DD"),
    hasta: str = typer.Option(HOY, help="Fecha de termino AAAA-MM-DD"),
):
    """Bajar un rango de imagenes del Astronomy Picture of the Day"""
    rich.print(f"Bajar las imagenes [blue]Astronomy Picture of the Day[/blue] del [green]{desde}[/green] al [green]{hasta}[/green]")

    # Cargar configuración
    settings = get_settings()

    # Definir los parametros para la solicitud
    parametros = {
        "api_key": settings.api_key,
        "start_date": desde,
        "end_date": hasta,
    }

    # Solicitar a la API las imagenes
    try:
        respuesta = requests.get(settings.base_url, params=parametros, timeout=settings.timeout)
        respuesta.raise_for_status()
        datos = respuesta.json()
    except requests.exceptions.HTTPError as error:
        rich.print(f"[red]Error {error.response.status_code}[/red]")
        rich.print(error.response.text)
    except requests.exceptions.RequestException as error:
        rich.print("[red]Error[/red]")
        rich.print(error)

    # Elaborar tabla
    tabla = rich.table.Table()
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
                rich.print(f"El archivo [yellow]{archivo}[/yellow] ya existe")
                continue

            # Bajar la imagen
            try:
                respuesta = requests.get(dato["url"], timeout=settings.timeout)
                respuesta.raise_for_status()
                with open(archivo, "wb") as f:
                    f.write(respuesta.content)
                rich.print(f"Archivo [green]{archivo}[/green] guardado...")
            except requests.exceptions.HTTPError as error:
                rich.print(f"[red]Error {error.response.status_code}[/red]")
                rich.print(error.response.text)
            except requests.exceptions.RequestException as error:
                rich.print("[red]Error[/red]")
                rich.print(error)

        # Agregar renglon a la tabla
        tabla.add_row(
            dato["date"],
            dato["title"],
            dato["media_type"],
            dato["url"],
        )

    # Mostrar tabla
    consola = rich.console.Console()
    consola.print(tabla)
