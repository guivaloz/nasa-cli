"""
Mars Rover Photos
"""
from pathlib import Path

import requests
import rich
import typer
from unidecode import unidecode

from .settings import get_settings

app = typer.Typer()


@app.command()
def mostrar(
    page: int = 1,
    sol: int = 0,
):
    """Mostrar imagenes del Mars Rover"""
    rich.print("Mostrar imagenes del [blue]Mars Rover[/blue]")

    # Cargar configuración
    settings = get_settings()

    # Definir los parametros para la solicitud
    parametros = {
        "api_key": settings.api_key,
        "page": page,
        "sol": sol,
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

    # Mostrar los datos
    rich.pretty.pprint(datos)
